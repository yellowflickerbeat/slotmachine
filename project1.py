import random
MAX_LINES=3
#Users can't bet more than 3 lines
MIN_BET=1
MAX_BET=100

count= {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}
def spin(rows, cols, count):
    all_symbols = []
    for symbol, count in all_symbols.items():
        for i in range(count):
            all_symbols.append(symbol)
    columns = [[], [], []]
    for col in range(rows):
        #initialize
        column = []


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

def no_of_lines():
    lines= input("Input numer of lines:")
    if lines.isdigit():
        lines= int(lines)
        if 1 =< lines =< MAX_LINES:
            break
        else:
            print("The number of lines should be valid.")
    else:
        print("Enter a number.")
    return lines

def bet_amt():
    bet_amt= int(input("Enter the betting amount per line:"))
    if MIN_BET =< bet_amt =< MAX_BET:
        break
    else:
        print("Enter the valid betting amount.")
    return bet_amt



def main():
    balance= entry()
    lines= no_of_lines()
    print(f"Your balance is {amt} and no of lines you are betting on:{lines}")
    bet=bet_amt()
    total= lines*bet
    if balance >= bet:
        print(f"Is your bet amount {bet}?")
        ans= input("Yes or No")
        if ans=="Yes":
            print(f"Your total amounts to {total}")
        else:
            print("Betting is off. Get out.")
    else:
        break
    

    