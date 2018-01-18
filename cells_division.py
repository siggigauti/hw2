import matplotlib.pyplot as plt
import numpy as np
import math

cells = 5000 #The initial cell count at time 0
cumulative_cells=[] #This is a list, empty right now. Will contain the cell count at each hour [5000, 10000, ...]
cumulative_cells_oxygen=[] #Same for these, just empty lists
cumulative_cells_095=[]
for i in range(24): #Here we iterate from 0 to 24, i=0, then i=1, then i=2,...
	cumulative_cells.append(cells) #We add the number cells into the list.  Was just [], now its [5000]
	cells *= (100/24) #Multiply the cells

cells = 5000
for i in range(24):
	cumulative_cells_095.append(cells)
	cells *= (95/24)


axes = plt.gca() #Needed to reduce the size of the y or x axis
#axes.set_ylim([0,2.5*math.pow(10,19)])      #Here I set the y axis to only show from 0 to 2.5*10^19 
plt.plot(cumulative_cells) #Here I plot the cumulative cell count
plt.ylabel("Number of cells")
plt.xlabel("Hours")
plt.plot(cumulative_cells_095)
plt.show() #Needed to display the graph.
