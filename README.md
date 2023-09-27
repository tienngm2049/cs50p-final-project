# STOCK PORTFOLIO TRACKER WITH REAL-TIME DATA

#### Video Demo: [Insert Video URL Here]

#### Description:
This project is a platform that allows you to efficiently manage and track your stock portfolio. Users can create accounts with usernames and passwords to securely access their portfolios. The application interacts with two CSV files: `login_database.csv` to authenticate users and `portfolio.csv` to store portfolio data.

#### Project Structure:
- `project.py`: The main Python script that runs the application.
- `test_project.py`: Unit tests for the application.
- `requirements.txt`: Lists all necessary Python libraries for easy installation.
- `README.md`: Documentation for the project.
- `login_database.csv`: Stores user login credentials.
- `portfolio.csv`: Stores user stock portfolios.

#### Libraries Used:
- **Tabulate:** Used for formatting tables in the application.
- **Cowsay:** Provides fun and interactive cow-based messages.
- **Pyfiglet:** Generates stylish text banners and ASCII art.
- **yfinance:** Enables access to real-time stock data.

To install the required libraries, simply run the following pip command:

```bash
pip install -r requirements.txt
```

#### Functionality:
- **User Authentication:** Users can log in with their existing credentials or sign up for a new account.
- **Real-Time Stock Data:** Access real-time data for stocks, including current prices, market capitalization, and more.
- **Portfolio Management:** Users can view, add, update, and delete stocks in their portfolio.
- **Stock Information:** Get detailed information about individual stocks, such as company name, sector, and website, price, PE and chart.
- **Automatic Saving:** All portfolio updates are automatically saved to `portfolio.csv`.
- **Security:** User login credentials and financial data are kept secure and private.

#### Usage:
1. When you log in or sign up, the program interacts with `login_database.csv` to check for existing usernames and passwords or appends new accounts.

2. Upon successful login, a dashboard is displayed with the following options:
   - View Portfolio
   - Add New Stock to Portfolio
   - Delete Stock from Portfolio
   - Get Detailed Information about One Stock
   - Exit

3. You can choose an option to manage your portfolio. When you exit, all new information is updated in `portfolio.csv`.

This Stock Portfolio Tracker empowers investors to stay informed about their investments, analyze stock performance, and make data-driven decisions. Watch the video demo to see the application in action and start optimizing your investment strategy today!