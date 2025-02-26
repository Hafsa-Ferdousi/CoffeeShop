menu={
    'Pizza':149,
    'Meat Box':120,
    'Tea':60,
    'Coffe':99,
    'Combo Offer':299


}

print("Welcome to BMukto Coffee Shop")

print("Menu:")
for item,price in menu.items():
    print(f"{item}: {price} BDT")

order_total=0
item_1= input("Enter the name of item of your order= ")
if item_1 in menu:
    order_total+=menu[item_1]
    print(f"Your item {item_1} has been added to your order")

else:
    print("Please order something else that we can serve you")


another_order=input("DO You want to add another item?(Yes/No)")

if another_order =="Yes":
    item_2 = input("Enter the name of second item= ")
    if item_2 in menu:
       order_total += menu[item_2]
       print(f"Item {item_2} has been added to order")
    else:
        print(f"Ordered item {item_2}is not available")

print(f"Total amount to pay {order_total} Taka")

