# Simple intrest calculation

def simple_intrest(p,n,r):
    i = (p*n*r)/100
    amt = p + i
    return{"intrest":i, "amount":amt}

# Take input from users in console
p = float(input("Please enter Principal in INR:"))
n = int(input("Please enter Number of Years:"))
r = float(input("please enter Rate of intrestin %p.a. : "))

# Calculate intrest and amount
results = simple_intrest(p, n, r)

# Print the results
print(results)
