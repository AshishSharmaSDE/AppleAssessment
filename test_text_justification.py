import unittest
from text_justification import justify_paragraph


class TestJustifyParagraph(unittest.TestCase):
    def test_single_word(self):
        paragraph = "Python"
        width = 10
        expected_output = ["Python    "]
        self.assertEqual(justify_paragraph(paragraph, width), expected_output)

    def test_multiple_words(self):
        paragraph = "This is a sample text."
        width = 20
        expected_output = ["This is a sample text."]
        self.assertEqual(justify_paragraph(paragraph, width), expected_output)

    def test_multiple_lines(self):
        paragraph = "This is a sample text but a complicated problem to be solved, so we are adding more text to see " \
                    "that it actually works. "
        width = 30
        expected_output = ["This is   a sample text but a",
                           "complicated problem to be",
                           "solved,  so  we   are",
                           "adding more text to see",
                           "that it actually works. "]
        self.assertEqual(justify_paragraph(paragraph, width), expected_output)

    def test_single_word_width_exceeded(self):
        paragraph = "Python"
        width = 5
        expected_output = ["Python"]
        self.assertEqual(justify_paragraph(paragraph, width), expected_output)


if __name__ == '__main__':
    unittest.main()
