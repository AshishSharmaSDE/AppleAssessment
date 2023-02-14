from text_justification import justify_paragraph

paragraph = "This is a sample text but a complicated problem to be solved, so we are adding more text to see that it " \
            "actually works. "
page_width = 20

justified_text = justify_paragraph(paragraph, page_width)

print(justified_text)
