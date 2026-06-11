account = {
  "owner": "Tom",
  "account": "4545",
  "balance": 100,
  "is_active": True,
  "transactions": []
}

print(f"Accessing account #: {account["account"]}")
print(f"Welcome, {account["owner"]}")
print(f"Current balance: ${account["balance"]:.2f}")

def deposit(current_balance, amount):
  message = f"depositing {amount} into your account."
  account["transactions"].append(message)
  # print(message)
  return current_balance + amount

def withdraw(current_balance, amount):
  if amount < 0:
    print("Invalid amount.")
    return current_balance
  elif amount <= current_balance:
    message = f"withdrawing {amount} from your account."
    account["transactions"].append(message)
    # print(message)

    return current_balance - amount
  else:
    print("Insufficient funds.")
    return current_balance

deposit_amount = float(input("How much do you want to deposit? "))

withdraw_amount = float(input("How much do you want to withdraw? "))


account["balance"] = deposit(account["balance"], deposit_amount)


print(f"Current balance: ${account["balance"]:.2f}")

account["balance"] = withdraw(account["balance"], withdraw_amount)

print(f"Current balance: ${account["balance"]:.2f}")

def print_transactions(account):
  print("Transactions:\n")
  for transaction in account["transactions"]:
    print("\t"+transaction)

print_transactions(account)
