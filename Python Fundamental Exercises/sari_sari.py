#Sari-Sari Store Logic
def input_validation(prompt):
  try:
    price = input(input(prompt))
    return price
  except TypeError:
    return print("Please input number only.")


print("Enter the following information")
print("--------------------------------")
item_name = input("Enter item name: ")
price = input_validation("Enter item price(PHP): ")
print(price)


