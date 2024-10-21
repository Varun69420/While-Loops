num1 = float(input("Please enter the first value num1: "))
num2 = float(input("Please enter the first value num2:"))
while(num2!=0):
    temp = num2
    num2 = num1 % num2
    num1 = temp
    
hcf = num1
print("HCF of num1 and num2 = ",hcf)