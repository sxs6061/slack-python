class BankAccount:
    
    def _init_(self):
        self.accounts = {}

    def _init_account(self, account_id):
        if account_id not in self.accounts:
            self.accounts[account_id] = {'balance': 0, 'transactions': []}
    
    def credit(self, account_id, timestamp, amount):
        self._init_account(account_id)
        self.accounts[account_id]['balance'] += amount
        self.accounts[account_id]['transactions'].append((timestamp, amount))

    def debit(self, account_id, timestamp, amount):
        self._init_account(account_id)
        if self.accounts[account_id]['balance'] >= amount:
            self.accounts[account_id]['balance'] -= amount
            self.accounts[account_id]['transactions'].append((timestamp, -amount))
            return True
        else:
            return False
    
    def balance_check(self, account_id):
        self._init_account(account_id)
        return self.accounts[account_id]['balance']
    
    def balance_change(self, account_id, start_timestamp, end_timestamp):
        self._init_account(account_id)
        transactions = self.accounts[account_id]['transactions']
        change = sum(amount for ts, amount in transactions if start_timestamp <= ts <= end_timestamp)
        return change
 
account = BankAccount()

account.credit(123, 100, 1000)
account.debit(123, 200, 500)
account.credit(123, 300, 200)

print(account.balance_check(123)) #700
print(account.balance_change(123, 100, 200)) #500


