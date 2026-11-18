from pathlib import Path
from io import StringIO
from Bio import SeqIO
from Bio.Seq import Seq
from Bio import pairwise2


VALID_DNA = set("ATGC")


def clean_and_validate_sequence(sequence: str) -> str:
    """Normalize a DNA sequence and reject characters other than A, T, G and C."""
    cleaned = "".join(sequence.split()).upper()
    if not cleaned:
        raise ValueError("Please enter a DNA sequence.")
    invalid = sorted(set(cleaned) - VALID_DNA)
    if invalid:
        raise ValueError(
            "Invalid DNA sequence. Only A, T, G and C are accepted. "
            f"Unexpected character(s): {', '.join(invalid)}"
        )
    return cleaned


def gc_content(sequence: str) -> float:
    """Return GC percentage for a validated DNA sequence."""
    if not sequence:
        return 0.0
    return ((sequence.count("G") + sequence.count("C")) / len(sequence)) * 100


def load_reference_fasta(path):
    """Read reference records from a FASTA file using Biopython SeqIO."""
    records = {}
    for record in SeqIO.parse(str(path), "fasta"):
        seq = clean_and_validate_sequence(str(record.seq))
        records[record.id] = seq
    if not records:
        raise ValueError("The reference FASTA file contains no records.")
    return records


def parse_uploaded_fasta(file_bytes):
    """Parse uploaded FASTA bytes and return Biopython SeqRecord objects."""
    text = file_bytes.decode("utf-8")
    records = list(SeqIO.parse(StringIO(text), "fasta"))
    if not records:
        raise ValueError("No FASTA records were found.")
    for record in records:
        clean_and_validate_sequence(str(record.seq))
    return records


def sequence_identity(query: str, reference: str) -> float:
    """
    Calculate percent identity from a global pairwise alignment.
    Uses Biopython pairwise2 globalxx; matches score 1, mismatches/gaps score 0.
    """
    alignments = pairwise2.align.globalxx(
        query, reference, one_alignment_only=True
    )
    if not alignments:
        return 0.0

    alignment = alignments[0]
    aligned_query = alignment.seqA
    aligned_reference = alignment.seqB

    comparable_columns = 0
    identical_columns = 0
    for q_base, r_base in zip(aligned_query, aligned_reference):
        if q_base != "-" and r_base != "-":
            comparable_columns += 1
            if q_base == r_base:
                identical_columns += 1

    if comparable_columns == 0:
        return 0.0
    return (identical_columns / comparable_columns) * 100


def analyze_sequence(query: str, references: dict) -> dict:
    """Analyze one query and compare it with every reference sequence."""
    query = clean_and_validate_sequence(query)
    if not references:
        raise ValueError("No reference sequences are available.")

    # Biopython Seq object is used to represent the biological sequence.
    query_seq = Seq(query)
    comparisons = []

    for name, reference in references.items():
        reference = clean_and_validate_sequence(reference)
        identity = sequence_identity(str(query_seq), reference)
        comparisons.append({
            "Reference": name,
            "Similarity (%)": identity,
            "Reference length (bp)": len(reference),
        })

    comparisons.sort(key=lambda row: row["Similarity (%)"], reverse=True)
    best = comparisons[0]

    return {
        "sequence": query,
        "length": len(query),
        "gc_content": gc_content(query),
        "best_match": best["Reference"],
        "best_similarity": best["Similarity (%)"],
        "comparisons": comparisons,
    }
