from project import check_login, check_create_user, load_portfolio_from_csv
import random
import string

def test_check_login():
    assert check_login("test1", "pass1") == True
    assert check_login("test2", "pass2") == True

    assert check_login("nonexistentuser", "testpassword") == False
    assert check_login("nonexistentuser2", "testpassword2") == False

# Function to generate a random string of a specified length
def generate_random_string(min_length, max_length):
    length = random.randint(min_length, max_length)
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))

def test_check_create_user():
    assert check_create_user("test1", "pass1") == False
    assert check_create_user("test2", "pass2") == False

    # Generate random usernames and passwords
    username1 = generate_random_string(6, 10)
    password1 = generate_random_string(6, 10)
    username2 = generate_random_string(6, 10)
    password2 = generate_random_string(6, 10)
    assert check_create_user(username1, password1) == True
    assert check_create_user(username2, password2) == True

    # Test with duplicate usernames
    assert check_create_user(username1, password1) == False
    assert check_create_user(username2, password2) == False

def test_load_portfolio_from_csv():
    assert load_portfolio_from_csv("test1") == ["AAPL","NVDA"]
    assert load_portfolio_from_csv("test2") == []
    assert load_portfolio_from_csv("tienngm2049") == ["AAPL", "AMZN", "NVDA", "TSLA"]

