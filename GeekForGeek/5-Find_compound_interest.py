# Compound Interest Calculator

def ci(principal, roi, year):
    amount = principal * (((1 + (roi/100)))**year)
    res = amount - principal
    return amount, res

P = int(input("Enter the Principal Amount : "))
R = float(input("Enter the Rate of Interest : "))
T = int(input("Enter the Time in years, Loan is taken for  : "))

A, CI = ci(P,R,T)

print(f"The Compound Interest on {P} for {T} Years with ROI {R} will be : {CI}")

print(f"And the Total Amount to be paid is : {A}")
