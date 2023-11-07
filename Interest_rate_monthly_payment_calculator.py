# Interest_rate_monthly_rate_calculator
# steps 
# collect the neccesary data / inputs , which are the following 
# principal(total money), annual interest rate , years 
# calculate the monthiy payment 

def main():
    print('this is a monthly payment loan calculator ')
    print('')

    
    
    principal=float(input('Input the loan amount :'))
    apr=float(input('Input the annual interest rate :'))
    years=int(input('enter amount of years :'))

    monthly_interest_rate=apr/1200
    amount_of_months =years*12
    monthly_payment=principal*monthly_interest_rate/(1-(1+monthly_interest_rate)**(-amount_of_months ))


    print('the monthly payment for this loan is :'+str(monthly_payment))
main()

#this is a monthly payment loan calculator 

#Input the loan amount :20000
#Input the annual interest rate :3
#enter amount of years :5
#the monthly payment for this loan is :359.3738132812698
    


 
