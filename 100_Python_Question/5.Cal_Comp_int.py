#take input principal,rate,time
principal = float(input("Enter the Principal: "))
rate = float((input("Enter the rate: ")))
time = float(input("Enter the time: "))

#Calculate Compound interest
Compound_interest = principal * (1 + rate/100)**time
#print result
print("Compound Interest is: ",Compound_interest)

#output
#Enter the Principal: 2000
#Enter the rate: 5
#Enter the time: 2
#Compound Interest is: 2205.0