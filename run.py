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
    print(f"your data provided was {data_str}")


get_sales_data()



