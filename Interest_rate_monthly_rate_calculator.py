def main():
    print('this is a monthly payment loan calculator ')
    print('')

    
    
    principal=float(input('Input the loan amount :'))
    apr=float(input('Input the annual interest rate :'))
    years=int(input('enter amount of years :'))

    monthly_interest_rate=apr/1200
    amount_of_months =years*12
    monthly_payment=principal*monthly_interest_rate/(1-(1+monthly_interest_rate)**(-amount_of_months ))


    print('the monthly payment for this loan is : %.2f ' % monthly_payment)
main()





#%.2f ---- what does it do is that it gonna cut the long float number to the two decimel places 
# syntax is --- print('the monthly payment for this loan is : %.2f ' % monthly_payment)




# change in output bcz of the %.2f -->
#PS C:\Users\rekha\OneDrive\Desktop\games> & C:/Users/rekha/AppData/Local/Microsoft/WindowsApps/python3.10.exe c:/Users/rekha/OneDrive/Desktop/games/Interest_rate_monthly_rate_calculator.py
#this is a monthly payment loan calculator 

#Input the loan amount :20000
#Input the annual interest rate :3
#enter amount of years :5
#the monthly payment for this loan is : 359.37 
#PS C:\Users\rekha\OneDrive\Desktop\games> 





# where previous one was 
# 
#Input the loan amount :20000
#Input the annual interest rate :3
#enter amount of years :5
#the monthly payment for this loan is :359.3738132812698