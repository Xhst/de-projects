from table_processing import clean_table, parse_html_table
from llm import query_groq
from examples import example1, example2, example3, example_data_table
import paths
import json

def extract_table_claims(table_data: dict) -> str:
    """
    Function to extract claims from a table in a research paper.

    Args:
        table_data (dict): The data of the table to extract claims from.

    Returns:
        str: The extracted claims from the table.
    """
    html_content = clean_table(table_data['table'])
    parsed_table = parse_html_table(html_content)
    
    print(parsed_table)

    system_prompt = """You are an expert in computer science and in understanding tables.
    Your task is to extract claims from papers' tables provided with their captions and references in this format:
    |{|Specification 1, Value|, |Specification 2, Value|}, Metric, Metric Value|

    Example: """ + example3.__str__() + """
    
    ---
    Note that when no metrics are inside the table (data table) we only want the specifications included, without any "metric" field.
    Like in this examples:
    Example data table:
    """ + example_data_table.__str__() + """
    ---
    Response MUST only include the claims, nothing else.
    """

    content = f"""
    Please provide the claims from the following table:
    [Table]: 
    {parsed_table}
    [Caption]: 
    {table_data['caption']}
    [References]: 
    {table_data['references']}
    
    """ # TODO: questo pezzo può essere tolto, per ora non si comporta benissimo POTREBBE ESSE UNA BUONA IDEA
    #These are some claims from the same paper for context:
    #""" + """|{|Dataset, ID|, |Range, [1,60]|, |Number of Integers, 5|, |Fine-tuned on, 1M|}, Zero-shot pass@1, 0.224|
    #|{|Dataset, Numerical OOD|, |Range, [1,100]|, |Number of Integers, 7|, |Fine-tuned on, 100M|}, Zero-shot pass@1, 0.315|
    #|{|Dataset, Form OOD|, |Range, [1,60]|, |Number of Integers, 8|, |Fine-tuned on, 1M|}, Zero-shot pass@1, 0.169|
    """---
    
    Response MUST only include the claims, nothing else.
    """
    
    return query_groq(messages=[
        {
            "role": "system",
            "content": system_prompt
        },
        {
            "role": "user",
            "content": content
        }
    ])

if __name__ == "__main__":
    with open(paths.RAW + '/2406.02100.json', 'r') as file:
        data = json.load(file)
        table_data = data['A1.T6']

    response = extract_table_claims(table_data)

    print("\n\033[92mLLM response:\033[0m\n")
    print(response)

    