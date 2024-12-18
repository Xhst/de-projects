from dataclasses import dataclass

@dataclass
class ExtractionExample:
    table: str
    caption: str
    references: list[str]
    result: str

    def __str__(self):
        return f"""
        [Table]: 
        {self.table}
        [Caption]: 
        {self.caption}
        [References]: 
        {self.references}
        [Response]: 
        {self.result}
        """

example1 = ExtractionExample(
    table="""
    ----------  -------------  -------------  -------------  -------------  -------------  -------------
                Lively         Lively         Harsh          Harsh          Wellcoming     Wellcoming
    Model       SI-MOS         N-MOS          SI-MOS         N-MOS          SI-MOS         N-MOS
    GT          4.49  ±  0.14  4.28  ±  0.38  4.52  ±  0.14  4.85  ±  0.21  4.01  ±  0.26  4.28  ±  0.29
    Synth none  2.67  ±  0.26  1.74  ±  0.24  2.71  ±  0.14  2.20  ±  0.22  2.63  ±  0.17  2.33  ±  0.27
    Synth TTS   2.65  ±  0.15  2.55  ±  0.16  2.17  ±  0.15  2.11  ±  0.19  2.99  ±  0.14  2.55  ±  0.27
    Synth both  2.24  ±  0.14  2.90  ±  0.31  2.25  ±  0.15  2.28  ±  0.20  3.06  ±  0.17  3.44  ±  0.28
    VC          3.04  ±  0.16  3.66  ±  0.26  1.93  ±  0.29  3.66  ±  0.38  3.61  ±  0.19  3.95  ±  0.54
    ----------  -------------  -------------  -------------  -------------  -------------  -------------
    """,
    caption="Table 3: Style Intensity (SI-MOS) and Naturalness (N-MOS) Mean Opinion Scores with 95% confidence intervals.",
    references=[
        """
        The results indicate that synthetic data generated by voice conversion (VC) exhibit higher naturalness than those from cross-speaker style transfer experiments.
        Consequently, both the Synth TTS and Synth both experiments, which incorporate synthetic data during training, show increased naturalness compared to Synth None, with Synth both demonstrating the highest improvement.
        However, we note that for style intensity, the Synth none configuration performed better in two out of three expressive styles in the dataset, despite having lower naturalness in each case (Table 3).
        """
    ],
    result="""
    { "Model": "GT", "Speaker-Style": "Lively", "SI-MOS": "4.49 ± 0.14", "N-MOS": "4.28 ± 0.38" },
    { "Model": "GT", "Speaker-Style": "Harsh", "SI-MOS": "4.52 ± 0.14", "N-MOS": "4.85 ± 0.21" },
    { "Model": "GT", "Speaker-Style": "Wellcoming", "SI-MOS": "4.01 ± 0.26", "N-MOS": "4.28 ± 0.29" },
    { "Model": "Synth none", "Speaker-Style": "Lively", "SI-MOS": "2.67 ± 0.26", "N-MOS": "1.74 ± 0.24" },
    { "Model": "Synth none", "Speaker-Style": "Harsh", "SI-MOS": "2.71 ± 0.14", "N-MOS": "2.20 ± 0.22" },
    { "Model": "Synth none", "Speaker-Style": "Wellcoming", "SI-MOS": "2.63 ± 0.17", "N-MOS": "2.33 ± 0.27" },
    { "Model": "Synth TTS", "Speaker-Style": "Lively", "SI-MOS": "2.65 ± 0.15", "N-MOS": "2.55 ± 0.16" },
    { "Model": "Synth TTS", "Speaker-Style": "Harsh", "SI-MOS": "2.17 ± 0.15", "N-MOS": "2.11 ± 0.19" },
    { "Model": "Synth TTS", "Speaker-Style": "Wellcoming", "SI-MOS": "2.99 ± 0.14", "N-MOS": "2.55 ± 0.27" },
    { "Model": "Synth both", "Speaker-Style": "Lively", "SI-MOS": "2.24 ± 0.14", "N-MOS": "2.90 ± 0.31" },
    { "Model": "Synth both", "Speaker-Style": "Harsh", "SI-MOS": "2.25 ± 0.15", "N-MOS": "2.28 ± 0.20" },
    { "Model": "Synth both", "Speaker-Style": "Wellcoming", "SI-MOS": "3.06 ± 0.17", "N-MOS": "3.44 ± 0.28" },
    { "Model": "Voice Conversion (VC)", "Speaker-Style": "Lively", "SI-MOS": "3.04 ± 0.16", "N-MOS": "3.66 ± 0.26" },
    { "Model": "Voice Conversion (VC)", "Speaker-Style": "Harsh", "SI-MOS": "1.93 ± 0.29", "N-MOS": "3.66 ± 0.38" },
    { "Model": "Voice Conversion (VC)", "Speaker-Style": "Wellcoming", "SI-MOS": "3.61 ± 0.19", "N-MOS": "3.95 ± 0.54" }
    """
)

