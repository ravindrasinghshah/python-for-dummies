age = 20
if age >= 18:
    message = "eligible"
else:
    message = "not eligible"
print(message)

# Different way of writing same code
message = "Eligible" if age >= 18 else "Not Eligible"
print(message)
