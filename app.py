import io
import pandas as pd
import streamlit as st
from Bio import SeqIO
from Bio.Seq import Seq
from Bio import pairwise2

from classifier import analyze_sequence, load_reference_fasta, parse_uploaded_fasta

st.set_page_config(page_title="Viral Strain Classifier", page_icon="🧬", layout="wide")

st.title("🧬 Sequence-Based Viral Strain Classifier")
st.caption("A basic educational bioinformatics application using Python and Biopython.")

with st.sidebar:
    st.header("About this project")
    st.write(
        "This app validates a DNA sequence, calculates basic sequence statistics, "
        "and compares it with a small reference FASTA database using pairwise alignment."
    )
    st.warning(
        "Educational demonstration only. It does not diagnose infection or establish "
        "a clinically valid viral strain."
    )

st.subheader("1. Provide a DNA sequence")
input_mode = st.radio("Input method", ["Paste sequence", "Upload FASTA file"], horizontal=True)

query = ""
query_name = "User sequence"

if input_mode == "Paste sequence":
    query_name = st.text_input("Sequence name", value="User sequence")
    query = st.text_area(
        "DNA sequence",
        placeholder="Example: ATGCGTACGTTAGCTA",
        height=140,
    )
else:
    uploaded = st.file_uploader("Upload a FASTA file", type=["fa", "fasta", "fna", "txt"])
    if uploaded is not None:
        try:
            records = list(parse_uploaded_fasta(uploaded.getvalue()))
            if len(records) != 1:
                st.error("Please upload a FASTA file containing exactly one query sequence.")
            else:
                query_name = records[0].id
                query = str(records[0].seq)
                st.success(f"Loaded FASTA record: {query_name}")
        except Exception as exc:
            st.error(f"Could not read FASTA file: {exc}")

st.subheader("2. Reference database")
reference_path = Path(__file__).parent / "reference_sequences.fasta"
try:
    references = load_reference_fasta(reference_path)
    st.info(f"{len(references)} reference sequences loaded from the bundled FASTA file.")
except Exception as exc:
    st.error(f"Reference database error: {exc}")
    references = {}

if st.button("Analyze sequence", type="primary", disabled=not query.strip() or not references):
    try:
        result = analyze_sequence(query, references)
        st.success("Sequence analysis completed.")

        left, middle, right = st.columns(3)
        left.metric("Sequence length", f"{result['length']} bp")
        middle.metric("GC content", f"{result['gc_content']:.2f}%")
        right.metric("Closest reference", result["best_match"])

        st.subheader("3. Pairwise comparison results")
        table = pd.DataFrame(result["comparisons"])
        table["Similarity (%)"] = table["Similarity (%)"].map(lambda x: round(x, 2))
        st.dataframe(table, use_container_width=True, hide_index=True)

        st.bar_chart(table.set_index("Reference")["Similarity (%)"])

        st.subheader("4. Interpretation")
        st.write(
            f"The closest sequence in this demonstration database is **{result['best_match']}**, "
            f"with **{result['best_similarity']:.2f}%** identity across the aligned positions."
        )
        st.download_button(
            "Download results as CSV",
            data=table.to_csv(index=False).encode("utf-8"),
            file_name="viral_strain_comparison.csv",
            mime="text/csv",
        )
        st.caption(
            "Similarity is a simple alignment identity measure. A closest match in this small "
            "teaching dataset is not proof of viral identity or clinical strain classification."
        )
    except ValueError as exc:
        st.error(str(exc))
    except Exception as exc:
        st.error(f"Analysis failed: {exc}")

st.divider()
st.caption("BT 2113 – Python & Biopython | Student mini-project")
