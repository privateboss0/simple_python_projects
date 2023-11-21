from questions_multiple_choice import Question

question_prompt = [
    "Which is a name of a Canadian City?\n(a) New York\n(b) Toronto\n(c) London\n(d) Paris\n\n",
    "What is the BMO's bank code as the first canadian bank?\n(a) 001\n(b) 002\n(c) 003\n(d) 004\n\n",
    "Which county is not in Europe?\n(a) Japan\n(b) Italy\n(c) Germany\n(d) Poland\n"
]

questions = [
    Question(question_prompt[0], "b"),
    Question(question_prompt[1], "a"),
    Question(question_prompt[2], "a")
]

def run_quiz(question):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print("You got " + str(score) + "/" +str(len(questions)) + " correct")

run_quiz(questions)