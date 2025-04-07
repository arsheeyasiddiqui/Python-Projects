Menu = {'Pizza':40,
       'Pasta':50,
       'Burger':55, 
       'Sandwitch':70,
       'Coffee':90,
       'Tea' : 25}

print("Welcome to our Restaurant")
print("Pizza:Rs.40\nPasta:50\nBurger:55\nSandwitch:70\nCoffee:90")

Order_total=0

Item_1 = input("Enter the name of the item you want to order= ")

if Item_1 in Menu:
    Order_total += Menu[Item_1]
    print(f"Your item {Item_1} has been added to your order")

else:
    print(f"Ordered item {Item_1} is not in the menu")

Another_order= input("Do you want to order something else-Yes/No ")

if Another_order == "Yes":
    Item_2 = input("Enter the name of second dish: ")
    if Item_2 in Menu:
        Order_total += Menu[Item_2]
    else:
        print(f"Ordered item {Item_2} is not available")
print(f'Total amount of your order is:  {Order_total}')