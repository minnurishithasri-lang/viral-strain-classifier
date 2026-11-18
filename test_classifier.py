import unittest
from classifier import clean_and_validate_sequence, gc_content, sequence_identity, analyze_sequence


class ClassifierTests(unittest.TestCase):
    def test_clean_sequence(self):
        self.assertEqual(clean_and_validate_sequence(" atg c\n"), "ATGC")

    def test_reject_invalid_sequence(self):
        with self.assertRaises(ValueError):
            clean_and_validate_sequence("ATGX")

    def test_gc_content(self):
        self.assertAlmostEqual(gc_content("ATGC"), 50.0)

    def test_identical_sequences(self):
        self.assertAlmostEqual(sequence_identity("ATGC", "ATGC"), 100.0)

    def test_best_reference(self):
        refs = {"A": "ATGC", "B": "TTTT"}
        result = analyze_sequence("ATGC", refs)
        self.assertEqual(result["best_match"], "A")


if __name__ == "__main__":
    unittest.main()
