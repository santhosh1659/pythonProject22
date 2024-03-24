import random

# Define Characters
characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"

# Generate Captcha
captcha = ''.join(random.choice(characters) for _ in range(5))

# Print Captcha
print("Generated Captcha:", captcha)