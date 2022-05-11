import string
import jsonManager


def create_seat(row, column):
    """
    Create a seat.
    """
    if row <= 4:
        price = 80
    elif row <= 10:
        price = 50
    else:
        price = 25

    seat = {"row": row, "column": column, "status": "a", "price": price}

    return seat


def create_seatsDict(rows, columns):
    """
    Create a dictionary of seats.
    """
    seats_plan = {}

    numOfSeats = (rows) * (columns)

    curRow = 0
    curColumn = 0

    for i in range(numOfSeats):
        if curRow < rows:
            if curColumn < columns:
                seats_plan[i] = create_seat(curRow, curColumn)
                curColumn += 1
            else:
                curRow += 1
                curColumn = 0
                seats_plan[i] = create_seat(curRow, curColumn)
                curColumn += 1


    save_seats(seats_plan)

    return seats_plan

def save_seats(seats_plan):
    """
    Save the seats.
    """

    jsonManager.save_json("seats.json", seats_plan)


def print_seats(seats_plan,rows,columns):
    """
    Print the seats.
    """

    curRow = 0;
    curCol = 0;
    print("   " + (string.ascii_uppercase[:columns]))
    
    displayString = " 0 "
    for i in range(len(seats_plan)):
        # print(i)

        num = str(i)
        if curRow < rows: 
            if curCol < columns-1:
                displayString += seats_plan[num]["status"]
                
                curCol += 1
            else:
                displayString += seats_plan[num]["status"]

                curRow += 1
                curCol = 0
                
                print(displayString)
                if curRow <= 9:
                    displayString = " " + str(curRow) + " "
                else:
                    displayString = str(curRow) + " "


def print_seats_status(seats_plan):
    """
    Print the seats status.
    """

    for i in range(len(seats_plan)):
        print(seats_plan[i]["status"])


def seatManager():
    """
    Main function.
    """

    rows = int(input("Enter the number of rows: "))
    columns = int(input("Enter the number of columns: "))

    seats_plan = create_seatsDict(rows, columns)



    print(seats_plan)
    print_seats(seats_plan,rows,columns)




def get_seats():
    """
    Get the seats.
    """

    seats_plan = jsonManager.open_json("seats.json")

    return seats_plan
