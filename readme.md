# Program to generate left and right justified text
This program takes a paragraph string and a page width as input parameters and returns an array of left and right-justified strings. The program splits the paragraph into a list of words and then groups these words into lines such that each line does not exceed the page width. It then left and right-justifies each line, adding appropriate padding to fill the remaining space up to the page width.

## Usage
To use the program, simply call the justify_paragraph() function in the text_justification.py file, passing in the paragraph string and page width as arguments. The function returns an array of left and right-justified strings.

![main.py](/assets/main.png)

## Running Unit Tests
The unit tests for the program are located in the test_text_justification.py file. To run the tests, simply run the following command in the terminal:

![test_text_justification.py](/assets/test.png)

The tests check that the lines are correctly split and justified, and that the program handles edge cases such as paragraphs that are shorter than the page width or that contain long words that cannot be split across lines.