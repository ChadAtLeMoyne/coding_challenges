# Here's your change: a recursive way to figure out which coins to give for change
def add_coin(coin, coins):
    if coin in coins.keys():
        coins[coin] += 1
    else:
        coins[coin] = 1

def calc_change(charged, paid, coins):
    change = paid - charged
    if change <= 0:
        return

    if change >= 0.25:
        add_coin("Quarters", coins)
        calc_change(charged, paid-0.25, coins)
    elif change >= 0.10:
        add_coin("Dimes", coins)
        calc_change(charged, paid - 0.10, coins)
    elif change >= 0.05:
        add_coin("Nickels", coins)
        calc_change(charged, paid - 0.05, coins)
    else:
        add_coin("Pennies", coins)
        calc_change(charged, paid - 0.01, coins)
        
def main():
    charged = float(input("What is the total charged? $"))
    paid = float(input("What is the total paid? $"))
    coins = {}
    print(coins)
    calc_change(charged, paid, coins)
    print(coins)

if __name__ == '__main__':
    main()