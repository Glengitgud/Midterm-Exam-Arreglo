import os

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
    while True:
        interface()
        salesInput = input("\nSelect an option 1-4: ").strip()
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

def salesRecord():
    print("Adding Sale Record")
    itemInput = input("\nEnter item name: ").strip()

    while True:
        try:
            quantityInput =int(input("Enter quantity: "))
            break

        except ValueError:
            print('\nPlease enter valid number.')
            salesRecord()

    while True:
        try:
            priceInput = float(input("Enter price: "))
            break
        except ValueError:
            print('\nPlease enter valid number.')
            salesRecord()

    quantityInput = int(quantityInput)
    priceInput = float(priceInput)
    totalAmount = quantityInput * priceInput

    with open('sales_log.txt') as file:
        file.write(f"Item: {itemInput} | Qty: {quantityInput} | Price: {priceInput} | Total: {totalAmount:.2f}\n")

    print(f"\n Successfully added record! Total amount: {totalAmount:.2f}\n")

def viewRecords():
    print("- Sales Record -")
    try:
        with open('sales.log.txt')as file:
            fileRead = file.read()
            if fileRead.strip():
                print(fileRead)
            else:
                print('Sales log is empty.')
    except FileNotFoundError:
        print('\nNo sales record found yet.')
def clearData():
    print("\nClearing All Records")
def exitSystem():
    print("\nThank you for using the Sales Record Management System")
    exit()

userInput()