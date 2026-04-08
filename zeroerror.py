#handling error when dividing by zero
while True :
    numerator = float(input("Enter a number (numerator):  "))
    denominator= float(input("Enter a number (denominator):  "))

    try:
        result = numerator/denominator

    except ZeroDivisionError:
        print ("Cannot divide by Zero, try again!")

    except ValueError:
        print ("Please enter a number and try again!")

    except Exception as e:
        print (f"due to {e}, program could not be run.")

    else:
        print("result is:   " , result)
        print ("Program end.")
        break