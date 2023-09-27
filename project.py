import csv
import time
import pyfiglet
import cowsay
from tabulate import tabulate
import yfinance as yf


def main():
    introduction = pyfiglet.figlet_format("Welcome to Stock Portfolio Tracker")
    print(introduction)
    user_login_interface()


def user_login_interface():
    """
    This function displays the user login interface, allowing users to log in, sign up,
    or exit the program based on their input.
    """
    while True:
        login_bar = [
            ["Option", "Action"],
            ["L", "Login"],
            ["S", "Signup"],
            ["E", "Exit"],
        ]
        print(tabulate(login_bar, headers="firstrow", tablefmt="grid"))
        start = input("👉 Select an option (L/S/E): ").upper()
        # Invalid input
        if start not in (("L", "S", "E")):
            print_color("Invalid input! Please try again. 🥲", RED)
        # Exit
        elif start == "E":
            farewell = pyfiglet.figlet_format("Goodbye")
            print(farewell)
            print_color(cowsay.get_output_string("cow", "Happy Investing!"), CYAN)
            break
        # Login
        elif start == "L":
            username = input("- Enter your username: ")
            password = input("- Enter your password: ")

            if check_login(username, password):
                print_color("Login successful! 🙂", GREEN)
                time.sleep(2)
                display_portfolio(username)
            else:
                print_color("Invalid username or password. Please try again.🥲", RED)
        # Signup
        elif start == "S":
            new_username = input("- Create a username: ")
            new_password = input("- Create a password: ")
            if check_create_user(new_username, new_password):
                print_color("Signup successful! You can now log in.🙂", GREEN)
            else:
                print_color("Username already exists. Please choose a different one.🥲", RED)


def check_login(username, password):
    """
    Check if the provided username and password match any records in the login database.
    True if the provided credentials match a record, False otherwise.
    """
    # Check if the provided username and password match any records in the login_database.csv
    with open("login_database.csv", "r") as file:
        reader = csv.reader(file)
        for row in reader:
            if username == row[0] and password == row[1]:
                return True
        return False


def check_create_user(username, password):
    """
    Check if a username already exists and create a new user if it doesn't.
    True if the username is new and successfully created, False if the username already exists.
    """
    # If username exists, ask for username again
    with open("login_database.csv", "r") as file:
        reader = csv.reader(file)
        for row in reader:
            if username == row[0]:
                return False
    # If username is new, add username and password to the login_database.csv
    with open("login_database.csv", "a", newline="\n") as file:
        writer = csv.writer(file)
        writer.writerow([username, password])
    return True


