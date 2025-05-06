import time

print(
"""
welcome to escaping saas
 its the end of lunch and you realized that you haven't eaten, your goal is to get daves hot chicken withought getting caught. 
 best of luck!(;
   \\      
   (o>   <(bok bok!)
\\_//)
 \_/_)
  _|_
""")
print("you start in abigails class, class started 5 mins ago. you are listening to attendace when your stomach starts rumbling really lound. you are REALLY hungry.")
 
print("(a) lie and say your going to the bathroom")
print("(b) just ask abigail")

useranswer = input()

if useranswer in ["lie and say your going to the bathroom", "a"]:
  print(
      """
      We Know abigail is nice you couldve just asked! now she will be suspicious if your gone to long so you better hurry!

      you run out of class and into the middle school. you see steve in the hallway.
      """)
    
  useranswer = input()

  print("steve is sometimes in a good mood and sometimes in a bad one. You can't avoid him now")
  print("(a) lie to steve and say your just going to class")
  print("(b) tell the truth and tell him you are going to get daves hot chicken")

  if useranswer in ["lie to steve and say your just going to class", "a"]:
    print("steve said 'thats not the right way to class kiddo! let me help you get to class' ")
    print("steve takes you to the high school and you are now separated from daves hot chicken by the gym")
      
    print("do you go through the gym or go around it?")
    print("(a) go through the gym")
    print("(b) go around the gym")
    
    if useranswer in ["go through the gym", "a"]:
      print("you go through the gym and see a group of kids playing basketball, you try to sneak past them but they see you and start chasing you!")
      print("you run out of the gym and out of saas! congrats! you made it out of saas! but be aware of security guards and teachers!")
      print("you are now at the vanderbilt corner but you bump into katherine ezzo")

      print("ezzo said 'hey! your supposed to be in class! where are you going?'")
      print("(a) say nothing and run away")
      print("(b) say your going to get daves hot chicken")

      if useranswer in ["say nothing and run away", "a"]:
        print("you avoided ezzo and she is calling the security guards!")
        print("you are now marked as a missing student and the security guards are looking for you!")

        print("you walk into daves hot chicken, do you get in line to order? or do you go back to saas and get in trouble?")
        print("(a) get in line to order")
        print("(b) go back to saas and get in trouble")

        if useranswer in ["get in line to order", "a"]:
          print("you get in line to order and the cashier said 'hey! you are not supposed to be here! go back to saas!'")
          print("the security guards come in and take you back to saas")
          print("you are now in trouble and have to go to the office")

          print("you lose! now your more hungry than ever!")


  if useranswer in ["tell the truth and tell him you are going to get daves hot chicken", "b"]:
      print("steve said 'You could've done that during Lunch kiddo go back to class' ")
      print("steve takes you back to your class and you are back to where you started") 

      print("now your stuck in class and you have to wait for the bell to ring! mission failed")
      
      useranswer = input()

if useranswer in ["just ask abigail", "b"]:
  print("Abigail said'No problem! just don't get caught!'  ")
  time.sleep(1)
  print("good job, you have abigails permission, but you realized you forgot your wallet in your locker, you have to go to your locker in the art center")
  time.sleep(1)
  print("you run to the art center and are about to turn the corner to your locker when a group of middle schoolers are running down the hall")

  useranswer = input()
  print("you have to make a choice")
  print("(a) wait for them to pass, but you might be late to class")
  print("(b) go against the flow of the middle schoolers")


  key = False
  if useranswer in ["wait for them to pass, but you might be late to class", "a"]:
    print("good job! you waited for the middle schoolers to pass and you are now at your locker. you see a key on the floor")
    key = True

  if useranswer in ["go against the flow of the middle schoolers", "b"]:
    print("you step into the crowd and are pushed the opposite direction of your locker!")  
    print("you have to make a choice")

  print("you go to the end of the hallway and see a door, you try to open it but its locked")
  if key == True:
    print("Good instinct to grab the key! you unlock the door and are now steps away from the exit")
  else:
    print("You ran out of time and now you have to go back to class! misson failed")

    useranswer = input()
    print("you walk out of saas and take a deep breath of fresh air, congrats! you made it out of saas! but be aware of security guards and teachers!")

    print("you are now at the vanderbilt corner and are about to cross the street but you bump into a homeless person")

    print("the homeless person said 'hey kiddo! you got any spare change?'")
    print("(a) give him a dollar")
    print("(b) say nothing and run away")

    if useranswer in ["give him a dollar", "a"]:
      print("the homeless person said 'thank you kiddo! you are a good person! what is your favorite food place around here? do you mind showing me?'")

    if useranswer in ["say nothing and run away", "b"]:
      print("you avoided the homeless person and are now at daves hot chicken")
      print("you walk into daves hot chicken and there is nobody there! you are the only one in the restaurant")

      answer = input()
