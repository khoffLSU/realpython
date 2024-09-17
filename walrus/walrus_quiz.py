'''Quis example taken from real python walrus tutorial and modified.'''

import random
import string

QUESTIONS = {
    "What is the formal name of PEP 572?": [
        "Assignment Expressions",
        "Named Expressions",
        "The Walrus Operator",
        "The Colon Equals Operator",
    ],
    "Which one of these is an invalid use of the walrus operator?": [
        "[y**2 for x in range(10) if y := f(x) > 0]",
        "print(y := f(x))",
        "(y := f(x))",
        "any((y := f(x)) for x in range(10))",
    ],
    "What's the purpose of the built-in zip() function": [
        "To iterate over two or more sequences at the same time",
        "To combine several strings into one",
        "To compress several files into one archive",
        "To get information from the user",
    ],
    "What's the name of Python's sorting algorithm": [
        "Timsort", "Quicksort", "Merge sort", "Bubble sort"
    ],
    "What does dict.get(key) return if key isn't found in dict": [
        "None", "key", "True", "False",
    ]
}

num_correct = 0
for question, answers in QUESTIONS.items():
    correct = answers[0]
    random.shuffle(answers)

    coded_answers = dict(zip(string.ascii_lowercase, answers))
    valid_answers = sorted(coded_answers.keys())

    for code, answer in coded_answers.items():
        print(f"  {code}) {answer}")

    while (user_answer := input(f"\n{question} ")) not in valid_answers:
        print(f"Please answer one of {', '.join(valid_answers)}")

    if coded_answers[user_answer] == correct:
        print(f"⭐ Correct! ⭐, the answer is {user_answer!r}\n")
        num_correct += 1
    else:
        print(f"No, the answer is {correct!r}\n")

print(f"You got {num_correct} correct out of {len(QUESTIONS)} questions")