def display_portfolio(username):
    portfolio = sorted(load_portfolio_from_csv(username))

    while True:
        dashboard_menu = [
            ["Option", "Description"],
            ["1", "View Portfolio"],
            ["2", "Add New Stock to Portfolio"],
            ["3", "Delete Stock from Portfolio"],
            ["4", "Get Detail Information about One Stock"],
            ["5", "Exit"],
        ]
        print_color("Portfolio Dashboard:", CYAN)
        print(tabulate(dashboard_menu, headers="firstrow", tablefmt="grid"))
        choice = input("👉 Enter your choice (1/2/3/4/5): ")

        # Option 1: View Portfolio
        if choice == "1":
            if not portfolio:
                print_color("Your portfolio is empty.", RED)

            else:
                print_color("Your portfolio: ", GREEN)
                for i, symbol in enumerate(portfolio):
                    print(i+1, symbol)

        # Option 2: Add New Stock to Portfolio
        elif choice == "2":
            symbol = input("Enter the stock symbol to add: ").upper()
            # Check if the entered symbol is valid using yfinance
            try:
                stock = yf.Ticker(symbol)
                if "N/A" in stock.info["longName"]:
                    raise ValueError
                elif symbol in portfolio:
                    print_color(f"'{symbol}' is already in your portfolio.", RED)
                else:
                    portfolio.append(symbol)
                    print_color(f"'{symbol}' has been added to your portfolio.", GREEN)
            except (ValueError, Exception):
                print_color(f"'{symbol}' is not a valid stock symbol", RED)

        # Option 3: Delete Stock from Portfolio
        elif choice == "3":
            symbol = input("Enter the stock symbol to delete: ").upper()
            if symbol in portfolio:
                while True:
                    confirm = input(f"Do you confirm to remove '{symbol}' from your portfolio? Press Y/N: ").upper()
                    if confirm == "Y":
                        portfolio.remove(symbol)
                        print_color(f"'{symbol}' has been remove from your portfolio.", GREEN)
                        break
                    elif confirm == "N":
                        print_color(f"Deletion of '{symbol}' cancelled.", RED)
                        break
                    else:
                        print_color("Invalid input. Please enter 'Y' to confirm or 'N' to cancel.", RED)
            else:
                print_color(f"'{symbol}' is not in your portfolio.", RED)

        # Option 4: Get Detail Information about One Stock
        elif choice == "4":
            symbol = input("Enter the stock symbol to get details: ").upper()
            stock = yf.Ticker(symbol)
            stock_info = stock.info
            print_color(f"Stock Information for '{symbol}'", GREEN)

            keys_to_print = [
                "longName",  # Full name of the company
                "country",   # Country where the company is based
                "website",   # Company's website URL
                "industry",  # Industry the company belongs to
                "sector",    # Sector the company operates in
                "regularMarketPreviousClose",  # Previous day's closing price
                "regularMarketOpen",  # Today's opening price
                "marketCap",  # Market capitalization
                "trailingPE",  # Trailing price-to-earnings ratio
                "forwardPE",   # Forward price-to-earnings ratio
                "trailingAnnualDividendYield",  # Trailing annual dividend yield
                "trailingAnnualDividendRate",   # Trailing annual dividend rate
                "dividendYield",   # Current dividend yield
                "dividendRate",    # Current dividend rate
                "beta",            # Beta value (stock's volatility relative to the market)
                "fiftyDayAverage",  # 50-day moving average
                "twoHundredDayAverage",  # 200-day moving average
            ]

            stock_data = []
            for key in keys_to_print:
                if key in stock_info:
                    if key == "marketCap":
                        # Format marketCap with commas
                        value = f"{stock_info[key]:,}"
                    else:
                        value = stock_info[key]
                    stock_data.append([key, value])
                else:
                    stock_data.append([key, "N/A"])
            chart_link = f"https://finance.yahoo.com/chart/{symbol}"
            stock_data.append(["chartLink", chart_link])
            print(tabulate(stock_data, headers=["Attribute", "Value"], tablefmt="github"))


        # Option 5: Exit and Save Portfolio
        elif choice == "5":
            print_color("Exiting the Stock Portfolio Tracker. \nBack to Login Interface.", GREEN)
            save_portfolio_to_csv(username, portfolio)
            break

        # Wrong Option: Ask again
        else:
            print_color("Invalid choice! Please select a valid option (1/2/3/4/5).🥲", RED)


def load_portfolio_from_csv(username):
    """
    This function takes a username as input and looks for the portfolio data of
    the matching username in 'portfolio.csv'.
    If the user's data is found, it returns the list of stock symbols in their portfolio.
    If the user's data is not found, it creates new empty list.
    """
    with open("portfolio.csv", "r") as file:
        reader = csv.reader(file)
        for row in reader:
            if len(row) == 2 and row[0] == username:
                return row[1].split(",") if row[1] else []
    return []


def save_portfolio_to_csv(username, portfolio):
    """
    This function takes a username and a portfolio list as input and updates the
    portfolio data in 'portfolio.csv'.
    If the user's data is not found, it creates a new entry.
    If the user's data is found, it updates the existing portfolio.
    """
    # Extract portfolio.csv data to a temporary list called 'data'
    data = []
    with open("portfolio.csv", "r") as file:
        reader = csv.reader(file)
        for row in reader:
            data.append(row)

    # Update or add the user's portfolio to portfolio.csv
    user_found = False
    for row in data:
        if row and row[0] == username:
            if len(row) > 1:
                row[1] = ",".join(portfolio) # Update the portfolio
            else:
                row.append(",".join(portfolio)) # If row[1] is empty, create a new portfolio
            user_found = True # Update user founded

    # If the user's data is not found, create a new entry
    if not user_found:
        new_entry = [username, ",".join(portfolio)]
        data.append(new_entry)

    # Write the updated data back to portfolio.csv
    with open("portfolio.csv", "w", newline="\n") as file:
        writer = csv.writer(file)
        writer.writerows(data)


CYAN = "\x1b[36m"
RESET = "\033[0m"
RED = "\033[91m"
GREEN = "\033[92m"


def print_color(text, color_code):
    """
    Prints the provided text in the specified color format.
    Note that color_code is the ANSI color code to apply to the text.
    """
    print()
    print("========================")
    print(color_code + text + RESET)
    print("========================")
    print()


if __name__ == "__main__":
    main()