example2 = ExtractionExample(
    table="""
    -----------------  ---------------------  --------------  -------  -------  -------  -------  -----
    Model Type         Model Name             Parameter Size  Level 1  Level 2  Level 3  Level 4  All
    General LLM        ChatGPT-3.5-turbo      175B            0.760    0.799    0.408    0.493    0.623
    General LLM        DIN-SQL+GPT-4          1.76T           0.861    0.866    0.700    0.654    0.762
    General LLM        CodeX-Davinci-3        175B            0.730    0.799    0.392    0.382    0.570
    General LLM        MPT-7B-instruct        7B              0.262    0.381    0.117    0.091    0.205
    General LLM        ALPACA                 7B              0.311    0.460    0.192    0.083    0.242
    General LLM        KOALA                  7B              0.195    0.218    0.017    0.071    0.131
    General LLM        OpenAssistant-pythia   12B             0.202    0.322    0.025    0.069    0.157
    General LLM        ORCA-mini              7B              0.243    0.280    0.101    0.076    0.169
    General LLM        LLaMA-2                7B              0.225    0.393    0.101    0.081    0.192
    Code Specific LLM  CodeGen2               7B              0.375    0.498    0.167    0.066    0.257
    Code Specific LLM  Starcoder              15.5B           0.584    0.628    0.275    0.208    0.410
    Code Specific LLM  Vicuna                 7B              0.060    0.134    0.008    0.042    0.064
    Code Specific LLM  nsql                   6B              0.772    0.732    0.608    0.277    0.548
    Seq-to-Seq Model   T5(tscholak/cxmefzzi)  3B              0.828    0.782    0.650    0.434    0.641
    Seq-to-Seq Model   PICARD+T5              3B              0.790    0.799    0.558    0.502    0.652
    Seq-to-Seq Model   RESDSQL                3B              0.872    0.857    0.666    0.696    0.775
    -----------------  ---------------------  --------------  -------  -------  -------  -------  -----
    """,
    
    caption="Table 1. Benchmark Results of Execution Match of all Models we tested on the 'dev' SPIDER dataset",
    
    references=["""
                In our experimentation, we organized the models into three distinct groups as illustrated in Table 1: general purpose LLMs, Code-Specific LLMs, and Sequence-to-Sequence models. Table 1 further presents the Execution Match score on the SPIDER dataset for each studied LLM and for each of the four difficulty levels.
                """],
    result="""
    |{|Model Type, General LLM|, |Model Name, ChatGPT-3.5-turbo|, |Parameter Size, 175B|, |Dataset, Spider dev|, |Difficulty Level, 1|}, Execution Match , 0.760|
|{|Model Type, General LLM|, |Model Name, ChatGPT-3.5-turbo|, |Parameter Size, 175B|, |Dataset, Spider dev|, |Difficulty Level, 2|}, Execution Match , 0.799|
|{|Model Type, General LLM|, |Model Name, ChatGPT-3.5-turbo|, |Parameter Size, 175B|, |Dataset, Spider dev|, |Difficulty Level, 3|}, Execution Match , 0.408|
|{|Model Type, General LLM|, |Model Name, ChatGPT-3.5-turbo|, |Parameter Size, 175B|, |Dataset, Spider dev|, |Difficulty Level, 4|}, Execution Match , 0.493|
|{|Model Type, General LLM|, |Model Name, ChatGPT-3.5-turbo|, |Parameter Size, 175B|, |Dataset, Spider dev|, |Difficulty Level, All|}, Execution Match , 0.623|
|{|Model Type, General LLM|, |Model Name, DIN-SQL+GPT-4|, |Parameter Size, 1.76T|, |Dataset, Spider dev|, |Difficulty Level, 1|}, Execution Match , 0.861|
|{|Model Type, General LLM|, |Model Name, DIN-SQL+GPT-4|, |Parameter Size, 1.76T|, |Dataset, Spider dev|, |Difficulty Level, 2|}, Execution Match , 0.866|
|{|Model Type, General LLM|, |Model Name, DIN-SQL+GPT-4|, |Parameter Size, 1.76T|, |Dataset, Spider dev|, |Difficulty Level, 3|}, Execution Match , 0.700|
|{|Model Type, General LLM|, |Model Name, DIN-SQL+GPT-4|, |Parameter Size, 1.76T|, |Dataset, Spider dev|, |Difficulty Level, 4|}, Execution Match , 0.654|
|{|Model Type, General LLM|, |Model Name, DIN-SQL+GPT-4|, |Parameter Size, 1.76T|, |Dataset, Spider dev|, |Difficulty Level, All|}, Execution Match , 0.762|
|{|Model Type, General LLM|, |Model Name, CodeX-Davinci-3|, |Parameter Size, 175B|, |Dataset, Spider dev|, |Difficulty Level, 1|}, Execution Match , 0.730|
|{|Model Type, General LLM|, |Model Name, CodeX-Davinci-3|, |Parameter Size, 175B|, |Dataset, Spider dev|, |Difficulty Level, 2|}, Execution Match , 0.799|
|{|Model Type, General LLM|, |Model Name, CodeX-Davinci-3|, |Parameter Size, 175B|, |Dataset, Spider dev|, |Difficulty Level, 3|}, Execution Match , 0.392|
|{|Model Type, General LLM|, |Model Name, CodeX-Davinci-3|, |Parameter Size, 175B|, |Dataset, Spider dev|, |Difficulty Level, 4|}, Execution Match , 0.382|
|{|Model Type, General LLM|, |Model Name, CodeX-Davinci-3|, |Parameter Size, 175B|, |Dataset, Spider dev|, |Difficulty Level, All|}, Execution Match , 0.570|
|{|Model Type, General LLM|, |Model Name, MPT-7B-instruct|, |Parameter Size, 7B|, |Dataset, Spider dev|, |Difficulty Level, 1|}, Execution Match , 0.262|
|{|Model Type, General LLM|, |Model Name, MPT-7B-instruct|, |Parameter Size, 7B|, |Dataset, Spider dev|, |Difficulty Level, 2|}, Execution Match , 0.381|
|{|Model Type, General LLM|, |Model Name, MPT-7B-instruct|, |Parameter Size, 7B|, |Dataset, Spider dev|, |Difficulty Level, 3|}, Execution Match , 0.117|
|{|Model Type, General LLM|, |Model Name, MPT-7B-instruct|, |Parameter Size, 7B|, |Dataset, Spider dev|, |Difficulty Level, 4|}, Execution Match , 0.091|
|{|Model Type, General LLM|, |Model Name, MPT-7B-instruct|, |Parameter Size, 7B|, |Dataset, Spider dev|, |Difficulty Level, All|}, Execution Match , 0.205|
|{|Model Type, General LLM|, |Model Name, ALPACA|, |Parameter Size, 7B|, |Dataset, Spider dev|, |Difficulty Level, 1|}, Execution Match , 0.311|
|{|Model Type, General LLM|, |Model Name, ALPACA|, |Parameter Size, 7B|, |Dataset, Spider dev|, |Difficulty Level, 2|}, Execution Match , 0.460|
|{|Model Type, General LLM|, |Model Name, ALPACA|, |Parameter Size, 7B|, |Dataset, Spider dev|, |Difficulty Level, 3|}, Execution Match , 0.192|
|{|Model Type, General LLM|, |Model Name, ALPACA|, |Parameter Size, 7B|, |Dataset, Spider dev|, |Difficulty Level, 4|}, Execution Match , 0.083|
|{|Model Type, General LLM|, |Model Name, ALPACA|, |Parameter Size, 7B|, |Dataset, Spider dev|, |Difficulty Level, All|}, Execution Match , 0.242|
|{|Model Type, General LLM|, |Model Name, KOALA|, |Parameter Size, 7B|, |Dataset, Spider dev|, |Difficulty Level, 1|}, Execution Match , 0.195|
|{|Model Type, General LLM|, |Model Name, KOALA|, |Parameter Size, 7B|, |Dataset, Spider dev|, |Difficulty Level, 2|}, Execution Match , 0.218|
|{|Model Type, General LLM|, |Model Name, KOALA|, |Parameter Size, 7B|, |Dataset, Spider dev|, |Difficulty Level, 3|}, Execution Match , 0.017|
|{|Model Type, General LLM|, |Model Name, KOALA|, |Parameter Size, 7B|, |Dataset, Spider dev|, |Difficulty Level, 4|}, Execution Match , 0.071|
|{|Model Type, General LLM|, |Model Name, KOALA|, |Parameter Size, 7B|, |Dataset, Spider dev|, |Difficulty Level, All|}, Execution Match , 0.131|
|{|Model Type, General LLM|, |Model Name, OpenAssistant-pythia|, |Parameter Size, 12B|, |Dataset, Spider dev|, |Difficulty Level, 1|}, Execution Match , 0.202|
|{|Model Type, General LLM|, |Model Name, OpenAssistant-pythia|, |Parameter Size, 12B|, |Dataset, Spider dev|, |Difficulty Level, 2|}, Execution Match , 0.322|
|{|Model Type, General LLM|, |Model Name, OpenAssistant-pythia|, |Parameter Size, 12B|, |Dataset, Spider dev|, |Difficulty Level, 3|}, Execution Match , 0.025|
|{|Model Type, General LLM|, |Model Name, OpenAssistant-pythia|, |Parameter Size, 12B|, |Dataset, Spider dev|, |Difficulty Level, 4|}, Execution Match , 0.069|
|{|Model Type, General LLM|, |Model Name, OpenAssistant-pythia|, |Parameter Size, 12B|, |Dataset, Spider dev|, |Difficulty Level, All|}, Execution Match , 0.157|
|{|Model Type, General LLM|, |Model Name, ORCA-mini|, |Parameter Size, 7B|, |Dataset, Spider dev|, |Difficulty Level, 1|}, Execution Match , 0.243|
|{|Model Type, General LLM|, |Model Name, ORCA-mini|, |Parameter Size, 7B|, |Dataset, Spider dev|, |Difficulty Level, 2|}, Execution Match , 0.280|
|{|Model Type, General LLM|, |Model Name, ORCA-mini|, |Parameter Size, 7B|, |Dataset, Spider dev|, |Difficulty Level, 3|}, Execution Match , 0.101|
|{|Model Type, General LLM|, |Model Name, ORCA-mini|, |Parameter Size, 7B|, |Dataset, Spider dev|, |Difficulty Level, 4|}, Execution Match , 0.076|
|{|Model Type, General LLM|, |Model Name, ORCA-mini|, |Parameter Size, 7B|, |Dataset, Spider dev|, |Difficulty Level, All|}, Execution Match , 0.169|
|{|Model Type, General LLM|, |Model Name, LLaMA-2|, |Parameter Size, 7B|, |Dataset, Spider dev|, |Difficulty Level, 1|}, Execution Match , 0.225|
|{|Model Type, General LLM|, |Model Name, LLaMA-2|, |Parameter Size, 7B|, |Dataset, Spider dev|, |Difficulty Level, 2|}, Execution Match , 0.393|
|{|Model Type, General LLM|, |Model Name, LLaMA-2|, |Parameter Size, 7B|, |Dataset, Spider dev|, |Difficulty Level, 3|}, Execution Match , 0.101|
|{|Model Type, General LLM|, |Model Name, LLaMA-2|, |Parameter Size, 7B|, |Dataset, Spider dev|, |Difficulty Level, 4|}, Execution Match , 0.081|
|{|Model Type, General LLM|, |Model Name, LLaMA-2|, |Parameter Size, 7B|, |Dataset, Spider dev|, |Difficulty Level, All|}, Execution Match , 0.192|
|{|Model Type, Code Specific LLM|, |Model Name, CodeGen2|, |Parameter Size, 7B|, |Dataset, Spider dev|, |Difficulty Level, 1|}, Execution Match , 0.375|
|{|Model Type, Code Specific LLM|, |Model Name, CodeGen2|, |Parameter Size, 7B|, |Dataset, Spider dev|, |Difficulty Level, 2|}, Execution Match , 0.498|
|{|Model Type, Code Specific LLM|, |Model Name, CodeGen2|, |Parameter Size, 7B|, |Dataset, Spider dev|, |Difficulty Level, 3|}, Execution Match , 0.167|
|{|Model Type, Code Specific LLM|, |Model Name, CodeGen2|, |Parameter Size, 7B|, |Dataset, Spider dev|, |Difficulty Level, 4|}, Execution Match , 0.066|
|{|Model Type, Code Specific LLM|, |Model Name, CodeGen2|, |Parameter Size, 7B|, |Dataset, Spider dev|, |Difficulty Level, All|}, Execution Match , 0.257|
|{|Model Type, Code Specific LLM|, |Model Name, Starcoder|, |Parameter Size, 15.5B|, |Dataset, Spider dev|, |Difficulty Level, 1|}, Execution Match , 0.584|
|{|Model Type, Code Specific LLM|, |Model Name, Starcoder|, |Parameter Size, 15.5B|, |Dataset, Spider dev|, |Difficulty Level, 2|}, Execution Match , 0.628|
|{|Model Type, Code Specific LLM|, |Model Name, Starcoder|, |Parameter Size, 15.5B|, |Dataset, Spider dev|, |Difficulty Level, 3|}, Execution Match , 0.275|
|{|Model Type, Code Specific LLM|, |Model Name, Starcoder|, |Parameter Size, 15.5B|, |Dataset, Spider dev|, |Difficulty Level, 4|}, Execution Match , 0.208|
|{|Model Type, Code Specific LLM|, |Model Name, Starcoder|, |Parameter Size, 15.5B|, |Dataset, Spider dev|, |Difficulty Level, All|}, Execution Match , 0.410|
|{|Model Type, Code Specific LLM|, |Model Name, Vicuna|, |Parameter Size, 7B|, |Dataset, Spider dev|, |Difficulty Level, 1|}, Execution Match , 0.060|
|{|Model Type, Code Specific LLM|, |Model Name, Vicuna|, |Parameter Size, 7B|, |Dataset, Spider dev|, |Difficulty Level, 2|}, Execution Match , 0.134|
|{|Model Type, Code Specific LLM|, |Model Name, Vicuna|, |Parameter Size, 7B|, |Dataset, Spider dev|, |Difficulty Level, 3|}, Execution Match , 0.008|
|{|Model Type, Code Specific LLM|, |Model Name, Vicuna|, |Parameter Size, 7B|, |Dataset, Spider dev|, |Difficulty Level, 4|}, Execution Match , 0.042|
|{|Model Type, Code Specific LLM|, |Model Name, Vicuna|, |Parameter Size, 7B|, |Dataset, Spider dev|, |Difficulty Level, All|}, Execution Match , 0.064|
|{|Model Type, Code Specific LLM|, |Model Name, nsql|, |Parameter Size, 6B|, |Dataset, Spider dev|, |Difficulty Level, 1|}, Execution Match , 0.772|
|{|Model Type, Code Specific LLM|, |Model Name, nsql|, |Parameter Size, 6B|, |Dataset, Spider dev|, |Difficulty Level, 2|}, Execution Match , 0.732|
|{|Model Type, Code Specific LLM|, |Model Name, nsql|, |Parameter Size, 6B|, |Dataset, Spider dev|, |Difficulty Level, 3|}, Execution Match , 0.608|
|{|Model Type, Code Specific LLM|, |Model Name, nsql|, |Parameter Size, 6B|, |Dataset, Spider dev|, |Difficulty Level, 4|}, Execution Match , 0.277|
|{|Model Type, Code Specific LLM|, |Model Name, nsql|, |Parameter Size, 6B|, |Dataset, Spider dev|, |Difficulty Level, All|}, Execution Match , 0.548|
|{|Model Type, Seq-to-Seq Model|, |Model Name, T5(tscholak/cxmefzzi)|, |Parameter Size, 3B|, |Dataset, Spider dev|, |Difficulty Level, 1|}, Execution Match , 0.828|       
|{|Model Type, Seq-to-Seq Model|, |Model Name, T5(tscholak/cxmefzzi)|, |Parameter Size, 3B|, |Dataset, Spider dev|, |Difficulty Level, 2|}, Execution Match , 0.782|       
|{|Model Type, Seq-to-Seq Model|, |Model Name, T5(tscholak/cxmefzzi)|, |Parameter Size, 3B|, |Dataset, Spider dev|, |Difficulty Level, 3|}, Execution Match , 0.650|       
|{|Model Type, Seq-to-Seq Model|, |Model Name, T5(tscholak/cxmefzzi)|, |Parameter Size, 3B|, |Dataset, Spider dev|, |Difficulty Level, 4|}, Execution Match , 0.434|       
|{|Model Type, Seq-to-Seq Model|, |Model Name, T5(tscholak/cxmefzzi)|, |Parameter Size, 3B|, |Dataset, Spider dev|, |Difficulty Level, All|}, Execution Match , 0.641|     
|{|Model Type, Seq-to-Seq Model|, |Model Name, PICARD+T5|, |Parameter Size, 3B|, |Dataset, Spider dev|, |Difficulty Level, 1|}, Execution Match , 0.790|
|{|Model Type, Seq-to-Seq Model|, |Model Name, PICARD+T5|, |Parameter Size, 3B|, |Dataset, Spider dev|, |Difficulty Level, 2|}, Execution Match , 0.799|
|{|Model Type, Seq-to-Seq Model|, |Model Name, PICARD+T5|, |Parameter Size, 3B|, |Dataset, Spider dev|, |Difficulty Level, 3|}, Execution Match , 0.558|
|{|Model Type, Seq-to-Seq Model|, |Model Name, PICARD+T5|, |Parameter Size, 3B|, |Dataset, Spider dev|, |Difficulty Level, 4|}, Execution Match , 0.502|
|{|Model Type, Seq-to-Seq Model|, |Model Name, PICARD+T5|, |Parameter Size, 3B|, |Dataset, Spider dev|, |Difficulty Level, All|}, Execution Match , 0.652|
|{|Model Type, Seq-to-Seq Model|, |Model Name, RESDSQL|, |Parameter Size, 3B|, |Dataset, Spider dev|, |Difficulty Level, 1|}, Execution Match , 0.872|
|{|Model Type, Seq-to-Seq Model|, |Model Name, RESDSQL|, |Parameter Size, 3B|, |Dataset, Spider dev|, |Difficulty Level, 2|}, Execution Match , 0.857|
|{|Model Type, Seq-to-Seq Model|, |Model Name, RESDSQL|, |Parameter Size, 3B|, |Dataset, Spider dev|, |Difficulty Level, 3|}, Execution Match , 0.666|
|{|Model Type, Seq-to-Seq Model|, |Model Name, RESDSQL|, |Parameter Size, 3B|, |Dataset, Spider dev|, |Difficulty Level, 4|}, Execution Match , 0.696|
|{|Model Type, Seq-to-Seq Model|, |Model Name, RESDSQL|, |Parameter Size, 3B|, |Dataset, Spider dev|, |Difficulty Level, All|}, Execution Match , 0.775|
"""   
)

