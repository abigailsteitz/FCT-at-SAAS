print("hello!! what's your name?")
username = input()

print("it's nice to meet you, "+ username + "!")
print(" ")

print("welcome to my quiz about pop culture! do you want to play?")
print("a) yes!!")
print("b) no!!")
useranswer0 = input()


if useranswer0 == "a":
  print("here you go!!")
  print (" ")
  score = 0
else:
  print("alright! have a good day!")


# ask user a question, get their answer, check if it's correct
if useranswer0 == "a":
  print("first question: three movies are tied for the most Academy Award wins. which one of the following isn't one of those three?")
  print("a) Titanic")
  print("b) Forrest Gump")
  print("c) Ben-Hur")
  print("d) The Lord of the Rings: The Return of the King")
  useranswer1 = input()
  print(useranswer1)
  
  if useranswer1 == "b" or useranswer1 == "Forrest Gump" :
    print("correct!!!")
    score = score + 100
    print("you now have: " + str(score) + " out of 500 points!")
    print (" ")
  else:
    print("incorrect, sorry!! the answer was b, Forrest Gump!")
    print (" ")
    
    
    
  # second question!!
  print("next question: what is the longest-running animated television show in the united states?")
  print("a) The Simpsons")
  print("b) Spongebob Squarepants")
  print("c) Tom and Jerry")
  print("d) Crusader Rabbit")
  useranswer2 = input()
  print(useranswer2)
  
  if useranswer2 == "a" or useranswer2 == "The Simpsons" :
    print("correct!!!")
    score = score + 100
    print("you now have: " + str(score) + " out of 500 points!")
    print (" ")
  else:
    print("incorrect, sorry!! the answer was a, The Simpsons!")
    print (" ")
    
    
    
  # third question!!
  print("next question: what is the top streamed song of all time on spotify?")
  print("a) Taylor Swift's 'Cruel Summer'")
  print("b) Lil Nas X's 'Old Town Road'")
  print("c) Sabrina Carpenter's 'Espresso'")
  print("d) The Weeknd's 'Blinding Lights'")
  useranswer3 = input()
  print(useranswer3)
  
  if useranswer3 == "d" or useranswer3 == "Blinding Lights" or useranswer3 == "The Weeknd's 'Blinding Lights'":
    print("correct!!!")
    score = score + 100
    print("you now have: " + str(score) + " out of 500 points!")
    print (" ")
  else:
    print("incorrect, sorry!! the answer was d, The Weeknd's 'Blinding Lights'!")
    print (" ")
    
    
    
  # fourth question!!
  print("next question: what was Stephen King’s first published novel?")
  print("a) Carrie")
  print("b) The Dead Zone")
  print("c) The Shining")
  print("d) ’Salem’s Lot")
  useranswer4 = input()
  print(useranswer4)
  
  if useranswer4 == "a" or useranswer4 == "Carrie":
    print("correct!!!")
    score = score + 100
    print("you now have: " + str(score) + " out of 500 points!")
    print (" ")
  else:
    print("incorrect, sorry!! the answer was a, Carrie!")
    print (" ")
    
  
   # last/fifth question!!
  print("last question!!: in the Tom Holland spider-man movies, what is the name of his love interest (played by Zendaya)?")
  print("a) Macy-Jane Watson")
  print("b) Madeline Jolene Waston")
  print("c) Mary Jane Watson")
  print("d) Michelle Jones-Watson")
  useranswer5 = input()
  print(useranswer5)
  
  if useranswer5 == "d" or useranswer5 == "Michelle Jones-Watson":
    print("correct!!!")
    print (" ")
    score = score + 100
    print ("congratulations! you made it through this quiz!!")
    print ("your total score is: " + str(score) + "/500 points!!")
  else:
    print("incorrect, sorry!! the answer was d, Michelle ('MJ') Jones-Watson!")
    print (" ")
    

    # bonus question!!
  if score == 500:
    print("⭐")
    print("you got a perfect score! you get a bonus question!!")
    print("")
    print("which singer was friends with the character 'al pacino' in The Godfather is based on?")
    print("a) Johnnie Johnston")
    print("b) Perry Como")
    print("c) Frank Sinatra")
    print("d) Ray Charles")
    useranswerb = input()
    print(useranswerb)
      
    if useranswerb == "c" or useransweb == "Frank Sinatra":
     print("correct!!!")
     print (" ")
    score = score + 100
    print ("wow!! you beat the bonus question too!! you win!")
    print ("your final total score is: " + str(score) + "/500 points!!")
else:
     print("incorrect, sorry!! the answer was c, Frank Sinatra! you had a good run!!")
     print (" ")
    
    
    