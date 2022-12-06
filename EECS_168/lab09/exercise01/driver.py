#driver.py

from circles import Circle

def userCircle():
    newCircle = Circle()
    newCircle.xpos = int(input("Enter an X coordinate for the center of your circle: "))
    newCircle.ypos = int(input("Enter a Y coordinate for the center of your circle:"))
    newCircle.rad = int(input("Enter a radius length for your circle: "))
    return newCircle

def printCircle(circle, *, name="Circle"):
    print(f"Information for {name}:")
    print(f"Location: ({circle.xpos},{circle.ypos})")
    print(f"Diameter: {circle.diameter()}")
    print(f"Area: {circle.area()}")
    print(f"Circumference: {circle.circum()}")
    print(f"Distance from orgin: {circle.orginDist()}")

def main():
    circle1 = userCircle()
    circle2 = userCircle()
    printCircle(circle1)
    printCircle(circle2)
    print(f"These circles intersect: {circle1.inter(circle2)}")

main()