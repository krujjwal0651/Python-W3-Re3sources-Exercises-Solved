# Simple Interest Calculator

def si(principal, roi, year):
    res = (principal * year * roi)/100
    return res

P = int(input("Enter the Principal Amount : "))
R = float(input("Enter the Rate of Interest : "))
T = int(input("Enter the Time in years, Loan is taken for  : "))

print(f"The Simple Interest on {P} for {T} Years with ROI {R} will be : {si(P,R,T)}")

print(f"And the Total Amount to be paid is : {P+si(P,R,T)}")
