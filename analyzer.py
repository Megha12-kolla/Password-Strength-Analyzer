print("🔐WELCOME TO PASSWORD STRENGTH ANALYZER!!")
password = input("Enter your Password: ")

upper_case = False
lower_case = False
digits = False
special_value = False


for char in password:
  if char.isupper():
    upper_case = True
  if char.islower():
    lower_case = True
  if char.isdigit():
    digits = True
  if char.isspace():
    special_value = True
  if not char.isalnum():
    special_value = True
  
print("Password Analysis: ")


print("Uppercase:", "✔" if upper_case else "✖")
print("Lowercase:", "✔" if lower_case else "✖")
print("Digit:", "✔" if digits else "✖")
print("Special Character:", "✔" if special_value else "✖")

if len(password) >= 8:
  print("✔Strong Password", ", The password is Greater than or equal to Eight number of Characters")
else:
  print("✖ The Password isn't Strong", ",Password should be at least 8 characters to make the it strong enough")