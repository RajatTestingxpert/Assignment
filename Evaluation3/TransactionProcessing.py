class Transaction_Processing:
    def __init__(self):
        self.transactions =[]
        self.user=[]
        self.balancee=0
        

    def add_money(self,id,user_id,amount,balance=0):
        if amount>0:



            
            self.id = id
            self.user_id = user_id
            self.amount=amount
            self.type = "credit"
            self.balancee +=amount


            self.user.append({'id':id,'user_id':user_id,'amount':amount,'type':'credit'})

            self.transactions.append({'id':id,'user_id':user_id,'amount':amount,'type':'credit'})
            
        else:
            print("Invalid amount")

    def withdraw_money(self,id,user_id,amount,balance=0):

        if amount>0:
            if amount>self.balancee:
                print("Less money")

            else:
                self.balancee -=amount
                self.user.append({user_id:{'id':id,'user_id':user_id,'amount':amount,'type':'debit'}})
                self.transactions.append({'id':id,'user_id':user_id,'amount':amount,'type':'debit'})

        else:
            print("Invalid amount")

    def __str__(self):
        res =f"Account Information : \n Account :{self.user_id} \n Balance:{self.balancee} \n Transactions :{self.transactions}"
        return res
    
    @property
    def total_transactions(self):
        return self.transactions
    

    def filter_transactions(self,min_amount=0,txn_type=None):
        new_transaction=[]

        for trans in self.transactions:
            if trans['amount']>=min_amount and trans['type']== txn_type:
                new_transaction.append(trans)
        
        return new_transaction
    
    def calculate_user_balance(self,transactions):
        total=0
        for trans in transactions:
            if trans['type']=='credit':
                total +=trans['amount']

            else:
                 total -=trans['amount']

        return total
    
    def transaction_repo(self,transactions):
        total_trans = len(transactions)

       
        total1=0
      
        for trans in transactions:
            if trans['type']=='credit':
                total1 +=trans['amount']

        total_credit=total1

        total2=0
        for trans in transactions:
            if trans['type']=='debit':
                total2 +=trans['amount']

        total_debit=total2

        net_flow=total1-total2

        # highest_transaction1 =sorted(transactions.items())
        # highest_transaction=highest_transaction1[0]
        
        return f"total_trans :{total_trans}\n total_credit :{total_credit}\n total_debit : {total_debit} net_flow {net_flow} \n highest_transaction :"






transaction = Transaction_Processing()

transaction.add_money('T1','U1',500)
transaction.add_money('T2','U1',2000)

print(transaction)
transaction.withdraw_money('T3','U1',2)
transaction.withdraw_money('T4','U1',5)

filter =transaction.filter_transactions(500,'credit')
print(filter)

total_trans = transaction.total_transactions

user_balance =transaction.calculate_user_balance(total_trans)
print(user_balance)

trans_repo =transaction.transaction_repo(total_trans)
print(trans_repo)




