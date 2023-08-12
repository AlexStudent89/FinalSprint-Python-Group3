# Program Name: Final Sprint - HAB Taxi Services
# Program Description: A program designed to service HAB Taxi Services, with calculations and reports
# Written By: Group 3
# Written On: August 4th - August 18, 2023

# imports
import csv
import datetime

# Constants
f = open('defaults.dat', 'r')

NEXT_TRANSACTION_NUM = int(f.readline())
NEXT_DRIVER_NUM = int(f.readline())
MONTHLY_STAND_FEE = float(f.readline())
DAILY_RENTAL_FEE = float(f.readline())
WEEKLY_RENTAL_FEE = float(f.readline())
HST_RATE = float(f.readline())

f.close()


# functions
def newEmployee():
    while True:

        empDriverNum = NEXT_DRIVER_NUM

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
            empAddress = input("Enter employee address: ")
            if empAddress == "":
                print("Enter a valid address.")
            else:
                break

        while True:
            empCityNotAllowed = set("1234567890")
            empCity = input("Enter employee city: ")
            if empCity == "":
                print("Enter a valid address.")
            elif set(empCity).issubset(empCityNotAllowed):
                print("Enter a valid city please. ")
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
            provAllowed = ["NL", "ON", "ONT", "QC", "SK", "MB", "NS", "NB", "PEI", "AB", "BC", "NWT", "NT", "YK"]
            empProv = input("Enter employee province(XX): ").upper()
            if empProv not in provAllowed:
                print("Enter a valid province please.")
            elif empProv == "":
                print("Enter province. ")
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
            licenseTimeline = input("Enter the driver license expiry with a '/' ")
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
            insuranceCompany = input("Enter the insurance company: ")
            if insuranceCompany == "":
                print("You must enter a company. ")
            else:
                break

        while True:
            empOwnCar = input("Does this employee have their own car? (Y/N)").upper()
            if empOwnCar != "Y" and empOwnCar != "N":
                print("Invalid response, enter Y or N please. ")
            elif empOwnCar == "Y":
                balDueSubtotal = MONTHLY_STAND_FEE
                break
            elif empOwnCar == "N":
                typeOfCharges = input("Daily or weekly rental? Enter Daily or Weekly: ").upper()
                if typeOfCharges == "DAILY":
                    balDueSubtotal = DAILY_RENTAL_FEE
                    break
                elif typeOfCharges == "WEEKLY":
                    balDueSubtotal = WEEKLY_RENTAL_FEE
                    break

        balDueTotal = balDueSubtotal * (1 + HST_RATE)

        f = open("drivers.dat", "a")

        driverFirstName = f.write(f"{empFirstName}, ")
        driverLastName = f.write(f"{empLastName}, ")
        driverAddress = f.write(f"{empAddress}, ")
        driverCity = f.write(f"{empCity}, ")
        driverProv = f.write(f"{empProv}, ")
        driverPostal = f.write(f"{empPostal}, ")
        driverPhone = f.write(f"{empPhone}, ".format(str(empPhone)))
        driverLicense = f.write(f"{licenseNum}, ".format(str(licenseNum)))
        driverLicenseTimeline = f.write(f"{licenseTimeline}, ")
        driverInsurance = f.write(f"{insuranceNum}, ")
        driverInsuranceCompany = f.write(f"{insuranceCompany}, ")
        driverCarYN = f.write(f"{empOwnCar}, ")
        driverBalDueSubtotal = f.write(f"{balDueSubtotal}, ".format(str(balDueSubtotal)))
        driverBalDueTotal = f.write(f"{balDueTotal}, \n".format(str(balDueTotal)))

        f.close()




    # update driver num in defaults
    # print receipt
    # continue prompt
# def carRentals():


# def companyProfitListing():


def customReport():
    """
    Generates a custom financial report for a specific driver within a given date range.

    Parameters:
    - driver_number_input (str): The driver number to generate the report for. Enter '0' to return to the main menu.
    - target_start_date (str): The start date of the date range (YYYY-MM-DD).
    - target_end_date (str): The end date of the date range (YYYY-MM-DD).

    Outputs:
    - Displays a report showing transaction details, payments, and remaining balance for the selected driver
      within the specified date range. If the driver number is '0', the function returns to the main menu.
    """
    driver_data = {}
    with open('drivers.dat', 'r') as f:
        next(f)  # Skip the header line
        for line in f:
            data = line.strip().split(',')
            driver_id = int(data[0])
            driver_info = {
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
            driver_data[driver_id] = driver_info

    revenue_data = []
    with open('revenue.dat', 'r') as f:
        next(f)  # Skip the header line
        for line in f:
            data = line.strip().split(',')
            transaction_id = int(data[0])
            date = data[1]
            payment_description = data[2]
            driver_id = int(data[3])
            subtotal = float(data[4])
            hst = float(data[5])
            total = float(data[6])
            revenue_info = {
                'payment_description': payment_description,
                'subtotal': subtotal,
                'hst': hst,
                'total': total
            }
            revenue_data.append({
                'transaction_id': transaction_id,
                'date': date,
                'driver_id': driver_id,
                'revenue_info': revenue_info
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

        if driver_number in driver_data:
            driver_info = driver_data[driver_number]
            print(f"Report for Driver {driver_number}: {driver_info['EmpName']}")
            print("Date\t\tTransaction ID\tPayment Description\tSubtotal\tHST\tTotal")

            total_payments = 0

            for entry in revenue_data:
                if entry['driver_id'] == driver_number and target_start_date <= entry['date'] <= target_end_date:
                    revenue_info = entry['revenue_info']
                    print(f"{entry['date']}\t{entry['transaction_id']}\t\t{revenue_info['payment_description']}\t\t{revenue_info['subtotal']:.2f}\t\t{revenue_info['hst']:.2f}\t{revenue_info['total']:.2f}")
                    total_payments += revenue_info['total']

            print("\nSummary:")
            remaining_balance = driver_info['BalDue'] - total_payments
            if remaining_balance < 0:
                remaining_balance = 0
            print(f"Total payments within the date range: ${total_payments:.2f}")
            print(f"Remaining balance owing: ${remaining_balance:.2f}")
        else:
            print(f"Driver {driver_number} not found.")

    if __name__ == "__main__":
        customReport()

# main program

while True:
    print()
    print("           HAB Taxi Services")
    print("           Company Services System")
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
        if 9 < userInput < 1:
            print("Please enter a valid number.")
        else:
            if userInput == 1:
                newEmployee()
            elif userInput == 2:
                print("Option not configured.")
            elif userInput == 3:
                print("Option not configured.")
            elif userInput == 4:
                carRentals()
            elif userInput == 5:
                employeePayment()
            elif userInput == 6:
                companyProfitListing()
            elif userInput == 7:
                print("Option not configured.")
            elif userInput == 8:
                customReport()
            else:
                print()
                print("System entering sleep mode. Thanks for using the company system.")
                break