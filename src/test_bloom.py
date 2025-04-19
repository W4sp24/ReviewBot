import unittest
from src.promts import BloomTaxonomy

class TestBloomTaxonomy(unittest.TestCase):

    def test_remembering(self):
        topic = "Photosynthesis"
        expected_output = ("Using Bloom’s Taxonomy Level 1 (Remembering), generate a set of basic recall-based "
                           "questions or information for the following topic: Photosynthesis")
        self.assertEqual(BloomTaxonomy.remembering(topic), expected_output)

    def test_remembering_empty_topic(self):
        topic = ""
        expected_output = ("Using Bloom’s Taxonomy Level 1 (Remembering), generate a set of basic recall-based "
                           "questions or information for the following topic: ")
        self.assertEqual(BloomTaxonomy.remembering(topic), expected_output)

    def test_remembering_special_characters(self):
        topic = "@#$%^&*()"
        expected_output = ("Using Bloom’s Taxonomy Level 1 (Remembering), generate a set of basic recall-based "
                           "questions or information for the following topic: @#$%^&*()")
        self.assertEqual(BloomTaxonomy.remembering(topic), expected_output)

if __name__ == "__main__":
    unittest.main()