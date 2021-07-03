import tkinter as tk
import time
from Node import Node
from Dijkstras import dijkstrasRecursion, initializeDijkstras

grid = [ [None]*20 for _ in range(20) ]

root = tk.Tk()

global gameframe
gameframe = tk.Frame(root)
gameframe.pack()

#Make the start dijkstras button
startButton = tk.Label(gameframe,text='Start Dijkstras',bg= "grey")
startButton.grid(row=0, column=0, columnspan= 15)
startButton.bind('<Button-1>', lambda e:doDijkstras())

# Label(master, image = img1).grid(row = 0, column = 2,
#        columnspan = 2, rowspan = 2, padx = 5, pady = 5)

for i,row in enumerate(grid):

    for j,column in enumerate(row):
        name = str(i)+str(j)
        L = tk.Label(gameframe,text='    ',bg= "grey")
        L.grid(row=i+1,column=j+1,padx='3',pady='3')
        L.bind('<Button-1>',lambda e,i=i,j=j:on_click(i,j,e))
        node = Node(i, j, L)
        grid[i][j] = node


def on_click(row, col, event):
    print(f"clicked: {row},{col}. prevNode = {grid[row][col].prevNode}, distance = {grid[row][col].distance}")
    grid[row][col].widget['bg'] = 'red'
    #Toggle the passability of the terrain
    if grid[row][col].isPassable == True:
        grid[row][col].isPassable = False
        grid[row][col].widget['bg'] = 'black'
    else:
        grid[row][col].isPassable = True
        grid[row][col].widget['bg'] = 'grey'


def doDijkstras():
    startX = 5
    startY = 5
    finishX = 18
    finishY = 18
    initializeDijkstras(grid, startX, startY, finishX, finishY)
    dijkstrasRecursion(grid, root)




root.mainloop()







































# global gameframe
# gameframe = tk.Frame(root)
# gameframe.pack()

# #Make the start dijkstras button
# startButton = tk.Label(gameframe,text='Start Dijkstras',bg= "grey")
# startButton.grid(row=0, column=0)
# startButton.bind('<Button-1>', lambda e:doDijkstras())

# for i,row in enumerate(grid):

#     for j,column in enumerate(row):
#         name = str(i)+str(j)
#         L = tk.Label(gameframe,text='    ',bg= "grey")
#         L.grid(row=i+1,column=j+1,padx='3',pady='3')
#         L.bind('<Button-1>',lambda e,i=i,j=j:on_click(i,j,e))
#         node = Node(i, j, L)
#         grid[i][j] = node

# def on_click(row, col, event):
#     print(f"clicked: {row},{col}")
#     grid[row][col].widget['bg'] = 'red'
#     #Toggle the passability of the terrain
#     if grid[row][col].isPassable == True:
#         grid[row][col].isPassable = False
#         grid[row][col].widget['bg'] = 'black'
#     else:
#         grid[row][col].isPassable = True
#         grid[row][col].widget['bg'] = 'grey'

# def doDijkstras():
#     initializeDijkstras(grid, 0, 0, 5, 5)
#     print("Totally doing dijkstras rn")

#     # Until we get to the final node, do this
#     i = 0
#     while i < 15:
#         dijkstras(grid, gameframe)
#         time.sleep(.5)
#         i+=1
    

# root.mainloop()