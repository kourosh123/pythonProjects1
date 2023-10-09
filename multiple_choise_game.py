from Question import Question

questions_prompt = [
    "what in  strawberry color?\n(a)blue\n(b)red\n(c)yellow", "\nWhat is banana color?\n(a)yellow\nb(red)\n(blue)",
    "\nwhat is sky color?\n(a)purple\n(b)blue\n(c)red"

]
questions = [
    Question( [0],"b"),
    Question( [1],"a"),
    Question( [2],"b")
]
def run_test(questions):
    score = 0
    for questions in questions_prompt:
        answer = input(questions_prompt)
        if answer == questions.answer:
            score += 1
    print("you got" + str(score) + "/" + str(len(questions)))




