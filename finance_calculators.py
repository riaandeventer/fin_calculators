# Software Engineer: RIAAN DEVENTER
# Written on 11 December 2022

#------------------------------------------------------------------------------------------------  
# Assume that you have been approached by a small financial company and asked to create a program 
# that allows the user to access two different financial calculators: 
# an investment calculator and a home loan repayment calculator.
#
# At the top of the file include the line import math
# Write the code that will do the following:
#
# 1. The user should be allowed to choose which calculation they want to do. 
#    -  The first output that the user sees when the program runs should look like this :
#------------------------------------------------------------------------------------------------
# Choose either 'investment' or 'bond' from the menu below to proceed:
# 
# investment    -   to calculate the amount of interest you'll earn on your investment
# bond          -   to calculate the amount you'll have to pay on a home loan
#------------------------------------------------------------------------------------------------
# 
#     -  How the user capitalises their selection should not affect how the program proceeds. 
#           i.e. ‘Bond’, ‘bond’, ‘BOND’ or ‘investment’, ‘Investment’, ‘INVESTMENT’, etc., 
#           should all be recognised as valid entries. 
#     -  If the user doesn’t type in a valid input, show an appropriate error message.
#
# 2. If the user selects ‘investment’, do the following:
#    -  Ask the user to input:
#       * The amount of money that they are depositing.
#       * The interest rate (as a percentage). Only the number of the interest rate should be entered, 
#         don’t worry about having to deal with the added ‘%’,  e.g. The user should enter 8 and not 8%.
#       * The number of years they plan on investing.
#       * Then ask the user to input if they want “simple” or “compound” interest, 
#         and store this in a variable called interest. 
#    -  Depending on whether or not they typed “simple” or “compound”, output the appropriate amount 
#       that they will get back after the given period, at the specified interest rate. 
#    -  Look below for the formula to be used:
#       *  The total amount when simple interest is applied is calculated as follows: A = P(1 + r * t)
#          The Python equivalent is very similar: A = P*(1+r*t)
#       *  The total amount when compound interest is applied is calculated as follows: A = P(1 + r) ^ t
#          The Python equivalent is slightly different: A = P* math.pow((1+r),t)
#       *  In the formulae above:
#          > ‘r’ is the interest entered above divided by 100, e.g. if 8% is entered, then r is 0.08.
#          > ‘P’ is the amount that the user deposits.
#          > ‘t’ is the number of years that the money is being invested.
#          > ‘A’ is the total amount once the interest has been applied.
#    -  Print out the answer!
# 
#    -  Try entering 20 years and 8 (%) and see what the difference is depending on the type of interest rate!
#
# 3. If the user selects ‘bond’, do the following:
#    -  Ask the user to input:
#       * The present value of the house. e.g. 100000
#       * The interest rate. e.g. 7
#       * The number of months they plan to take to repay the bond. e.g. 120
#    -  Bond repayment formula:
#       *  The amount that a person will have to repay on a home loan each month 
#          is calculated as follows: repayment = x = (i.P)/(1 - (1+i)^(-n))
#       *  In the formula above:
#          > ‘P’ is the present value of the house.
#          > ‘i’ is the monthly interest rate, calculated by dividing the annual interest rate by 12.
#          > ‘n’ is the number of months over which the bond will be repaid.
#    -  Calculate how much money the user will have to repay each month and output the answer.
#
# *****************************************************
import math

# Prepare the user screen interface

print ()
print ("Choose either 'investment' or 'bond' from the menu below to proceed:\n")
print ("investment    -   to calculate the amount of interest you'll earn on your investment")
print ("bond          -   to calculate the amount you'll have to pay on a home loan\n")

# Request the user input
usr_choice_str = input ("Please enter your choice (e.g. investment or bond): ")
usr_choice_str = usr_choice_str.upper ()

if usr_choice_str == "INVESTMENT" :

    # Request the user input for the investment calculator option
    print ()
    inv_dep_flt = float (input ("Enter your investment deposit. (e.g. 100000) : "))
    print ()
    inv_rate_flt = float (input ("Enter the interest rate of your investment. (e.g. Enter 8 or 8.5 and not 0.08 or 8.5%) : "))
    print ()
    inv_yrs_int = int (input ("How many years do you plan on investing? (Enter full years) : "))
    print ()
    
    interest_str = input ("Do you want (s)imple or (c)ompount interest? (Enter s or c) : " )
    print ()
    if interest_str != "" :
        interest_str = interest_str [0].upper ()            # Store first letter of choice as CAPS to illiminate redundant testing

    if interest_str == "S" :                            # S for Simple interest
        # Calculate the return amount (A) = inDeposit * ((1 + (interest-rate / 100)) * years-to-invest)
        inv_return_flt = inv_dep_flt * ((1 + (inv_rate_flt / 100)) * inv_yrs_int)

        # Display the result in a meaningful way
        print (f"A deposit of R{inv_dep_flt:.2f} after {inv_yrs_int} years, at a simple interest rate of {inv_rate_flt:.2f}%, ")
        print (f"will give you a return of R{inv_return_flt:.2f}. \n")

    elif interest_str == "C" :                          # C for Compound interest
        # Calculate the return amount (A) = Deposit * ((1 + (interest-rate / 100)) to the power of years-to-invest)
        inv_return_flt = inv_dep_flt * math.pow (1 + (inv_rate_flt / 100), inv_yrs_int)
        
        # Display the result in a meaningful way
        print (f"A deposit of R{inv_dep_flt:.2f} after {inv_yrs_int} years, at a compound interest rate of {inv_rate_flt:.2f}%, ")
        print (f"will give you a return of R{inv_return_flt:.2f}. \n")
    else :
        print ("You did not enter a valid input! Run program again to use calculator.")
        print ()

elif usr_choice_str == "BOND" :

    # Request the user input for the bond calculator option
    print ()
    bnd_val_flt = float (input ("Enter the present value of the house. (e.g. 100000) : "))
    print ()
    bnd_rate_flt = float (input ("Enter the yearly interest rate of your bond. (e.g. Enter 8 or 8.5 and not 0.08 or 8.5%) : "))
    print ()
    bnd_mths_int = int (input ("Enter the number of months you plan to take to repay the bond. (e.g. 120) : "))
    print ()

    # Calculate the monthly repayment amount (R) = 
    # [(monthly-interest-rate / 100) * present-value] / [1 - ((1 + (monthly-interest-rate / 100)) to power of negative(months-to-pay-bond))]

    bnd_repay_flt = (((bnd_rate_flt / 12) / 100) * bnd_val_flt) / (1 - math.pow (1 + ((bnd_rate_flt / 12) / 100), -bnd_mths_int))

    # Display the result in a meaningful way
    print (f"A bond of R{bnd_val_flt:.2f} paid over {bnd_mths_int} months, at a yearly interest rate of {bnd_rate_flt:.2f}%, ")
    print (f"will give you a monthly payment of R{bnd_repay_flt:.2f}. \n")

else :

    # Display an error message if the user did not input investment or bond
    print ()
    print ("You did not enter a valid input! Run program again to choose a calculator.")
    print ()

#************** END OF PROGRAM **************