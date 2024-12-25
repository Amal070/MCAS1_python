from PROGRAM_8.graphics import circle,rect 
r=int(input("Enter the radius of circle:"))
circle.cir_area(r)
circle.circ_perimeter(r)
l=int(input("\nEnter the length of rectangle:"))
b=int(input("Enter the breadth of rectangle:"))
rect.area(l,b)
rect.perimeter(l,b)

from PROGRAM_8.graphics.threedgraphics import cuboid,sphere

l1=int(input("\nEnter the length of cuboid:"))
b1=int(input("Enter the breadth of cuboid:"))
h1=int(input("Enter the height of cuboid:"))
cuboid.area_cub(l1,b1,h1)
cuboid.perimeter_cub(l1,b1,h1)

r1=int(input("\nEnter the radius of sphere:"))
sphere.area_sp(r1)
sphere.peri_sp(r1)