'''Biology Quiz Game'''

import time
score = 0
border = "____________________________________________________________________________"
print("Welcome to my biology quiz game!!")
print()
print("This is a mutiple choice quiz.")
print("When prompted, please input just the lowercase letter of your answer.")
print()
print("You will be given two chances for every question.")
print("If you get it correct on the first try, you get 10 points.")
print("If you get it correct on the second try, you get 5 points.")
print("If you don't get it correct, you will be told the answer but won't be awarded any points.")
print()
print("Now let's begin!")
print()
time.sleep(8)
def quiz_game (cor_ans):
    global score
    answer = input("Enter your answer: ")
    answer = answer.lower()
    cor_ans = cor_ans.lower()
    if answer == cor_ans:
        time.sleep(1)
        print("Well done, you got it correct!")
        score += 10
        print("Your new score is",score,".")
    else:
        time.sleep(1)
        print("Sorry, that's incorrect.")
        print("Please try again.")
        answer = input("Enter your answer: ")
        answer = answer.lower()
        if answer == cor_ans:
              time.sleep(1)
              print("Second time's a charm!")
              print("Good job.")
              score += 5
              print("Your new score is",score,".")
        else:
            time.sleep(1)
            print("Oops, wrong again.")
            print("The correct answer is",cor_ans,".")
            print("Your score is still",score,".")
        
print("1. What is adenine paired with in DNA?")
print("a. guanine                    b. thynine")
print("c. cytocine                   d. uracil")
quiz_game("b")

print(border)
print(border)

time.sleep(1)
print("2. What is adenine paired with in RNA?")
print("a. guanine                    b. thynine")
print("c. cytocine                   d. uracil")
quiz_game("d")

print(border)
print(border)

time.sleep(1)
print("3. What cell organelle makes up part of the cell membrane?")
print("a. ribosome                  b. cell wall")
print("c. endoplasmic reticulum     d. vacuole")
quiz_game("c")

print(border)
print(border)

time.sleep(1)
print("4. Which part of blood helps clot the blood at wounds?")
print("a. red blood cells           b. white blood cells")
print("c. plasma                    d. platelets")
quiz_game("d")

print(border)
print(border)

time.sleep(1)
print("5. What kingdom is seaweed a part of?")
print("a. protista                 b. plantea")
print("c. animalia                 d. archea")
quiz_game("a")

print(border)
print(border)

time.sleep(1)
print("6. What is the name of the organism that quickly reproduces if its population falls below carrying capacity?")
print("a. capacitor                b. oppurtunist")
print("c. competitor               d. reproducer")
quiz_game("b")

print(border)
print(border)

time.sleep(1)
print("7. What is the scientific name of the period of time that a fetus is growing inside one of its parents?")
print("a. germination              b. gestation")
print("c. pregnancy                d. growth period")
quiz_game("b")

print(border)
print(border)

time.sleep(1)
print("8. What is the first stage of a virus infecting a cell called?")
print("a. invasion                 b. injection")
print("c. infection                d. attatchment")
quiz_game("d")

print(border)
print(border)

time.sleep(1)
print("9. Which scientist came up with the theory that giraffes grew long necks by reaching their heads up to grab leaves?")
print("a. Pastuer                 b. Einstein")
print("c. Darwin                  d. Mendel")
quiz_game("c")

print(border)
print(border)

time.sleep(1)
print("10. What is the name of the square that takes parent's genes and shows the possible outcomes of their children's genes?")
print("a. Gene Square              b. Punnet Square")
print("c. Outcome Square           d. Trait Square")
quiz_game("b")

print(border)
print(border)

time.sleep(1)
print("11. What is the name for a trait that can be seen?")
print("a. genotype                b. phenotype")
print("c. noticeable trait        d. physical trait")
quiz_game("b")

print(border)
print(border)

time.sleep(1)
print("12. What is the name of the plankton that makes its food via photosynthesis?")
print("a. plantea plankton              b. chloroplast plankton")
print("c. phytoplankton                 d. photoplankton")
quiz_game("c")

print(border)
print(border)

time.sleep(1)
print("You finished my quiz game!")
print("Now, to calculate your end score...")
time.sleep(2)
if score == 120:
    print("Great job! You got all the questions correct!")
    print("Your final score is",score,".")
elif score > 80 and score < 120:
    print("Not too shabby.")
    print("You got most of the question correct; your final score is",score,".")
elif score < 80:
    print("Wow. That was disappointing.")
    print("You only got",score," points... better luck next time.")