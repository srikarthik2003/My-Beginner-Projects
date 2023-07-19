import matplotlib.pyplot as plt
import random
import numpy as np
import math


print("what do you want to play:")
print("1,scatter plot game!!")
print("2.projectile game!!")
print("3.two step solve for a vsriable!!")

def scatter_plot():
  score = 0

  xmin = -8
  xmax = 8
  ymin = -8
  ymax = 8

  fig, ax = plt.subplots()

  for i in range(0,3):
      xpoint = random.randint(xmin, xmax)
      ypoint = random.randint(ymin, ymax)
      x = [xpoint]
      y = [ypoint]
      plt.axis([xmin,xmax,ymin,ymax])
      plt.plot([xmin,xmax],[0,0],'b')
      plt.plot([0,0],[ymin,ymax], 'b')
      plt.plot(x, y, 'ro')
      print(" ")
      plt.grid()
      plt.show()
      guess = input("Enter the coordinates of the red point point: \n")
      guess_array = guess.split(",")
      xguess = int(guess_array[0])
      yguess = int(guess_array[1])
      if xguess == xpoint and yguess == ypoint:
          score = score + 1

  print(f"Your score:{score}" )


def projectile_game():

  loc = random.randint(0,100)
  h = random.randint(0,1000)

  print(f"a rocket has to clear a wall {loc} metres away")
  a = -4.9
  b = float(input("enter the velocity:"))
  c = 0

  vx = -b/(2*a)
  vy = a*vx**2+b*vx+c

  xmin = -1
  xmax = int((2*vx)+20)
  ymin = -1
  ymax = int(vy+10)

  fig,ax=plt.subplots()
  plt.axis([xmin,xmax,ymin,ymax])
  plt.plot([xmin,xmax],[0,0],'k')
  plt.plot([0,0],[ymin,ymax],'k')
  points = 2*(xmax-xmin)

  x = np.linspace(xmin,xmax,points)
  y = a*x**2+b*x+c

  plt.plot(x,y,'b')
  plt.plot([loc,loc],[0,h],'r')


  root_2 = round((-b-math.sqrt(b**2-4*a*c))/(2*a))
  if root_2>=loc:
    print(f"success, croosed by {root_2} metres")
  else:
    print("missed!!")

  print("")


  plt.show()




while True:
  choose = input("enter your choice(0 to quit):")
  if choose == '1':
    scatter_plot()
  elif choose == '2':
    projectile_game()
  elif choose == '0':
    break
  else:
    print("invalid choice,choose again!!")