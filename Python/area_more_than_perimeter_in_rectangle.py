'''Q3. Given the length and breadth of a rectangle, write a program to find whether the area of the
rectangle is greater than its perimeter. For example, the area of the rectangle with length = 5 and
breadth = 4 is greater than its perimeter.'''

# Input length and breadth
length = float(input("Enter the length of the rectangle: "))
breadth = float(input("Enter the breadth of the rectangle: "))

# Calculate area and perimeter
area = length * breadth
perimeter = 2 * (length + breadth)

# Compare and display result
if area > perimeter:
    print("The area ", area ," is greater than the perimeter", perimeter ,".")
elif area < perimeter:
    print("The perimeter ", perimeter ,"is greater than the area ", area ,".")
else:
    print("The area and perimeter are equal.")
