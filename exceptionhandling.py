#to handle filenotfound and permissionerror when trying to open a file
def file_errors ():
    filename = input("enter file name with extension:   ")
    try:
        file = open(filename , "r")

    except FileNotFoundError:
        print ("File does not exist.")

    except PermissionError:
        print("you dont have permission to open this file")

    except Exception as e :
        print (f"due to {e}, program cannot be run.")
    
    else:
        print(filename.read())
    
    finally:
        print("thats all")


if __name__=="__main__":
    file_errors()
    