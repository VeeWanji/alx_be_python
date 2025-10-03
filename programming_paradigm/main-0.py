from bank_account import BankAccount
def main():
    account = BankAccount(100)
    account.deposit(67)
    print("Expected: Deposited: $67")
    account.display_balance()  
    if account.withdraw(50):
        print("Expected: Withdrew: $50")
    else:
        print("Unexpected: Withdrawal failed")
    account.display_balance() 
    if account.withdraw(300):
        print("Unexpected: Withdrew: $300")
    else:
        print("Expected: Insufficient funds.")
    account.display_balance()
    print("Final Check: $250")
    account.display_balance(250)

if __name__ == "__main__":
    main()
    