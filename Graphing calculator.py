

from sympy import *
import numpy as np
import matplotlib.pyplot as plt


def table():

  equation = input("Enter the equation (in terms of 'a'): ")
  title = "Graph of the Equation: {}".format(equation)

  rows = [[0, 0]]

  for a in range(1, 10):
      rows.append([a, eval(equation)])  

  table = np.array(rows)

  x = table[:, 0]
  y = table[:, 1]

  plt.plot(x, y, 'bx')
  plt.xlabel('x')
  plt.ylabel('y')
  plt.title(title)
  plt.grid(True)
  plt.show()

  fig, ax = plt.subplots()
  ax.set_axis_off()
  table = ax.table(cellText=table, colLabels=["x", "y"], loc='center', cellLoc='center')
  plt.show()


def sys_eq():
   
   x,y = symbols('x y')
   eq1 = input("enter eq1  in terms of x and y:")
   eq2 = input("enter eq2  in terms of x and y:")
   print("solution:",linsolve([eq1,eq2], (x, y)))

def graph_eqs_plot_pt_of_intersection():

  print("First equation: y = mx + b")
  mb_1 = input("Enter m and b, separated by a comma: ")
  mb_in1 = mb_1.split(",")
  m1 = float(mb_in1[0])
  b1 = float(mb_in1[1])

  print("Second equation: y = mx + b")
  mb_2 = input("Enter m and b, separated by a comma: ")
  mb_in2 = mb_2.split(",")
  m2 = float(mb_in2[0])
  b2 = float(mb_in2[1])

  x,y = symbols('x y')
  first = m1*x + b1 - y
  second = m2*x + b2 - y
  solution = nonlinsolve([first, second], (x, y))
  x_solution = round(float(solution.args[0][0]),3)
  y_solution = round(float(solution.args[0][1]),3)


  xmin = int(x_solution) - 20
  xmax = int(x_solution) + 20
  ymin = int(y_solution) - 20
  ymax = int(y_solution) + 20
  points = 2*(xmax-xmin)


  graph_x = np.linspace(xmin,xmax,points)


  y1 = m1*graph_x + b1
  y2 = m2*graph_x + b2

  fig, ax = plt.subplots()
  plt.axis([xmin,xmax,ymin,ymax])
  plt.plot([xmin,xmax],[0,0],'k') 
  plt.plot([0,0],[ymin,ymax], 'k') 


  plt.plot(graph_x, y1)

  plt.plot(graph_x, y2)

  plt.plot([x_solution],[y_solution],'rx')

  plt.show()
  print(" ")
  print(f"Solution:({x_solution}, {y_solution})")

def quadratics():
  
  a = int(input("enter a value for a:"))
  b = int(input("enter a value for b:"))
  c = int(input("enter a value for c:"))

  vx = -b/2*a
  vy = a*(vx**2)+b*(vx)+c
  
  print(f"vertex = ({vx},{vy})")
  
  xmin = -10
  xmax = 10
  ymin = -10
  ymax = 10

  fig,ax = plt.subplots()
  plt.axis([xmin,xmax,ymin,ymax])
  plt.plot([xmin,xmax],[0,0],'b')
  plt.plot([0,0],[ymin,ymax],'b')
 
  d = b**2-(4*a*c) 
  if d>=0:
    root_1 = ((-b+np.sqrt(d))/(2*a))
    root_2 = ((-b-np.sqrt(d))/(2*a))
    print(f"root_1 = {root_1}\nroot_2 = {root_2}")
    plt.plot([root_1,root_2],[0,0],'kx')
  else:
    print("no real roots!!")
  
 
  points = 2*(xmax-xmin)

  x = np.linspace(xmin,xmax,points)
  y = a*x**2+b*x+c

  plt.plot(x,y,'b')
  plt.plot([vx],[vy],'rx')
  plt.show()







while True:
  print("1.Display the graph and a table of values for any ")
  print("2.Solve a system of two equations without graphing")
  print("3.Graph two equations and plot the point of intersection")
  print("4.graph a quadratic equation, plot the roots and vertex")
  print()
  choose = input("enter choice:")
  if choose == '1':
    table()
  elif choose == '2':
    sys_eq()
  elif choose == '3':
    graph_eqs_plot_pt_of_intersection()
  elif choose == '4':
    quadratics()
  elif choose == '0':
    break
  print()
