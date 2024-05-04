def entry():
    amt = input("Enter the amount to be deposited:")
    '''Normally, I would've just written:
    amt=int(input(/'Enter the amount:'/))
    However here we want to promt the user to enter a number above zero,
     instead of just throwing an error'''
    if amt.isdigit():
        amt= int(amt)
        if amt > 0:
            break
        else:
            print("The amount should be more than zero.")
    else:
        print("Error.Enter a number.")
    return amt
