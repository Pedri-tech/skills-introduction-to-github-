menu = {"pizza": 3.00,
        "nachos": 4.50,
        "fries": 2.50,
        "chips": 1.00,
        "soda": 3.00
        }
cart = []
total = 0

for key, value in menu.items():
    print(f"{key:10}: ${value:.2f}")