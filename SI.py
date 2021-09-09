currency = str(input("Enter currency symbol: "))
P = float(input("Enter principal: "))
R = float(input("Enter rate of interest: "))
T = int(input("Enter no. of years: "))

SI = (P*R*T)/100

print("\nS.I is\n",currency,SI)