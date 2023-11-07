# format specifiers = { value : flags } format a value on what flgs are inserted .


#                            flags are inserted 
# .(number )f= round to that many decimal places (fixed point )
# :(number )= allocate that many spaces 
# :03 = allocate and zero pad that many spaces 
# :< = left justify 
# :>= right justify
# from now on we will call thaese > as left angle and  < as right angle .
# :^ =center align 
# :+= use a pluys sign to indicate positive value 
# := = place sign to leftmost position 
#  :  = insert a space before positivenumbers 
# ;, = comma seperator 


price1 = 3.123
price2 = -9867.34
price3 = 12.345

print(f"Price 1 is {price1:.2f}")# .2f here .2 is telling 2 numbers after dot and f means 
#floating point number #adding decimal point precision # here we are considering  prices as values
# and after the :(colon) we are considering as flags 
print(f"Price 2 is {price2:.2f}")# value:flags 
print(f"Price 3 is {price3:.2f}")
# Price 1 is 3.12
# Price 2 is -9867.34
# Price 3 is 12.35


# to aalocate spaces to display a value 
# after the colon add some number 
print(f"Price 1 is {price1:10}")
print(f"Price 2 is {price2:10}")# value:flags 
print(f"Price 3 is {price3:10}")
 




# to left justify a value you will use a left angle value 
print(f"Price 1 is {price1:>10}")
print(f"Price 2 is {price2:>10}")# value:flags 
print(f"Price 3 is {price3:>10}")



# similarly to right justify the values 
print(f"Price 1 is {price1:<10}")
print(f"Price 2 is {price2:<10}")# value:flags 
print(f"Price 3 is {price3:<10}")


print(f"Price 1 is {price1:+}")
print(f"Price 2 is {price2:+}")# value:flags 
print(f"Price 3 is {price3:+}")






print(f"Price 1 is {price1:,}")
print(f"Price 2 is {price2:,}")# value:flags 
print(f"Price 3 is {price3:,}")






print(f"Price 1 is {price1:,.2f}")
print(f"Price 2 is {price2:,.2f}")# value:flags 
print(f"Price 3 is {price3:,.2f}")



# combination of flags 
print(f"Price 1 is {price1:+,.2f}")
print(f"Price 2 is {price2:+,.2f}")# value:flags 
print(f"Price 3 is {price3:+,.2f}")



