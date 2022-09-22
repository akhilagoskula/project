print("Hi sir/madam,Welcome to star resturant")
print("Here is our menu")

paneer = 350;
corn = 200;
mushroom = 300;
chicken = 250;
mutton = 500;
fish = 450;
prawns = 480;
paneerbiryani = 380;
mushroombiryani = 320;
chickenbiryani = 350;
beetrootbiryani = 220;
muttonbiryani = 550;
fishbiryani = 550;
total = 0.0;
DONE = False
        
print("""
+-------------------------------------------+
| The Restaurant at the End of the Universe |
+---------------------------------+---------+
| A\t paneer               | $""" + str(paneer) + """|
+---------------------------------+---------+
| B\t corn                 | $""" + str(corn) + """|
+---------------------------------+---------+
| C\t mushroom             | $""" + str(mushroom) + """|
+---------------------------------+---------+
| D\t chicken              | $""" + str(chicken)  + """|
+---------------------------------+---------+
| E\t mutton               | $""" + str(mutton) + """|
+---------------------------------+---------+
| F\t fish                 | $""" + str(fish) + """|
+---------------------------------+---------+
| G\t prawns               | $""" + str(prawns) + """|
+-------------------------------------------+
| H\t paneer biryani       | $""" + str(paneerbiryani) + """|
+---------------------------------+---------+
| I\t mushroom biryani     | $""" + str(mushroombiryani) + """|
+---------------------------------+---------+
| J\t beetroot biryani     | $""" + str(beetrootbiryani) + """|
+---------------------------------+---------+
| K\t chicken biryani      | $""" + str(chickenbiryani) + """|
+---------------------------------+---------+
| L\t mutton biryani       | $""" + str(muttonbiryani)  + """|
+---------------------------------+---------+
| M\t fish biryani         | $""" + str(fishbiryani) + """|
+---------------------------------+---------+

""");
while True:
  print("Total:", total);
  Item = input("Select a letter or 'done': ");
  if Item == "A":
    total += paneer;
  elif Item == "B":
    total += corn;
  elif Item == "C":
    total += mushroom;
  elif Item == "D":
    total += chicken;
  elif Item == "E":
    total += mutton;
  elif Item == "F":
    total += fish;
  elif Item == "G":
    total += prawns;
  elif Item == "H":
    total += paneerbiryani;
  elif Item == "I":
    total += mushroombiryani;
  elif Item == "J":
    total += beetrootbiryani;
  elif Item == "K":
    total += chickenbiryani;
  elif Item == "L":
    total += muttonbiryani;
  elif Item == "M":
    total += fishbiryani;
  elif Item == "done":
    print("Final total:", total);
  else:
    print("can you please order from the menu:")
    DONE = True
       
           
