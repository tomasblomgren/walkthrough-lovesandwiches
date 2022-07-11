import gspread
from google.oauth2.service_account import Credentials

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
    print("Please enter sales data from last market")
    print("data should be six numbers separated by commas")
    print("Example 1,2,3,4,5,6\n")

    data_str = input("Enter your numbers here!: ")

    sales_data = data_str.split(",")
    validate_data(sales_data)


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


get_sales_data()
