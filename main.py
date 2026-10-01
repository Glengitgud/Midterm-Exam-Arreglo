from os import write

#push github
def interface():
    print("========================================")
    print("     SALES RECORD MANAGEMENT SYSTEM     ")
    print("========================================")
    print("1. Add Sale Record")
    print("2. View All Records & Summary Statistics")
    print("3. Clear All Sales Data")
    print("4. Exit System")
    print("========================================")

def userInput():
    try:
        salesInput = input("\nSelect an option 1-4: ")
        if salesInput == "1":
            salesRecord()
        elif salesInput == "2":
            viewRecords()
        elif salesInput == "3":
            clearData()
        elif salesInput == "4":
            exitSystem()
        else:
            print('\nPlease enter valid number.')
            interface()
            userInput()
    except ValueError:
        print('\nPlease enter valid number.')
        interface()
        userInput()

def salesRecord():

    itemInput = input("\nEnter item name: ")
    quantityInput = input("Enter quantity: ")
    priceInput = input("Enter price: ")

    quantityInput = int(quantityInput)
    priceInput = float(priceInput)

    open('sales_log.txt')
    write(itemInput)
    write(quantityInput)
    write(priceInput)


def viewRecords():
    read = open('sales_log.txt')
    for line in read.readlines():
        print(line)
def clearData():
    print("\nClearing All Records")
def exitSystem():
    print("\nThank you for using the Sales Record Management System")
    exit()

interface()
userInput()