example3 = ExtractionExample(
    table="""
    -----------------  ---------------------  --------------  -------  -------  -------  -------  -----
    Model Type         Model Name             Parameter Size  Level 1  Level 2  Level 3  Level 4  All
    General LLM        ChatGPT-3.5-turbo      175B            0.760    0.799    0.408    0.493    0.623
    -----------------  ---------------------  --------------  -------  -------  -------  -------  -----
    """,
    
    caption="Table 1. Benchmark Results of Execution Match of all Models we tested on the 'dev' SPIDER dataset",
    
    references=["""
                In our experimentation, we organized the models into three distinct groups as illustrated in Table 1: general purpose LLMs, Code-Specific LLMs, and Sequence-to-Sequence models. Table 1 further presents the Execution Match score on the SPIDER dataset for each studied LLM and for each of the four difficulty levels.
                """],
    result="""
    |{|Model Type, General LLM|, |Model Name, ChatGPT-3.5-turbo|, |Parameter Size, 175B|, |Dataset, Spider dev|, |Difficulty Level, 1|}, Execution Match , 0.760|
|{|Model Type, General LLM|, |Model Name, ChatGPT-3.5-turbo|, |Parameter Size, 175B|, |Dataset, Spider dev|, |Difficulty Level, 2|}, Execution Match , 0.799|
|{|Model Type, General LLM|, |Model Name, ChatGPT-3.5-turbo|, |Parameter Size, 175B|, |Dataset, Spider dev|, |Difficulty Level, 3|}, Execution Match , 0.408|
|{|Model Type, General LLM|, |Model Name, ChatGPT-3.5-turbo|, |Parameter Size, 175B|, |Dataset, Spider dev|, |Difficulty Level, 4|}, Execution Match , 0.493|
|{|Model Type, General LLM|, |Model Name, ChatGPT-3.5-turbo|, |Parameter Size, 175B|, |Dataset, Spider dev|, |Difficulty Level, All|}, Execution Match , 0.623|
"""   
)

example_data_table = ExtractionExample(
    table="""+-------------------------+--------------+-------------------+--------------+
|     Hyperparameter      |    Value     |  Hyperparameter   |    Value     |
|      Learning Rate      | 1    e  -  4 |      Epochs       |      5       |
    """,
    caption="Table 3: Hyperparameter Settings",
    
    references=[""],
    result="""
    |{|Hyperparameter, Learning Rate|, |Value, 1e-4|}|
    |{|Hyperparameter, Epochs|, |Value, 5|}|
"""  
)