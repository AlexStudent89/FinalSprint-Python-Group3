# Program Name: Final Sprint - HAB Taxi Services
# Program Description: A program designed to service HAB Taxi Services, with calculations and reports
# Written By: Group 3
# Written On: August 4th - August 18, 2023

# imports
import csv
import datetime


# Functions
def newEmployee():

    f = open('defaults.dat', 'r')

    NEXT_TRANSACTION_NUM = int(f.readline())
    NEXT_DRIVER_NUM = int(f.readline())
    MONTHLY_STAND_FEE = float(f.readline())
    DAILY_RENTAL_FEE = float(f.readline())
    WEEKLY_RENTAL_FEE = float(f.readline())
    HST_RATE = float(f.readline())

    f.close()

    while True:

        print()
        print("Add new Employee:")
        print()

        while True:
            empNameAllowed = set("QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm'")

            empFirstName = input("Enter employee first name: ").title()
            if not set(empFirstName).issubset(empNameAllowed):
                print("Enter a valid name please.")
            elif empFirstName == "":
                print("Enter a valid name please.")
            else:
                break

        while True:
            empLastName = input("Enter employee last name: ").title()
            if not set(empLastName).issubset(empNameAllowed):
                print("Enter a valid name please.")
            elif empLastName == "":
                print("Enter a valid name please.")
            else:
                break

        while True:
            empAddress = input("Enter employee address: ").upper()
            if empAddress == "":
                print("Enter a valid address.")
            else:
                break

        while True:
            empCityNotAllowed = set("1234567890")
            empCity = input("Enter employee city: ").title()
            if empCity == "":
                print("Enter a valid address.")
            elif set(empCity).issubset(empCityNotAllowed):
                print("Enter a valid city please. ")
            else:
                break

        while True:
            provAllowed = ["NL", "ON", "ONT", "QC", "SK", "MB", "NS", "NB", "PEI", "AB", "BC", "NWT", "NT", "YK"]
            empProv = input("Enter employee province(XX): ").upper()
            if empProv not in provAllowed:
                print("Enter a valid province please.")
            elif empProv == "":
                print("Enter province. ")
            else:
                break

        while True:
            empPostalCharAllowed = set("ASDFGHJKLQWERTYUIOPZXCVBNM")
            empPostalNumAllowed = set("1234567890")
            empPostal = input("Enter employee postal code(X1X1X1): ").upper()
            if empPostal == "":
                print("Enter a valid Postal Code.")
            elif len(empPostal) != 6:
                print("Enter a valid Postal Code without spaces.")
            elif not set(empPostal[0]).issubset(empPostalCharAllowed) or not set(empPostal[2]).issubset(empPostalCharAllowed) or not set(empPostal[4]).issubset(empPostalCharAllowed):
                print("1Enter a valid Postal Code.")
            elif not set(empPostal[1]).issubset(empPostalNumAllowed) or not set(empPostal[3]).issubset(empPostalNumAllowed) or not set(empPostal[5]).issubset(empPostalNumAllowed):
                print("2Enter a valid Postal Code.")
            else:
                break


        while True:
            phoneNumAllowed = set("1234567890-")
            empPhone = input("Enter employee phone number(999-999-9999): ")
            if not set(empPhone).issubset(phoneNumAllowed):
                print("Enter a valid number please. ")
            elif len(empPhone) != 12:
                print("Enter a full 10 digit phone number with dashes please. ")
            else:
                break

        while True:
            try:
                licenseNum = int(input("Enter driver license number: "))
            except:
                print("Enter a valid number please. ")
            else:
                if licenseNum == "":
                    print("Enter a license. ")
                else:
                    break

        while True:
            licenseTimelineAllowed = set("/1234567890")
            licenseTimeline = input("Enter the driver license expiry(99/99): ")
            if not set(licenseTimeline).issubset(licenseTimelineAllowed):
                print("Enter a valid set of numbers with a '/' please. ")
            elif licenseTimeline == "":
                print("Enter a license number please.")
            elif len(licenseTimeline) != 5:
                print("Use 2 digits for both month and year please. ")
            elif licenseTimeline[2] != "/":
                print("Use a '/' in the correct spot to define month and year please. ")
            else:
                break

        while True:
            insuranceNumAllowed = set("1234567890")
            insuranceNum = input("Enter the employee's insurance number: ")
            if not set(insuranceNum).issubset(insuranceNumAllowed):
                print("Enter a valid insurance number please. ")
            elif insuranceNum == "":
                print("Enter insurance number. ")
            else:
                break

        while True:
            insuranceCompany = input("Enter the insurance company: ").title()
            if insuranceCompany == "":
                print("You must enter a company. ")
            else:
                break

        while True:
            empOwnCar = input("Does this employee have their own car? (Y/N): ").upper()
            if empOwnCar != "Y" and empOwnCar != "N":
                print("Invalid response, enter Y or N please. ")
            elif empOwnCar == "":
                print("Invalid response, enter Y or N please. ")
            elif empOwnCar == "Y":
                balDueSubtotal = MONTHLY_STAND_FEE
                typeOfCharges = "N/A"
                break
            elif empOwnCar == "N":
                typeOfCharges = input("Type of Rental(Daily or Weekly): ").upper()
                if typeOfCharges == "DAILY":
                    balDueSubtotal = DAILY_RENTAL_FEE
                    break
                elif typeOfCharges == "WEEKLY":
                    balDueSubtotal = WEEKLY_RENTAL_FEE
                    break


        if empOwnCar == "N":
            empCarNum = input("Enter car ID(999): ")
        else:
            empCarNum = "N/A"

        balDueTotal = balDueSubtotal * (1 + HST_RATE)

        f = open("drivers.dat", "a")
        f.write(f"{NEXT_DRIVER_NUM},")
        f.write(f"{empFirstName}, ")
        f.write(f"{empLastName}, ")
        f.write(f"{empCarNum}, ")
        f.write(f"{empAddress}, ")
        f.write(f"{empCity}, ")
        f.write(f"{empProv}, ")
        f.write(f"{empPostal}, ")
        f.write(f"{empPhone}, ")
        f.write(f"{licenseNum}, ")
        f.write(f"{licenseTimeline}, ")
        f.write(f"{insuranceNum}, ")
        f.write(f"{insuranceCompany}, ")
        f.write(f"{empOwnCar}, ")
        f.write(f"{typeOfCharges}, ")
        f.write(f"{balDueSubtotal}, ")
        f.write(f"{balDueTotal}\n")
        f.close()

        NEXT_DRIVER_NUM += 1

        f = open('defaults.dat', 'w')
        f.write(f"{NEXT_TRANSACTION_NUM}\n")
        f.write(f"{NEXT_DRIVER_NUM}\n")
        f.write(f"{MONTHLY_STAND_FEE}\n ")
        f.write(f"{DAILY_RENTAL_FEE}\n")
        f.write(f"{WEEKLY_RENTAL_FEE} \n")
        f.write(f"{HST_RATE} ")
        f.close()



        balDueTaxAmt = balDueTotal - balDueSubtotal

        balDueSubtotalDsp = "${:,.2f}".format(balDueSubtotal)
        balDueTotalDsp = "${:,.2f}".format(balDueTotal)
        balDueTaxAmtDsp = "${:,.2f}".format(balDueTaxAmt)


        print()
        print(f" Employee added successfully.")
        print()

        print("EMPLOYEE DETAILS")
        print("=" * 70)
        print(f"NEW EMPLOYEE ADDED: {empFirstName:<15s} {empLastName:<15s}")
        print(f"DRIVER NUMBER: {NEXT_DRIVER_NUM:<5d}")  
        print("=" * 70)
        print("EMPLOYEE ADDRESS:")
        print(f"{empAddress:<60s}")
        print(f"{empCity:<30s} {empProv:<10s} {empPostal:<15s}")
        print(f"PHONE: {empPhone:<25s}")
        print("=" * 70)
        print("LICENSE INFORMATION:")
        print(f"LICENSE NUMBER: {str(licenseNum):>30s} - {licenseTimeline:<20s}")
        print("=" * 70)
        print("INSURANCE INFORMATION:")
        print(f"INSURANCE NUMBER: {str(insuranceNum):>28s} - {insuranceCompany:<25s}")
        print("=" * 70)
        print("EMPLOYEE CAR INFORMATION:")
        print(f"CAR NUMBER: {empCarNum:<40s}")
        print(f"EMPLOYEE OWNS CAR: {empOwnCar:<15s}")
        print(f"TYPE OF CHARGES: {typeOfCharges:<20s}")
        print("=" * 70)
        print("EMPLOYEE BALANCE:")
        print()
        print(f"SUBTOTAL: {balDueSubtotalDsp:>30s}")
        print(f"TAXES: {balDueTaxAmtDsp:>33s}")
        print(f"TOTAL: {balDueTotalDsp:>33s}")
        print("=" * 70)
        print()
        print()
        newEmployeeContinue = input("Do you want to enter a new employee?: ").upper()
        if newEmployeeContinue != "Y" and newEmployeeContinue != "N":
            print("Invalid response, enter Y or N please. ")
        elif newEmployeeContinue == "Y":
            pass
        else:
            break


