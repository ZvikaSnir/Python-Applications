class Account:
    def __init__(self,filepath):
        self.filepath=filepath
        with open(filepath,'r') as file:
            self.balance=int(file.read())

    def withdraw(self,amount):
        self.balance-=amount

    def deposit(self,amount):
        self.balance+=amount

    def commit(self):
        with open(self.filepath,'w') as file:
            file.write(str(self.balance))



class Checking(Account):
    """This class generates checking account objects"""

    type="checking"
    def __init__(self,filepath,fee):
        Account.__init__(self,filepath)
        self.fee=fee

    def transfer(self,amount):
        self.balance-=amount - self.fee


checking=Checking("jack.txt",1)
print(checking.balance)
checking.transfer(110)
checking.commit()
print(checking.type)

checking2=Checking("jack.txt",1)
print(checking2.balance)
checking2.transfer(110)
checking2.commit()
print(checking2.type)
