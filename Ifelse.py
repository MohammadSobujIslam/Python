# python If else condition some different
# if are same syntex but else if equal elif
"""
is_hot=False
is_cold=False
if is_hot:
    print("It's a hot day")
    print('Drink plenty of water')
elif is_cold:
    print("It's is cold day")
    print('Wear warm clothes')
else:
    #hot=6
    print("It's a lovely day")



print('Enjoy your day')

price=1000000
good_credit=True
if good_credit:
    down_payment=0.1*price
    print(f'down_payment is= {down_payment}'   )

else:
    down_payment=0.2*price
    print(f"down_payment is=  {down_payment}" )

temperature=float(input('Enter your number? '))

if temperature>30:
    print("It's hot day")
elif temperature<10:
    print("It's a cold day")
else:
     print("It's neither hot nor cold")

name=input("Enter your name ")
name_len=len(name)
if name_len<3:
    print("at least 3 characters")
elif name_len>50:
    print("maximum of 50 characters")
else:
    print('name looks good!')
"""
weight=float(input("Enter your weight "))
convert=input('(L)bs or (K)g:')
if convert.upper()=="L":
    kilo = weight * 0.45
    print(f"You are {kilo} kilos")

#elif conver=='k' or conver=='K':

else:
 #   print("it's any one to convert")
    pound = weight / 0.45
    print(f"Your are  {pound} pound")