def companyProfitListing():
    while True:
        start_date = input("Enter the start date (YYYY-MM-DD) or press enter to return to main menu: ")
        if not start_date.strip():
            break
        
        end_date = input("Enter the end date (YYYY-MM-DD): ")
        print()
        
        print("-" * 100)
        print(" " * 37 + "HAB Taxi Services - Profit Listing Report")
        print("-" * 100)
        print(f"Report Period: {start_date} to {end_date}\n")
        
        expenses = []
        revenue = []

        with open("expenses.dat", "r") as expenses_file:
            lines = expenses_file.readlines() 
            for line in lines: 
                data = line.strip().split(',') 
                expenses.append({ 
                    "InvNum": int(data[0]),
                    "DriverID": int(data[1]),
                    "CarID": int(data[2]),
                    "InvDate": data[3],
                    "ItemName": data[4],
                    "ItemNum": int(data[5]),
                    "Description": data[6],
                    "Quantity": int(data[7]),
                    "UnitCost": float(data[8]),
                    "Subtotal": float(data[9]),
                    "HST": float(data[10]),
                    "Total": float(data[11])
                })

        with open("revenue.dat", "r") as revenue_file:
            next(revenue_file) 
            for line in revenue_file:
                data = line.strip().split(',')
                revenue.append({
                    "TransactionID": int(data[0]),
                    "Date": data[1],
                    "PaymentDescription": data[2],
                    "DriverID": int(data[3]),
                    "Subtotal": float(data[4]),
                    "HSTamt": float(data[5]),
                    "Total": float(data[6]),
                })

        total_revenue = sum(rev["HSTamt"] for rev in revenue if start_date <= rev["Date"] <= end_date)
        total_expenses = sum(expense["Subtotal"] + expense["HST"] for expense in expenses if start_date <= expense["InvDate"] <= end_date)
        total_profit_loss = total_revenue - total_expenses

        print("Revenues:")
        print(f"Total Revenue: ${total_revenue:.2f}")
        print("Revenue Breakdown:")
        print()
        print("  Type:                                         Amount:")
        for i, rev in enumerate(revenue, start=1):
            if start_date <= rev["Date"] <= end_date:
                print(f"  {rev['PaymentDescription']:45} ${rev['Total']:.2f}")

        print("\nExpenses:")
        print(f"Total Expenses: ${total_expenses:.2f}")
        print("Expenses Breakdown:")
        print()
        print("  Type:                                         Amount:")
        for i, expense in enumerate(expenses, start=1):
            if start_date <= expense["InvDate"] <= end_date:
                print(f"  {expense['Description']:45} ${expense['Total']:.2f}")

        print("-" * 100)
        print(f"Profit Loss: ${total_profit_loss:.2f}")
        print("-" * 100)
        print()

