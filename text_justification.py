import unittest


def justify_paragraph(paragraph, width):
    # Split the paragraph into words
    words = paragraph.split()

    # Initialize an empty list to store the lines
    lines = []

    # Initialize an empty list to store the words in the current line
    current_line = []

    # Initialize the current line width to zero
    current_width = 0

    # Iterate through the words in the paragraph
    for word in words:
        # Check if adding the current word to the current line would exceed the width
        if current_width + len(word) + len(current_line) <= width:
            # If not, add the word to the current line and update the current width
            current_line.append(word)
            current_width += len(word)
        else:
            # If adding the word would exceed the width, add the current line to the list of lines
            lines.append(current_line)
            # Start a new line with the current word
            current_line = [word]
            # Update the current width
            current_width = len(word)

    # Add the last line to the list of lines
    lines.append(current_line)

    # Initialize an empty list to store the justified lines
    output = []

    # Iterate through the lines
    for line in lines:
        # If the line contains only one word, left-justify it and add it to the output
        if len(line) == 1:
            output.append(line[0].ljust(width))
        else:
            # Otherwise, calculate the number of spaces needed between the words to justify the line
            total_spaces = width - sum(len(word) for word in line)
            num_gaps = len(line) - 1
            spaces_per_gap = total_spaces // num_gaps
            extra_spaces = total_spaces % num_gaps
            # Concatenate the words and spaces to form the justified line
            justified_line = ''
            for i, word in enumerate(line):
                justified_line += word
                if i < num_gaps:
                    justified_line += ' ' * spaces_per_gap
                    if i < extra_spaces:
                        justified_line += ' '
            # Add the justified line to the output
            output.append(justified_line)

    # Return the list of justified lines
    return output

