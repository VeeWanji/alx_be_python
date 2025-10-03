from bank_account import BankAccount
def main():
    account = BankAccount(100)
    account.deposit(50)
    print("Expected: Deposited: $50")
    account.display_balance() 
    if account.withdraw(20):
        print("Expected: Withdrew: $20")
    else:
        print("Unexpected: Withdrawal failed")
    account.display_balance() 
    if account.withdraw(200):
        print("Unexpected: Withdrew: $200")
    else:
        print("Expected: Insufficient funds.")
    account.display_balance()
    print("Final Check:")
    account.display_balance(250)

if __name__ == "__main__":
    main()