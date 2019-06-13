#Function to calculate Area of Triangles
def area(x1, y1, x2, y2, x3, y3): 
  
    return abs((x1 * (y2 - y3) + x2 * (y3 - y1)  
                + x3 * (y1 - y2)) / 2.0) 
  
  
 #Function to find if Origin is inside the Triangle 
def isInside(x1, y1, x2, y2, x3, y3, x, y):
    #print(x1, y1, x2, y2, x3, y3, x, y)
	# Calculate area of triangle ABC
    A = area(x1, y1, x2, y2, x3, y3)
    #print(A)
	# Calculate area of triangle PBC
    A1 = area (x, y, x2, y2, x3, y3)
	# Calculate area of triangle PAC
    A2 = area (x1, y1, x, y, x3, y3)
    # Calculate area of triangle PAB
    A3 = area (x1, y1, x2, y2, x, y)
    # Check if sum of A1, A2 and A3
    # is same as A
    if(A == A1 + A2 + A3):
        return True
    else:
        return False
  
# Main Function
def findcount():
	count = 0
	outcount=0
	#Setting Origin
	x = 0
	y = 0
	f= open("triangles.txt","r")
	f1 = f.readlines()
	for line in f1:
		coordinates=line.split(",")
		hasorigin = isInside(
			int(coordinates[0]),
			int(coordinates[1]),
			int(coordinates[2]),
			int(coordinates[3]),
			int(coordinates[4]),
			int(coordinates[5]),x,y
		)
#		print(hasorigin)
		if(hasorigin):
			count += 1
		else:
		    outcount += 1
	f.close() 
	print ('Number of triangles for which the interior contains the origin:',count)
	print ('Number of triangles for which the interior does not contains the origin:',outcount)
findcount()