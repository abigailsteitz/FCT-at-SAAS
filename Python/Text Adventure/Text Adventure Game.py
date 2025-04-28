print("Welcome to Pig Farm")

print("Would you like ) to buy some pigs? yes or no?")
typeOfMarker = input()

if typeOfMarker == "no":
  print("you lose")
  
  kick = input()
  
  if kick == "yes":
    print("your great")
    
    print("Buy food?")
    kick = input()
    
    if kick == "yes":
      print("pigs are nourished")
    else:
      print("your ppigs die")
  else:
    print("I have no clue")
elif typeOfMarker == "yes":
  print("your great")

  print("do you want to buy food?")
  kick = input()

  if kick == "yes":  
    print("your pigs are nourished")

  
  if kick == "no":
   print("your pigs die")

  print("do you want to have a girl and a boy pig?")
  kick = input()

  if kick == "yes":  
    print("YAY more pigs")
  
  
  if kick == "no":
   print("no more pigs")


  print("do you want to buy more fence?")
  kick = input()

  if kick == "yes":  
    print("YAY thrive")

  
  if kick == "no":
   print("your pigs escapey")


  print("do you want to sell half of your pigs?")
  kick = input()

  if kick == "yes":  
    print("you get money and win!")
    kick = input()
  
  
  if kick == "no":
   print("you go bancrupt and lose")
else:
  print("Not understood " + typeOfMarker)