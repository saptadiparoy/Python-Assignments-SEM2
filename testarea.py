import area_module #type:ignore
while True:

    choice = int(input("1. Area of Circle \n2. Area of triangle \n3. Area of Rectangle \n4. exit \nSelect to calculate: "))

    if choice == 1:
        r = float(input("Enter radius of circle:    "))
        area_module.area_circle(r)
    
    elif choice == 2:
        h = float(input("Enter height of triangle:    "))
        b = float(input("Enter base of triangle:    "))
        area_module.area_triangle(h,b)

    elif choice == 3:
        h = float(input("Enter radius of rectangle:    "))
        b = float(input("Enter height of rectangle:    "))
        area_module.area_rectangle(h,b)
    
    elif choice == 4:
        print ("Exiting prog.")
        break

    else:
        print ("Invalid, try again.")