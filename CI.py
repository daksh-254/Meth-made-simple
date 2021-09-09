currency = str(input("Enter currency symbol: "))
P = float(input("Enter principal: "))
R = float(input("Enter rate of interest: "))
T = int(input("Enter no. of years: "))

CI = P*(pow(1+(R/100), T))

print("\nC.I is\n",currency,CI)