# Create a class `Temperature` with methods to convert temperatures between Celsius and Fahrenheit.
# Use local variables to store intermediate results within the methods.
class Temperature:
    def Celcius_to_Far():
        c=float(input("Enter value for c"))
        Far=(c*9/5)+32
        print(Far)
    def Far_to_Celcius():
        F=float(input("Enter value for F"))
        Cel=(F-32)*5/9
        print(Cel)
Temperature.Celcius_to_Far()
Temperature.Far_to_Celcius()