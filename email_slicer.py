# what an email slicer is that a program that takes a particular email and slices it into 
# a particular  name and domain and we also gonna slice it into username , domain , extension -- @gmail.com ,.com


# collect email from the user 
# slice/split the email using the @ 
# hellocodewithtomi.com -- the first part as the user name  , the second part as the domain name 
# split domain using . .
def main():
    print('welcome to the email slicer')
    print('')

    email_input=input('input your eamil address: ')
    (username,domain)=email_input.split('@')
    (domain,extension)=domain.split('.')

    print('username :',username)
    print('domain :',domain)
    print('extension :', extension)
main()

# output
# input your eamil address: aloke@pramanik.com
#username : aloke
#domain : pramanik
#extension : com