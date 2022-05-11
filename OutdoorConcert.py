# import userdata.json
# import seats.json
# import purchases.json

import email
from select import select
import userManager as um
import jsonManager as jm
import seatManager as sm


def Menu():
    print()
    print("---------------------------------------")
    print("|        Welcome to the Venue         |")
    print("---------------------------------------")
    print("[V] View availabe seats")
    print("[B] Buy a seat")
    print("[C] Cancel seat")
    print("[S] Search for a friend")
    print("[D] Display all purchases")
    print("[Q] Quit")
    print("---------------------------------------")


def available_seats(seat_plan, start, end):
    """
    Print the available seats.
    """
    for i in range(start, end):
        if seat_plan[str(i)]["status"] == "X":
            return False
    return True


def purchase_seat(seat_plan, maxRows, maxColumns,user,name):
    """
    Purchase a seat.
    """

    selction = ""

    amountOfTickets = int(input("Enter the number of tickets[ Has to less than or equal to 26]: "))

    if amountOfTickets == 0:
        return seat_plan, user

    while selction != "Q":
        sm.print_seats(seat_plan, maxRows, maxColumns)



        row = int(input("Enter the row: "))



        # columnStart = ""
        # columnEnd = ""

        if amountOfTickets == 1:
            columnStart = int(ord(input("Enter the column: ")) - 97)
            columnEnd = columnStart
        else:
            do = True
            while do == True:
                columnStart = int(ord(input("Enter the intial column: ")) - 97)
                columnEnd = int(ord(input("Enter the final column: ")) - 97)

                if columnStart > columnEnd:
                    print("The final column must be greater than the initial column.")
                    do = True
                if columnEnd - columnStart + 1 != amountOfTickets:
                    print("The number of tickets must match the number of columns.")
                    do = True
                else:
                    do = False

        if available_seats(seat_plan, row, columnStart) and (row % 2 == 0 or row == 0):
            for i in range(columnStart, columnEnd+1):
                seat_plan[str(row * 26 + i)]["status"] = "X"
                selction = "Q"
        else:
            print("At least one seat not available")
            selction = input("Enter Q to quit or any other key to continue: ")

        price = amountOfTickets * seat_plan[str(row * 26 + columnStart)]["price"]

    receipt(price)


    user["Profit"] = user["Profit"] + price

    user[str(name)] = {"seat": {"row": row, "columnStart": columnStart, "columnEnd": columnEnd}, "orderCost": (price*1.0725) + 5.00}




    return seat_plan,user


def receipt(price):
    """
    Print the receipt.
    """
    print("---------------------------------------")
    print("|        Receipt for your purchase      |")
    print("---------------------------------------")
    print("| Price: " + "$" + str(price))
    print("| Tax: " + "$" + str(price * 0.0725))
    print("| Fee: " + "$" + str(5))
    print("| Total: " + "$" + str((price * 1.0725) + 5.00))
    print("---------------------------------------")


def printAllPurchases(user):
    """
    Print the purchases.
    """
    print("---------------------------------------")
    print("|        Purchases                    |")
    print("---------------------------------------")
    for key in user:
        if key != "Profit":
            print("| Name: " + key)
            print("| Seat: " + str(user[key]["seat"]["row"]) + " " + str(user[key]["seat"]["columnStart"]) + "-" + str(user[key]["seat"]["columnEnd"]))
            print("| Price: " + "$" + str(user[key]["orderCost"]))
            print("---------------------------------------")
        print("---------------------------------------")
    print("Total: " + "$" + str(user["Profit"]))



def search_friend(user):
    """
    Search for a friend.
    """
    print("---------------------------------------")
    print("|        Search for a friend          |")
    print("---------------------------------------")
    name = input("Enter the name: ")
    if name in user:
        print("| Name: " + name)
        print("| Seat: " + str(user[name]["seat"]["row"]) + " " + str(user[name]["seat"]["columnStart"]) + "-" + str(user[name]["seat"]["columnEnd"]))
        print("---------------------------------------")
    else:
        print("| No friend found with that name.")
        print("---------------------------------------")


def cancel_purchase(user,seat_plan):
    """
    Cancel a purchase.
    """
    print("---------------------------------------")
    print("|        Cancel a purchase            |")
    print("---------------------------------------")
    name = input("Enter your name: ")
    if name in user:
        print("| Name: " + name)
        print("| Seat: " + str(user[name]["seat"]["row"]) + " " + str(user[name]["seat"]["columnStart"]) + "-" + str(user[name]["seat"]["columnEnd"]))
        print("---------------------------------------")
        do = True
        while do == True:
            choice = input("Are you sure you want to cancel your purchase? (Y/N): ")
            choice = choice.upper()
            if choice == "Y":
                for i in range(user[name]["seat"]["columnStart"], user[name]["seat"]["columnEnd"]):
                    seat_plan[str(user[name]["seat"]["row"] * 26 + i)]["status"] = "a"
                    user["Profit"] = user["Profit"] - ((user[name]["orderCost"]-5.00)/1.0725)
                del user[name]
                do = False
            elif choice == "N":
                do = False
            else:
                print("Invalid input.")
                do = True


def main():
    maxRows = int(20)
    maxColumns = int(26)

    user = jm.open_json("user.json")
    seat_plan = jm.open_json("seats.json")

    choice = ""

    while choice != "Q":
        Menu()
        choice = input("Enter your choice: ")
        choice = choice.upper()
        if choice == "V":
            sm.print_seats(seat_plan, maxRows, maxColumns)
        if choice == "B":
            name = input("Enter your name: ")
            email = input("Enter your email: ")

            newData = purchase_seat(seat_plan, maxRows, maxColumns,user,name)

            seat_plan = newData[0]

            

            user =  newData[1]

            # print(user)

        if choice == "D":
            printAllPurchases(user)
        if choice == "S":
            search_friend(user)
        if choice == "C":
            cancel_purchase(user,seat_plan)



    


main()
