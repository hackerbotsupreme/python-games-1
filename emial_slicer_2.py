def main():
    print('welcome to the email slicer')
    print('')

    email_input=input('input your eamil address: ')
    (username,domain)=email_input.split('@')
    (domain,extension)=domain.split('.')

    print('username :',username)
    print('domain :',domain)
    print('extension :', extension)
    
while True:
    main()
# the only difference is while True line 



# only one flaw of this code is this will continue taking inputs and never stop 
