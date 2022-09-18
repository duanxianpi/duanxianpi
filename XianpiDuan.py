#DFIC QUANT GROUP CODING ASSESSMENT

#Follow the instructions below carefully

# Email your submission named YourName.py to colclour@mcmaster.ca
# You are going to be creating a class which mimics a bank account.
# A bank account contains someones name, their age, and all of their sub accounts
# sub accounts can be named anything, and will each have their own values
# e.g. you can have a "savings" account with $150, "chequing" with $20, "someaccount1231234" with $1, etc. 
# There will be functions to print this information for the user 

#Use programming best practices such as good variable names, using functions/methods instead of repeating code, commenting
#Write a test case for the updateBalance and addAccount method, which uses the printSummary method to show they are working


#Example test case:
#testAccount = BankAccount("John Doe", 19,  .. ..) 
#testAccount.printSummary()
#testAccount.deposit("savings", 10)
#testAccount.withdraw("savings", 5)
#testAccount.addSubAccount("chequing", 1)
#testAccount.printSummary()


#FORMAL REQUIREMENTS
#Write a class called "BankAccount" which has the following properties:

    # the bank account must have a name and age attached to it
    # An account can have multiple (unlimited) sub accounts
	    # Hint: use a dictionary

    # the inital instance of the class should contain a name, an age, and one account: "savings" with $0

    # The methods:
        # __init__
        # getIdentity (prints name and age)
        # getBalances (prints names and balances of all sub accounts)
        # addSubAccount  (takes sub account name and balance as input)
        # deposit (takes sub account name and the amount to deposit)
        # withdraw (takes sub account name and the amount to withdraw)
        # printSummary (prints name of the bank (make it whatever you want), the user, the sub accounts and their balances)

class BankAccount:

    def __init__(self,name,age):
        """Init a bank acount with client's name and age. 
        There will be a deafult sub account called "savings" with $0 inside.

        Args:
            name: the client's name
            age: the client's age
        """
        self.clientName = name
        self.clientAge = age
        self.subAccountsDict = {"savings":0}

    def getIdentity(self):
        """Print client's name and age.
        """

        print("--------------------------------")
        print("Client's Name:",self.clientName)
        print("Client's Age:",self.clientAge)
        return

    def getBalances(self):
        """Prints Client's names and balances of all sub accounts
        """
        
        print("--------------------------------")
        print("Sub Accounts:")
        for key in self.subAccountsDict.keys():
            print("{}: ${}".format(key,self.subAccountsDict[key]))
        return

    def addSubAccount(self,accountName,accountBalance):
        """Takes sub account name and balance as input and create a new bank account.

        Args:
            accountName: the name of sub account
            accountBalance: the money in this sub account
        """

        self.subAccountsDict[accountName] = accountBalance
        return

    # Deposite a specified amount of money into a specified bank account
    def deposit(self,accountName,money):
        """Deposite a specified amount of money into a specified bank account

        Args:
            accountName: the name of account which you wanted the money to be deposited into.
            money: the amount of money.

        Raises:
            KeyError: An error when try to deposit into a non-existent account.
        """

        try:
            self.subAccountsDict[accountName] += money
        except:
            raise Exception("Sorry no such account!")

        return
    
    def withdraw(self,accountName,money):
        """Withdraw a specified amount of money from a specified bank account

        Args:
            accountName: the name of account which you wanted the money to be withdrawed from.
            money: the amount of money.

        Raises:
            KeyError: An error when try to withdraw from a non-existent account.
        """

        try:
            self.subAccountsDict[accountName] -= money
        except:
            raise Exception("Sorry no such account!")
        
        return

    def printSummary(self):
        """Prints name of the bank, user information and the sub accounts and their balances
        """
        print("================================")
        print("Bank Name: Royal Bank of Canada")
        self.getIdentity()
        self.getBalances()
        return

if __name__ == "__main__":
    # testing the updateBalance and addAccount method.
    testAccount = BankAccount("John Doe", 19) 
    testAccount.printSummary()
    testAccount.deposit("savings", 1000)
    testAccount.withdraw("savings", 850)
    testAccount.addSubAccount("chequing", 2000)
    print("")
    testAccount.printSummary()