class User:
    def __init__(self, name, email_address):
        self.name = name
        self.email = email_address
        self.bank_account = 0
        
    def make_deposit(self, amount):
        print(f"Initial Balance = ${self.bank_account}")
        self.bank_account += amount
        print(f"Depositing ${amount} in to account. \n{self.name}'s New balance total is ${self.bank_account}")
        return self
        
    def make_withdrawal(self, amount):
        print(f"Initial Account Balance = ${self.bank_account}")
        self.bank_account -= amount
        print(f"Withdrawing ${amount} from Account. \n{self.name}'s New balance total is ${self.bank_account}")
        return self
    
    def transfer_money(self, other_user, amount):
        if(self.bank_account > amount):
            print(f"Transferring ${amount} from {self.name} to {other_user.name}")
            self.bank_account -= amount
            other_user.bank_account += amount
        return self
            

    def display_user_balance(self):
        print(f"{self.name}'s current account balance is ${self.bank_account}")
        return self
    



chris = User("Chris", "cmsl4y3r@gmail.com")
misty = User("Misty", "email@email.com")
chris.make_deposit(100).make_withdrawal(50).make_deposit(1000).make_deposit(500).make_withdrawal(100).display_user_balance()
misty.make_deposit(1000).make_deposit(500).make_withdrawal(50).make_withdrawal(100).make_deposit(200).make_withdrawal(100).transfer_money(chris, 100).display_user_balance()
chris.display_user_balance()