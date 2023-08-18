#Create a temperature converter program that converts Celsius to Fahrenheit. If the Fahrenheit temperature is above 100, print "Hot day!
celsius=int(input("Enter a temp"))
fah=(1.8*celsius)+32
print("celsius to fahrenhite is:",fah)
if fah>100:
    print("Hot Day")
    print("The temp above 100 degrees")
