import gspread
from google.oauth2.service_account import Credentials
from pprint import pprint

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('love_sandwiches')


def get_sales_data():
    """
    Get sales input figures from the user
    """
    while True:

        print("Please enter sales data from last market")
        print("data should be six numbers separated by commas")
        print("Example 1,2,3,4,5,6\n")

        data_str = input("Enter your numbers here!: ")

        sales_data = data_str.split(",")

        if validate_data(sales_data):
            print("Data is valid!")
            break
    return sales_data


def validate_data(values):
    """
    inside the try, converts all string values into integers
    Raises valuerror to all data that is not strings or not 6 inputs
    """
    [int(value)for value in values]
    try:
        if len(values) != 6:
            raise ValueError(
                f"Exactly 6 values required, you provided {len(values)}"
            )
    except ValueError as e:
        print(f"invalid data: {e}, please try again.\n ")
        return False

    return True


def update_sales_worksheet(data):
    """
    updating sales worksheet, add new row with the list data provided
    """
    print("updating sales worksheet\n")
    sales_worksheet = SHEET.worksheet("sales")
    sales_worksheet.append_row(data)
    print("sales worksheet updated successfully.\n")


def update_surplus_worksheet(data):
    """
    updating surplus worksheet, add new row with the list data provided
    """
    print("updating surplus worksheet\n")
    surplus_worksheet = SHEET.worksheet("surplus")
    surplus_worksheet.append_row(data)
    print("surplus worksheet updated successfully.\n")


def calculate_surplus_data(sales_row):
    """
    compare sales with stock and calculate surplus data
    """

    print("calulating surplus data...\n")
    stock = SHEET.worksheet("stock").get_all_values()
    stock_row = stock[-1]
 
    surplus_data = []
    for stock, sales in zip(stock_row, sales_row):
        surplus = int(stock) - sales
        surplus_data.append(surplus)
 
    return surplus_data


def main():
    """
    Run all program funtions
    """
    data = get_sales_data()
    sales_data = [int(num)for num in data]
    update_sales_worksheet(sales_data)
    new_surplus_data = calculate_surplus_data(sales_data)
    update_surplus_worksheet(new_surplus_data)


print("Welcome to love sandwiches data automation")
main()
