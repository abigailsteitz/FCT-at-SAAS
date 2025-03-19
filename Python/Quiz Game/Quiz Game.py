import time
import random

print("hello vro")
time.sleep(1)
print("bienvinidos a mi trivia")
time.sleep(2)

def run_quiz(questions):
    score = 0
    random.shuffle(questions)
    quizstart = True
    
    for question, correct_answer in questions:
        print(question)
        user_answer = input(": ")
        
        
        if user_answer.lower() == correct_answer.lower():
            print("LETS GOOO THAT IS RIGHT\n")
            score += 1
            time.sleep(2)
        else:
            print("NOOOOOOOOOO IT WAS " + correct_answer + " do better\n")
            time.sleep(2)
    
    print("you got " + str(score) + " big people points!!!" )
    if score == 0:
      print("wow, you suck")
      time.sleep(1)
      print("patchwerk fat american 胖胖美国人angered hits on armored men对装甲兵的怒吼intentional pain river keeps others safe故意痛苦的河流使他人安全medics focus those who eat fists医务人员将重点放在那些吃拳头的人身上")
    if score in range(2, 7):
      print("no freaking way dude")
      time.sleep(1)
      print("wise men failure 基爾紮紮德 swordmen killed by ice wizzard 冰精灵 scandinavian rage 危險地上的圓圈 require new blessings 朋友是")

questions = [\
    ("how much dollars is one million dollars","one million dollars"),
    ("convert 70 billion degrees to radians", "1,221,730,476.4"),
    ("yeah?", "on god"),
    ("what color is an orange", "An orange, the fruit, gets its characteristic color from carotenoids, particularly beta-carotene, which reflect light in the red and yellow spectrum, creating the vibrant hue we associate with the fruit. This color arises from the degradation of chlorophyll as the fruit ripens, revealing the orange pigments. Orange is a secondary color on the visible spectrum, situated between red and yellow, and is perceived by the human eye when light in these wavelength ranges is detected. Beyond its biological and chemical origins, the color orange holds cultural significance, often symbolizing energy, vitality, and warmth in various societies. Thus, the color of an orange is not just a visual trait, but a complex interaction of light, biology, and cultural meaning."),
    ("what is your name", "barrett"),
    ("do you like this quiz", "yes"),
    ("what is this https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQELv8Fn63rtiXqq3Ag71BaV2UuHiIneP_8hQ&s", "the death of america"),
    ("how do you spell minecraft", "MineCraft"),
]

run_quiz(questions)    
