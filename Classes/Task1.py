class Account:
    def __init__(self, number, password, balance):
        self.__accountNumber = number
        self.__accountPassword = password
        self.__accountBalance = balance

    def getNumber(self):
        return self.__accountNumber

    def checkPassword(self, password):
        if password == self.__accountPassword:
            return True
        else:
            return False

    def getBalance(self):
        return self.__accountBalance

    def setBalance(self, newBalance):
        self.__accountBalance = newBalance

class Bank:
    def __init__(self):
        self.__accounts = []
        self.__latestAccount = -1

    def login(self):
        AccNumb = int(input("Enter your Account number: "))
        for account in self.__accounts:
            if AccNumb == account.getNumber():
                AccPassword = input("Enter your password: ")
                while not account.checkPassword(AccPassword):
                    AccPassword = input("Incorrect Password. Re-enter (input '-1' to quit): ")
                    if AccPassword == -1:
                        return -1
                return AccNumb
        
        print("Account not found.\n")
        return -1

    def deposit(self, number):
        for account in self.__accounts:
            if account.getNumber() == number:
                amount = int(input("How much to deposit into your account: £"))
                newAmount = account.getBalance() + amount
                account.setBalance(newAmount)

    def withdraw(self, number):
        for account in self.__accounts:
            if account.getNumber() == number:
                amount = int(input("How much to withdraw from your account: £"))
                newAmount = account.getBalance() - amount
                account.setBalance(newAmount)

    def checkBalance(self, number):
        for account in self.__accounts:
            if account.getNumber() == number:
                print("\nYour balance is: £"+str(account.getBalance())+"\n")
                return None

    def addAccount(self):
        AccNumb = len(self.__accounts)+1
        AccPassword = input(f"Enter a password for your account number {AccNumb}: ")
        AccBalance = 0
        self.__accounts.append(Account(AccNumb, AccPassword, AccBalance))

def main():
    bank = Bank()
    loggedIn = False
    quitting = False
    while not loggedIn and not quitting:
        response = input("\nDo you have an account? (y/n/quit): ")
        if response == "y":
            account = bank.login()
            if account != -1:
                loggedIn = True
        elif response == "n":
            bank.addAccount()
        elif response == "quit":
            quitting = True

    while not quitting:
        option = input("\nMenu: \n 1). Check your balance \n 2). Deposit money \n 3). Withdraw the money \n 4). To exit \nChoice: ")
        if option == "1":
            bank.checkBalance(account)
        elif option == "2":
            bank.deposit(account)
            bank.checkBalance(account)
        elif option == "3":
            bank.withdraw(account)
            bank.checkBalance(account)
        elif option == "4":
            quitting = True
        else:
            print("Invaild option selected")


if __name__ == '__main__':
    main()
