def load_to_list(filepath: str) -> list[float]:
    # I'm gonna read each line from the file and turn it into a float
    temps = []  # list to store temperature floats
    with open(filepath, 'r') as f:
        for line in f:
            line = line.strip()  # ditch extra spaces and newline chars
            if line:
                # make sure line isn't empty before conversion
                temps.append(float(line))  # convert text to float and save
    return temps  # hand back the list of temperatures

def descriptive_statistics(source_data: list[float]) -> None:
    # Let's figure out some basic stats from the list
    total = len(source_data)           # how many readings we got
    average = sum(source_data) / total # mean temp
    low = min(source_data)             # coldest reading
    high = max(source_data)            # hottest reading

    # Print out results in the exact format required
    print(f"There are {total} values in the data source.")
    print(f"The average value is {average:.2f}")
    print(f"The highest value is {high} and the smallest value is {low}.")

def apply_markup(filepath: str) -> None:
    # read whole file into a single string
    text = ""
    with open(filepath, 'r') as f:
        for line in f:
            text += line.strip() + " "
    # split into sentences on “. ” so we print one sentence per line
    parts = text.strip().split(". ")
    for i, part in enumerate(parts):
        if not part:
            continue
        sent = part + "." if i < len(parts) - 1 else part
        words = sent.split()
        out = []
        for word in words:
            if word.startswith('.') and len(word) > 1:
                out.append(word[1:].upper())
            elif word.startswith('_') and len(word) > 1:
                out.append(" ".join(word[1:]))
            else:
                out.append(word)
        print(" ".join(out))




#--------------------------------------------------------------------------------#
# ⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎  WRITE YOUR CODE ABOVE THIS  LINE ⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎

# ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓  DO NOT MODIFY THE CODE BELOW THIS LINE ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓
#--------------------------------------------------------------------------------#
# 
import unittest
import io
import sys
import os

class TestWeek06(unittest.TestCase):
    def test_load_to_list_matches_manual_read(self):
        manual = []
        with open('data/temperatures.txt', 'r') as f:
            for line in f:
                line = line.strip()
                if line:
                    manual.append(float(line))
        result = load_to_list('data/temperatures.txt')
        self.assertEqual(manual, result)

    def test_descriptive_statistics_simple(self):
        data = [1.0, 2.0, 3.0]
        expected = (
            "There are 3 values in the data source.\n"
            "The average value is 2.00\n"
            "The highest value is 3.0 and the smallest value is 1.0.\n"
        )
        buf = io.StringIO()
        old_stdout = sys.stdout
        try:
            sys.stdout = buf
            descriptive_statistics(data)
        finally:
            sys.stdout = old_stdout
        self.assertEqual(buf.getvalue(), expected)

    def test_descriptive_statistics_actual_file(self):
        temps = load_to_list('data/temperatures.txt')
        buf = io.StringIO()
        old_stdout = sys.stdout
        try:
            sys.stdout = buf
            descriptive_statistics(temps)
        finally:
            sys.stdout = old_stdout
        expected = (
            "There are 19 values in the data source.\n"
            "The average value is 70.26\n"
            "The highest value is 81.0 and the smallest value is 5.0.\n"
        )
        self.assertEqual(buf.getvalue(), expected)

    def test_apply_markup_inline_example(self):
        sample = "Not _all those .who wander are lost\n"
        tmp = 'temp_markup.txt'
        with open(tmp, 'w') as f:
            f.write(sample)
        buf = io.StringIO()
        old_stdout = sys.stdout
        try:
            sys.stdout = buf
            apply_markup(tmp)
        finally:
            sys.stdout = old_stdout
        os.remove(tmp)
        self.assertEqual(buf.getvalue(), "Not a l l those WHO wander are lost\n")

    def test_apply_markup_actual_file(self):
        buf = io.StringIO()
        old_stdout = sys.stdout
        try:
            sys.stdout = buf
            apply_markup('data/markup.txt')
        finally:
            sys.stdout = old_stdout
        expected = (
            "Markup is a technique where FORMAT INSTRUCTIONS are inserted as part of a text file.\n"
            "In this file, a word preceded by a DOT should be printed in upper case.\n"
            "And a word preceded by an UNDERSCORE should be typed in expanded form, with spaces between its letters.\n"
            "Such formatting brings attention to KEY elements of a text, through c l a r i t y and f o c u s\n"
        )
        self.assertEqual(buf.getvalue(), expected)

if __name__ == '__main__':
    unittest.main()



