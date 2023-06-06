import math




graph = ("""

    
   -|--------->  +Y
    |
    |
    |

   +X

   
   
   NW  N   NE
    \  |  /
     \ | /
 W____\|/_____E
      /|
     / | \ 
    /  |  
   SW  S   SE


""")



print(graph)
print("hello")


print("1.Diagonal")
print("2.Manahattan")
print("3.Euclidean")

heudis = int(input("Enter what distance you want to use as a heuristic distance: "))

#Function To Calculate Heuristic_Distance
def heuristic_distance(current_node,goal):
    if heudis==1:
        x = (current_node[0] - goal[0])
        y = (current_node[1] - goal[1])
        
        D=1
        d=2**(1/2)
        
        h = D*(x + y) + (d - 2*D)*min(x, y)

    elif heudis==2:
        h = abs(current_node[0] - goal[0]) + abs(current_node[1] - goal[1])

    else:
        x = abs(current_node[0] - goal[0])
        y = abs(current_node[1] - goal[1])
        h = math.sqrt(x*x + y*y)


    return h



#Function To Get The Neighbours Of The Current Node
def neighbours_node(thegrid,current):

    neighbours = []

    # EAST,WEST,NORTH,SOUTH,NORTHEAST,NORTHWEST,SOUTHEAST,SOUTHWEST
    directions = [(1,0),(-1,0),(0,1),(0,-1),(1,1),(-1,1),(1,-1),(-1,-1)]

    rows = len(thegrid)
    cols = len(thegrid[0])


    #Appending Neighbours In All 8 Directions Of Current Node
    for direction in directions:

        new_x = int(current[0] + direction[0])
        new_y = int(current[1] + direction[1])

        if 0 <= new_x < rows and 0 <= new_y < cols and thegrid[new_x][new_y] == 0:
            neighbours.append((new_x, new_y))

    return neighbours



#Our A* Function
def astar(grid, start_node, goal_node): 

    rows = len(grid)
    cols = len(grid[0])

    #Initializing A "Open_List"
    open_list = [(0, start_node)] 

    #Dictionary Containing "Parent" Of Nodes
    parent = {}  

    # Dictionary Containing "G_value" For Node
    g_value = {start_node: 0}  

    # Dictionary Containing "F_value" For Node
    f_value = {start_node: heuristic_distance(start_node, goal_node)}  


    
    while (len(open_list) != 0): 

        #Loop To Get Node With Minimum "F_Value" From Open_List
        current_node = open_list[0][1]
        min_f_score = open_list[0][0]

        for f_score,pos in open_list:
            if f_score < min_f_score:
                min_f_score = f_score
                current_node = pos


        #Combining And Returning The Shortest Path Nodes IF We Reach Goal_Node
        if current_node == goal_node:
        
            path = [current_node]
            while current_node in parent:
                current_node = parent[current_node]
                path.append(current_node)
            path.reverse()

            return path
        

        #Loop To Remove Current_Node From Open_list
        some_set = []
        for i in open_list:
            if i[1] != current_node:
                some_set.append(i)
        open_list = some_set


        #Getting All "8" NEighbours Of Current Node And Calculating Their G_Value
        for i in neighbours_node(grid, current_node):

            neighbour_g_value = g_value[current_node] + 1 

            #Appending G_Value And Parent Node For Each Neighbour If It Is Not Already In "G_Value Dictionary" Or Their "New G_Value" Is Less Than The "Previous G_Value"
            if i not in g_value or neighbour_g_value < g_value[i]:
                parent[i] = current_node
                g_value[i] = neighbour_g_value
                f_value[i] = neighbour_g_value + heuristic_distance(i, goal_node)
                open_list.append((f_value[i], i))


    return []




#our Grid
grid = [
    [0, 0, 0, 0, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 0, 0],
    [1, 1, 1, 0, 1],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0]
]



#Loop To Print "Our Grid"
for i in grid:
    print(i)



#Getting Input From User About Start_Node And End_Node
start_x = int(input("Enter your Start_X coordinate:"))
start_y = int(input("Enter your Start_Y coordinate:"))
start_pos = (start_x, start_y)

goal_x = int(input("Enter your Goal_X coordinate:"))
goal_y = int(input("Enter your Goal_Y coordinate:"))
goal_pos = (goal_x, goal_y)



#Calling The Function A*
path = astar(grid, start_pos, goal_pos)



#Printing The Shortest Path If Found Otherwise Returning A Statement That "Sorry, No Path Found..."
if path:
    print("Your Path:")
    for coor in path:
        print(coor)
else:
    print("Sorry, No path found...")