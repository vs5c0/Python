from Question import Question

question_prompts = [
    "What color are apples? \n(a)Red \n (b)Green \n (c)Both \n (d)None\n\n",
    "What color are Mangoes? \n(a)Blue \n (b)White \n (c)Yellow \n (d)Orange\n\n",
    "What colors are there in India Flag? \n(a)Saffron \n (b)Green \n (c)White \n (d)All\n\n",
    "What color are Pulihora after done the preparation? \n(a)Red \n (b)Green \n (c)Both \n (d)Brown\n\n",
    "Who is PM of Italy? \n(a)Melodi \n (b)Meloni \n (c)Modi \n (d)Kim\n\n",
]

questions = [
    Question(question_prompts[0], "c"),
    Question(question_prompts[1], "c"),
    Question(question_prompts[2], "d"),
    Question(question_prompts[3], "d"),
    Question(question_prompts[4], "b"),

]

def runtest(questions):
    score = 0
    for quest in questions:
        answer = input(quest.prompt)
        if answer == quest.answer:
            score += 1
    print("You got " + str(score) + "/" + str(len(questions)) +"correct")

    runtest(questions)