def customReport():
    """
    Custom report uses data from revenue.dat and drivers.dat to generate a report
    that shows the payments for each driver, the total amount of payments made, and 
    the total amount of money owed for a specified period of time
    """
    driver_info = {}
    with open('drivers.dat', 'r') as f:
        next(f) 
        for line in f:
            data = line.strip().split(',')
            driver_id = int(data[0])
            driver_info[driver_id] = {
                'LicenseNum': data[1],
                'CarID': data[2],
                'EmpName': data[3],
                'EmpStreetAdd': data[4],
                'EmpCity': data[5],
                'EmpProv': data[6],
                'EmpPhone': data[7],
                'EmpEmail': data[8],
                'BalDue': float(data[9]) if data[9] != 'Yes' else 0.0,
            }

    revenue_info = []
    with open('revenue.dat', 'r') as f:
        next(f)
        for line in f:
            data = line.strip().split(',')
            revenue_info.append({
                'transaction_id': int(data[0]),
                'date': data[1],
                'payment_description': data[2],
                'driver_id': int(data[3]),
                'subtotal': float(data[4]),
                'hst': float(data[5]),
                'total': float(data[6]),
            })

    while True:
        driver_number_input = input("Enter driver number (or 0 to return to the main menu): ")
        if driver_number_input == '0':
            break

        try:
            driver_number = int(driver_number_input)
        except ValueError:
            print("Invalid input. Please enter a valid driver number or 0 to return to the main menu.")
            continue
        
        target_start_date = input("Enter the start date of the range (YYYY-MM-DD): ")
        target_end_date = input("Enter the end date of the range (YYYY-MM-DD): ")
        print()
        
        if driver_number in driver_info:
            driver = driver_info[driver_number]
            company_name = "HAB Taxi Service"
            print("{:^103s}".format(company_name))
            print("-" * 103)
            print(f"Report for Driver: {driver_number} ")
            print(f"Employee Name: {driver['EmpName']}")
            print(f"Address: {driver['EmpStreetAdd']}, {driver['EmpCity']}, {driver['EmpProv']}")
            print()
            print("Date          Transaction ID          Payment Description          Subtotal          HST          Total")
            print("-" * 103)

            total_payments = 0

            for entry in revenue_info:
                if entry['driver_id'] == driver_number and target_start_date <= entry['date'] <= target_end_date:
                    print("{:<10s}         {:<15d}     {:<25s}   {:<12.2f}     {:<8.2f}   {:>8.2f}".format(
                        entry['date'], entry['transaction_id'], entry['payment_description'],
                        entry['subtotal'], entry['hst'], entry['total']))
                    total_payments += entry['total']

            print("-" * 103)
            remaining_balance = driver['BalDue'] - total_payments
            if remaining_balance < 0:
                remaining_balance = 0
            print(f"Total payments within the date range: ${total_payments:.2f}")
            print(f"Remaining balance owing: ${remaining_balance:.2f}")
            print()
        else:
            print(f"Driver {driver_number} not found.")


