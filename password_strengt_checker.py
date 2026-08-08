print("Password Strength Checker")
password=input("Enter your password:")
length= len(password)
print("Passwordlength:", length)
has_uppercase = any(char.isupper() for char in password)
print("contains uppercase:",has_uppercase)
has_number= any(char.isdigit()for char in password)
print("contains number:",has_number)
has_symbol = any(not char.isalnum() for char in password)
print("contains symbol:",has_symbol)
score = 0

if length >= 8:
    score += 1

if has_uppercase:
    score += 1

if has_number:
    score += 1

if has_symbol:
    score += 1
print("Password score:", score)
if length >= 8:
    validity = "Valid"
else:
    validity = "Invalid"

print("Password validity:", validity)
if score <= 1:
    strength = "Weak"
elif score <= 3:
    strength = "Medium"
else:
    strength = "Strong"

print("Password strength:", strength)