# Program #4: Coordinates
#Henry Forst
#10/16/25
# Write a distance function that will take two 3-dimensional coordinates (as input) 
# and will return (as output) the distance between those points in space.  
# The 3-dimensional coordinates must be stored as tuples.
import math
def distance(coord1, coord2):
    x1, y1, z1 = coord1
    x2, y2, z2 = coord2 
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2 + (z2 - z1)**2)
def main():
    try:
        coord1 = eval((input("Enter the first coordinate (x1, y1, z1) seperate numbers with a comma: ")))
        coord2 = eval((input("Enter the second coordinate (x2, y2, z2 seperate numbers with a comma): ")))
        if len(coord1) != 3 or len(coord2) != 3:
            print("Each tuple needs to have three variables")
            return
        print (f'The distance between the points is:{distance(coord1, coord2): .2f} spaces')
    except Exception as er:
        print(f"Error: {er}")

# Now write a mainline that has the user enter the two tuples.  
# The mainline calls the distance function and stores the distance in a variable.  The mainline then displays the distance.  
# Also include exception handling to deal with faulty input.
# The distance between two points (x1,y1,z1) and (x2, y2, z2) is 
#    given by:   sqrt ((x2-x1)^2 + (y2 - y1)^2 + (z1 - z2)^2) 
main()