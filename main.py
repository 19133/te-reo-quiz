# Uses method from
# https://www.geeksforgeeks.org/python-shuffle-two-lists-with-same-order/
# to generate random list of questions and answers in same order

import random

questions = ["How many days are there in a year?", "How many days are in a century?", "How many hours are in a day"]
answers = [365, 
           365*100,   # ignoring leap years
           24]

qa_pairs = list(zip(questions, answers))   # list of question/answer pairs
random.shuffle(qa_pairs)                   # list of question/answer pairs in random order

question, answer = qa_pairs.pop()          # Get question & answer from list (pop returns last pair, but we don't care about order)
while True:
    # Ask last question in list
    response = int(input(question))         # User answer

    if response == answer:
        # Next  question and answer
        if qa_pairs:
            question, answer = qa_pairs.pop()
        else:
            break   # Out of questions
    else:
        print('Incorrect, try again')

