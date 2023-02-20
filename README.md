# Financial Calculator Program

This program allows the user to access two different financial calculators: 
an investment calculator and a home loan repayment calculator.

## Table of Content
1. Installation
2. Executing Program
3. Authors

### Installation

### 1.  Implementing the program in a virtual environment.

##### 1.1   Dependencies

The virtual environment requires the installation of python and importing the math module.

##### 1.2   Copying Files

Go to the directory or folder where you want to install the project and enter the following command in the command line:
```
>git clone https://github.com/riaandeventer/fin_calculators
```
If you are asked for a login then it should be because you might have made a typing error with the link.

##### 1.3   Run Program

If your files copied successfully, there should be a folder fin_calculators when you (for windows) enter the >dir command.
Go to this directory with below command.
```
>cd fin_calculators
```
Now we can run the program with below command:
```
>python finance_calculators.py
```

### Executing Program

* Run the program
* You will see the menu.

###### 1. The user chooses which calculation they want to do. 

-  The first output that the user sees when the program runs should look like this :
_______________________________________________________________________________________________
 Choose either 'investment' or 'bond' from the menu below to proceed:
 
 investment    -   to calculate the amount of interest you'll earn on your investment
 
 bond          -   to calculate the amount you'll have to pay on a home loan
_______________________________________________________________________________________________

-  If the user doesn't type in a valid input, the program shows an appropriate error message.

###### 2. If the user selects 'investment', the user must input:
   * The amount of money that they are depositing.
   * The interest rate (as a percentage). Only the number of the interest rate should be entered, e.g. The user should enter 8 and not 8%.
   * The number of years they plan on investing.
   * Does the user want “simple” or “compound” interest, 
     -  Depending on whether or not they typed 'simple' or 'compound', the program outputs the appropriate amount 
        that they will get back after the given period, at the specified interest rate. 
     -  Look below for the formula used:
        *  The total amount when simple interest is applied is calculated as follows: A = P(1 + r * t)
        *  The total amount when compound interest is applied is calculated as follows: A = P(1 + r) ^ t
        *  In the formulae above:
           > ‘r’ is the interest entered above divided by 100, e.g. if 8% is entered, then r is 0.08.
           > ‘P’ is the amount that the user deposits.
           > ‘t’ is the number of years that the money is being invested.
           > ‘A’ is the total amount once the interest has been applied.

###### 3. If the user selects ‘bond’, the user must input:
   * The present value of the house. e.g. 100000
   * The interest rate. e.g. 7
   * The number of __months__ they plan to take to repay the bond. e.g. 120
     -  Calculate how much money the user will have to repay each month and output the answer.
     -  Bond repayment formula:
        *  The amount that a person will have to repay on a home loan each month is calculated as follows: repayment = x = (i.P)/(1 - (1+i)^(-n))
        *  In the formula above:
           > ‘P’ is the present value of the house.
           > ‘i’ is the monthly interest rate, calculated by dividing the annual interest rate by 12.
           > ‘n’ is the number of months over which the bond will be repaid.

## Authors

Riaan Deventer  - [LinkedIn: @riaandeventer](https://www.linkedin.com/in/riaandeventer/)
