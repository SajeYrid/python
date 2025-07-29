dollar = int(input("dollah?"))
false_cent = int(input("cent?"))
amount = int(input("amount?"))
cent = false_cent / 100
number = (dollar + cent)
total = number * amount
response = "The total cost of {} cookies is {}. "
print(response.format(amount, total))
