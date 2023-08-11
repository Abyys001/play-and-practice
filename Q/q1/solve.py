# venv/scripts/activate

"""

"""

saraSMS = input("""
    sara SMS is:
                
""")

def Payment_calculation(SMS):
    if len(saraSMS) > 24:
        price = len(saraSMS) // 24
        price *= 274
        price += 100
    else: 
        price = 100
    price /= 10

    return price


if __name__ == "__main__":
    print(Payment_calculation(saraSMS))

