import logging
from functools import wraps



logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)

logger = logging.getLogger(__name__)



def track_function(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            result = func(*args, **kwargs)

            logger.info(
                "Function '%s' executed successfully",
                func.__name__
            )
            return result

        except:
            logger.exception(
                "Function '%s' failed due to insufficient balance ",
                func.__name__
            )
            raise

    return wrapper


class BankAccount:
    def __init__(self,account_number,initial_balance=0):
        self.account_number = account_number
        self.initial_balance = initial_balance
        self.transaction_history=[]

    def deposit(self,amount):
        if amount>0:
            self.initial_balance+=amount
            self.transaction_history.append(amount)
        else:
            return f"Amount must be positive"
        
    @track_function    
    def withdraw(self,amount):
        if amount<self.initial_balance:
            self.initial_balance=self.initial_balance-amount
            self.transaction_history.append(-amount)
        else:
            raise 

    def get_balance(self):
        return self.initial_balance
    
    def get_transaction_history(self):
        return f"Transaction history is :{self.transaction_history}"

    def __str__(self):
        return f"Account Number :{self.account_number} \n Balance :{self.initial_balance}"
    

account =BankAccount("ACC001",1000)

account.deposit(1000)
print(account)
print()
print()

account.withdraw(200)
print(account)
print()
print()

print(account)
print(account.get_transaction_history)
print()
print()



try:
    account.withdraw(10)
except:
    print("Error :")

print()
print()


try:
    account.withdraw(20000)

except :
    print("Error :")







