import requests
import arxiv
import paths
import time
from lxml import html
import os

query = '(abs:"record linkage" OR abs:"entity resolution")'
query1 = '(abs:"synthetic data generation")'

search = arxiv.Search(
    query=query1,
    max_results=600,
    sort_by=arxiv.SortCriterion.SubmittedDate,
)

print(f"Query: {query}")

if not os.path.exists(paths.HTML_FOLDER):
    os.makedirs(paths.HTML_FOLDER)

for result in search.results():
    paper_id = result.get_short_id().split("v")[0]

    url = f"https://ar5iv.labs.arxiv.org/html/{paper_id}"

    time.sleep(0.5)

    response = requests.get(url, allow_redirects=False)

    if response.status_code in (301, 302, 307, 308):
        url = response.headers["Location"].replace("abs", "html")
        print(f"Redirected to {url}")
        response = requests.get(url, allow_redirects=False)

    if response.status_code == 404:
        print(f"404 Not Found for {url}")
        continue

    if response.status_code != 200:
        print(f"Failed to open {url}")
        continue

    if "reCAPTCHA" in response.text:
        print("reCAPTCHA detected")
        continue

    html_content = str(response.text)

    with open(f"{paths.HTML_FOLDER}/{paper_id}.html", "w", encoding="utf-8") as file:
            file.write(html_content)    