p = int ( input (" enter principal"))
r = int (input (" interest "))
t = int ( input ( " time period "))
Amount= p * (pow((1 + r / 100), t))
CI = Amount - p
print("Compound interest is", CI)