# Main program
while True:
    print()
    print("           HAB Taxi Services")
    print("        Company Services System")
    print()
    print("1. Enter a New Employee (driver)")
    print("2. Enter Company Revenues")
    print("3. Enter Company Expenses")
    print("4. Track Car Rentals")
    print("5. Record Employee Payment")
    print("6. Print Company Profit Listing")
    print("7. Print Driver Financial Listing")
    print("8. Custom report")
    print("9. Quit Program")
    print()

    try:
        userInput = int(input("Enter a number of 1 through 9: "))
    except:
        print("Please enter a valid number.")
    else:
        if userInput == 1:
            newEmployee()
        elif userInput == 2:
            while True:
                notConfig = input("Option not configured. Try another menu option?(Y or N): ").upper()
                if notConfig != "Y" and notConfig != "N":
                    print("Invalid response, enter Y or N please.")
                if notConfig == "Y":
                    break
                if notConfig == "N":
                    break
            if notConfig == "N":
                break
        elif userInput == 3:
            while True:
                notConfig = input("Option not configured. Try another menu option?(Y or N): ").upper()
                if notConfig != "Y" and notConfig != "N":
                    print("Invalid response, enter Y or N please.")
                if notConfig == "Y":
                    break
                if notConfig == "N":
                    break
            if notConfig == "N":
                break
        elif userInput == 4:
            while True:
                notConfig = input("Option not configured. Try another menu option?(Y or N): ").upper()
                if notConfig != "Y" and notConfig != "N":
                    print("Invalid response, enter Y or N please.")
                if notConfig == "Y":
                    break
                if notConfig == "N":
                    break
            if notConfig == "N":
                break
        elif userInput == 5:
            while True:
                notConfig = input("Option not configured. Try another menu option?(Y or N): ").upper()
                if notConfig != "Y" and notConfig != "N":
                    print("Invalid response, enter Y or N please.")
                if notConfig == "Y":
                    break
                if notConfig == "N":
                    break
            if notConfig == "N":
                break
        elif userInput == 6:
            companyProfitListing()
        elif userInput == 7:
            while True:
                notConfig = input("Option not configured. Try another menu option?(Y or N): ").upper()
                if notConfig != "Y" and notConfig != "N":
                    print("Invalid response, enter Y or N please.")
                if notConfig == "Y":
                    break
                if notConfig == "N":
                    break
            if notConfig == "N":
                break
        elif userInput == 8:
            customReport()
        elif userInput == 9:
            print("\nSystem entering sleep mode. Thanks for using the company system.")
            break
