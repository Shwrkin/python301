from fileinput import close


class BankUser():
    def __init__(self, name):
        self.name = name
        self.file = f'{name}.txt'
        # Creating the bank file of the current user
        try:
            open(f'{name}.txt', 'x').close()
        except FileExistsError:
            pass

    # Makes the user Choose which action to do and with how much money
    def bankAction(self):
        action = ''
        amount = 0

        while not action:
            action = input('Withdrawal or Deposit? (w/d) ').lower()

            if action == 'w':
                while not amount:
                    amount = float(input('How much would you like to withdraw? '))
                    if type(amount) is not float or amount <= 0:
                        print('Please enter a valid number')
                        amount = 0
                    else:
                        with open(self.file, 'a') as file:
                            file.write(f'-{amount}\n')

            elif action == 'd':
                while not amount:
                    amount = float(input('How much would you like to deposit? '))
                    if type(amount) is not float or amount <= 0:
                        print('Please enter a valid number')
                        amount = 0
                    else:
                        with open(self.file, 'a') as file:
                            file.write(f'+{amount}\n')

            else:
                print('Please choose one of the options')
                action = ''
        
        with open(self.file, 'r') as f:
            print(f.read())


sagi = BankUser('Sagi')
while True:
    sagi.bankAction()