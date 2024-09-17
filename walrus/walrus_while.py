'''Another example of the area where the walrus operator can provide value 
in the construction of a program.  Here a multiple choice question construct
is being configured, but the input must be called twice due to the need to
initiate the validation.'''

question = "Do you use the walrus operator?"
valid_answers = {"yes", "Yes", "y", "Y", "no", "No", "n", "N"}

## original code
# user_answer = input(f"\n{question} ")
# while user_answer not in valid_answers:
#     print(f"Please answer one of {', '.join(valid_answers)}")
#     user_answer = input(f"\n{question} ")

## update refactored code with walrus implementation

while (user_answer := input(f"\n{question} ")) not in valid_answers:
    print(f"Please answer one of {', '.join(valid_answers)}")