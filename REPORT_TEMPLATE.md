# Project Report: Sequence-Based Viral Strain Classifier (Basic)

## 1. Title
Sequence-Based Viral Strain Classifier (Basic)

## 2. Abstract
Write a short summary of the problem, the application, the methods used and the main outcome after testing. Do not claim clinical identification.

## 3. Introduction
Explain why computational sequence comparison is useful in bioinformatics and introduce the educational goal of comparing a query DNA sequence with reference sequences.

## 4. Aim and Objectives
- Build a basic sequence-analysis web application.
- Validate DNA sequence input.
- Calculate sequence length and GC content.
- Read reference sequences from FASTA.
- Compare sequences using Biopython pairwise alignment.
- Display and export comparison results.

## 5. Syllabus Mapping
Map the implementation to BT 2113: strings/lists, loops/functions, dictionaries, file I/O, FASTA parsing, Biopython Seq/SeqIO, pairwise alignment and Pandas.

## 6. Tools and Technologies
Python, Biopython, Streamlit, Pandas, FASTA, GitHub and Streamlit Community Cloud.

## 7. Methodology / Workflow
Describe input -> cleaning and validation -> FASTA parsing -> pairwise alignment -> identity calculation -> ranking -> results display.

## 8. Implementation
Explain `app.py`, `classifier.py`, the reference FASTA file and test file. Include selected code snippets and explain them in your own words.

## 9. Results
Insert screenshots from the running app and a table of actual test outputs. State which reference dataset was used. The bundled sequences are fictional demonstration data.

## 10. Testing
Record tests for valid DNA, invalid characters, FASTA upload, identical sequences, and comparison ranking. Include actual pass/fail results.

## 11. Limitations
The reference dataset is tiny and fictional; percent identity is a simple educational metric; closest match does not establish a real viral strain or clinical diagnosis.

## 12. Conclusion and Future Scope
Summarize what was achieved. Possible extensions include curated NCBI reference sequences with accession numbers, more robust alignment settings, larger datasets and improved reporting.

## 13. References
- BT 2113 Python & Biopython course syllabus.
- Biopython Tutorial and Cookbook: https://biopython.org/wiki/Documentation
- Streamlit documentation: https://docs.streamlit.io/
