
# Lab 28: ATM

Let's ATM class containing two attributes: a balance and an interest rate. A newly created account will have a balance of 0 and an interest rate of 0.1%.

- `check_balance()` returns the account balance
- `deposit(amount)` deposits the given amount in the account
- `check_withdrawal(amount)` returns true if the withdrawn amount won't put the account in the negative
- `withdraw(amount)` withdraws the amount from the account and returns it
- `calc_interest()` returns the amount of interest calculated on the account

## Version 2
Have the ATM maintain a list of transactions. Every time the user makes a deposit or withdrawal, add a string to a list saying 'user deposited $15' or 'user withdrew $15'. Add a new function to your class for printing out the list of transactions.

## Version 3
Allow the user to enter commands
```
> what would you like to do (deposit, withdraw, check balance, history)?
> deposit
> how much would you like to deposit?
> $5
> what would you like to do (deposit, withdraw, check balance)?
> check balance
> balance: $5
```