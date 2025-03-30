menu = {
    "pizza": 3.00,
    "nachos": 4.50,
    "popcorn": 6.00,
    "fries": 2.50,
    "chips": 1.00,
    "pretzel": 3.50,
    "soda": 3.00,
    "lemonade": 4.25
}

cart = []
nada = []  # List to store unavailable items
total = 0


print("------Menu------")
for key, value in menu.items():
    print(f"{key:10}: ${value:.2f}")
print("-----------------")


while True:
    food = input("Select an item? (q to quit): ").lower()
    
    if food == "q":
        break
    elif food in menu:
        cart.append(food)
    else:
        nada.append(food)  # Store unavailable items


if cart:
    print("\nYou Bought:", "  ".join(cart))


if nada:
    print("\nSorry, we don't have:", "  ".join(nada))


for food in cart:
    total += menu.get(food)

print(f"\nTotal is: ${total:.2f}")
input("\nWelcome! Press Enter to quit.")
