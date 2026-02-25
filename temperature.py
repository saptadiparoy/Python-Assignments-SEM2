#to create a custom module which helps in temperature conversion

#1. Celsius to farenheit:
def cel_to_faren(celsius):
    faren =  ((9/5) * celsius) + 32
    print (f"{celsius} C is : {faren} F")

#2. Farenheit to Celsius:
def faren_to_cel(faren):
    celsius =  (faren - 32) * 5/9
    print (f"{faren} F is : {celsius} C")

#3. Celsius to Kelvin:
def cel_to_k(celsius):
    kelvin = celsius + 273
    print (f"{celsius} C is :   {kelvin} K")
