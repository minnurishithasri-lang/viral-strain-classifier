# Sequence-Based Viral Strain Classifier (Basic)

A beginner-friendly educational web app built with Python, Streamlit and Biopython for the BT 2113 Python & Biopython course.

## Features
- Paste a DNA sequence or upload one FASTA record.
- Validate DNA input (A, T, G, C).
- Calculate sequence length and GC percentage.
- Parse reference sequences from FASTA using `Bio.SeqIO`.
- Compare the query with each reference using Biopython `pairwise2` global alignment.
- Display percent identity, a comparison chart and downloadable CSV results.

## Important scientific limitation
The bundled reference sequences are **fictional demonstration sequences**, not verified viral genomes. The app only reports the closest match within this small teaching dataset. It is not a clinical diagnostic tool and must not be used to identify infections or make medical decisions. Replace the demonstration FASTA file with properly sourced, documented reference sequences before making biological claims.

## Run locally
1. Install Python 3.10 or newer.
2. Open a terminal in this project folder.
3. Create and activate a virtual environment (recommended).
4. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

5. Start the app:

   ```bash
   streamlit run app.py
   ```

## Deploy using GitHub and Streamlit Community Cloud
1. Create a new **public** GitHub repository.
2. Upload all project files and folders, preserving the structure.
3. Open https://share.streamlit.io/ and sign in with GitHub.
4. Choose **Create app**, select your repository, branch (`main`) and main file (`app.py`).
5. Deploy. Streamlit will install packages from `requirements.txt`.

## Project structure
```text
viral_strain_classifier_project/
├── app.py
├── classifier.py
├── requirements.txt
├── README.md
├── data/
│   └── reference_sequences.fasta
└── tests/
    └── test_classifier.py
```

## Syllabus alignment
- Strings, validation, loops, functions and dictionaries.
- File input/output and FASTA parsing.
- Biopython `Seq` and `SeqIO`.
- Pairwise sequence alignment using `Bio.pairwise2`.
- Pandas table for comparison results.

## Method
The query is normalized and validated, then globally aligned against each reference. Percent identity is calculated as identical non-gap aligned columns divided by all non-gap paired columns, multiplied by 100. The highest identity is reported as the closest match in the supplied reference set.
