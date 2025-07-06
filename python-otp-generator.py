import random

def generate_otp(length=6):
    otp = ""
    for _ in range(length):
        otp += str(random.randint(0, 9))
    return otp

# Generate and display OTP
otp_code = generate_otp()
print("Your OTP is:", otp_code)
