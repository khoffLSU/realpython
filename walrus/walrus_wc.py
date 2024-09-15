"""In the next example, you’ll work with a bare-bones implementation of the wc utility 
for counting lines, words, and characters in a text file:"""

import pathlib  # noqa: E402
import sys  # noqa: E402

for filename in sys.argv[1:]:
    path = pathlib.Path(filename)

    counts = (
        (text := path.read_text()).count("\n"),  # Number of lines with walrus assignment embedded
        len(text.split()),  # Number of words
        len(text),  # Number of characters
    )
    print("lines | words | characters: ",*counts, path)

# Run in Command Line: python walrus_wc.py <file path or local name>

# ---------------------------------------------------------------------------------#