import unittest
from unittest.mock import Mock

# Example one
class Angel:
    def __init__(self, degrees):
        self.degrees = degrees % 360
    def is_acute(self):
        return self.degrees < 90
    def __add__(self, other):
        return Angel(self.degrees + other.degrees)

class TestAngel(unittest.TestCase):
    def test_degrees(self):
        small_angel = Angel(10)
        self.assertEqual(small_angel.degrees, 10)
        self.assertTrue(small_angel.is_acute())
        big_angel = Angel(320)
        self.assertEqual(big_angel.degrees, 320)
        self.assertFalse(big_angel.is_acute())

    def test_add(self):
        small_angel = Angel(10)
        big_angel = Angel(320)
        total_angle = small_angel + big_angel
        self.assertEqual(total_angle.degrees, 330)

# Example two
class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            raise ValueError("Division by zero is not allowed.")
        return a / b

class TestCalculator(unittest.TestCase):
    def setUp(self):
        """Set up a Calculator instance for use in tests."""
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)

    def test_subtract(self):
        self.assertEqual(self.calc.subtract(5, 3), 2)
        self.assertEqual(self.calc.subtract(-1, -1), 0)

    def test_multiply(self):
        self.assertEqual(self.calc.multiply(3, 4), 12)
        self.assertEqual(self.calc.multiply(-1, 5), -5)

    def test_divide(self):
        self.assertEqual(self.calc.divide(10, 2), 5)
        self.assertEqual(self.calc.divide(-10, 2), -5)
        with self.assertRaises(ValueError):
            self.calc.divide(10, 0)


# Example three
class InsufficientFundsError(Exception):
    """Custom exception for insufficient funds."""
    pass

class Account:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            raise InsufficientFundsError("Insufficient funds for withdrawal.")
        self.balance -= amount

    def get_balance(self):
        return self.balance


class Bank:
    def __init__(self):
        self.accounts = {}

    def create_account(self, owner):
        if owner in self.accounts:
            raise ValueError("Account already exists.")
        self.accounts[owner] = Account(owner)

    def get_account(self, owner):
        return self.accounts.get(owner)

    def transfer(self, from_owner, to_owner, amount):
        from_account = self.get_account(from_owner)
        to_account = self.get_account(to_owner)

        if from_account is None or to_account is None:
            raise ValueError("One or both accounts do not exist.")

        from_account.withdraw(amount)
        to_account.deposit(amount)

class TestBankingSystem(unittest.TestCase):
    def setUp(self):
        """Set up a Bank instance for use in tests."""
        self.bank = Bank()
        self.bank.create_account("Alice")
        self.bank.create_account("Bob")

    def test_create_account(self):
        self.bank.create_account("Charlie")
        self.assertIn("Charlie", self.bank.accounts)
        with self.assertRaises(ValueError):
            self.bank.create_account("Alice")  # Duplicate account

    def test_deposit(self):
        account = self.bank.get_account("Alice")
        account.deposit(100)
        self.assertEqual(account.get_balance(), 100)

        with self.assertRaises(ValueError):
            account.deposit(-50)  # Invalid deposit

    def test_withdraw(self):
        account = self.bank.get_account("Alice")
        account.deposit(100)
        account.withdraw(50)
        self.assertEqual(account.get_balance(), 50)

        with self.assertRaises(InsufficientFundsError):
            account.withdraw(100)  # Insufficient funds

    def test_transfer(self):
        account_a = self.bank.get_account("Alice")
        account_b = self.bank.get_account("Bob")

        account_a.deposit(100)
        self.bank.transfer("Alice", "Bob", 50)

        self.assertEqual(account_a.get_balance(), 50)
        self.assertEqual(account_b.get_balance(), 50)

        with self.assertRaises(ValueError):
            self.bank.transfer("Alice", "Charlie", 10)  # Non-existent account

    def test_get_balance(self):
        account = self.bank.get_account("Alice")
        self.assertEqual(account.get_balance(), 0)

        account.deposit(200)
        self.assertEqual(account.get_balance(), 200)


class TestBankingSystemWithFixtures(unittest.TestCase):

    def setUp(self):
        """Set up a Bank instance and accounts for use in tests."""
        self.bank = Bank()
        self.bank.create_account("Alice")
        self.bank.create_account("Bob")
        self.bank.get_account("Alice").deposit(100)  # Initial balance for Alice
        self.bank.get_account("Bob").deposit(50)  # Initial balance for Bob

    def tearDown(self):
        """Clean up after tests."""
        self.bank = None  # Clear the bank instance

    def test_initial_balances(self):
        """Test the initial balances of the accounts."""
        self.assertEqual(self.bank.get_account("Alice").get_balance(), 100)
        self.assertEqual(self.bank.get_account("Bob").get_balance(), 50)

    def test_deposit(self):
        account = self.bank.get_account("Alice")
        account.deposit(50)
        self.assertEqual(account.get_balance(), 150)

    def test_withdraw(self):
        account = self.bank.get_account("Alice")
        account.withdraw(30)
        self.assertEqual(account.get_balance(), 70)

        with self.assertRaises(InsufficientFundsError):
            account.withdraw(100)  # Attempt to withdraw more than available

    def test_transfer(self):
        self.bank.transfer("Alice", "Bob", 30)
        self.assertEqual(self.bank.get_account("Alice").get_balance(), 70)
        self.assertEqual(self.bank.get_account("Bob").get_balance(), 80)

        with self.assertRaises(ValueError):
            self.bank.transfer("Alice", "Charlie", 10)  # Non-existent account

# Integration Testing
def fetch_data(api_client):
    data = api_client.get_data()
    return data

class UserRepository:
    def __init__(self, db_client):
        self.db_client = db_client

    def get_user(self, user_id):
        return self.db_client.query_user(user_id)

class TestFetchData(unittest.TestCase):
    def test_fetch_data(self):
        mock_client = Mock()
        mock_client.get_data.return_value = {"key": "value"}
        result = fetch_data(mock_client)
        self.assertEqual(result, {"key": "value"})

    def test_get_user(self):
        # Create a mock for the database client
        mock_db_client = Mock()
        mock_db_client.query_user.return_value = {"name": "Bob", "age": 25}

        user_repo = UserRepository(mock_db_client)

        # Call the method
        result = user_repo.get_user(1)

        # Verify the result
        self.assertEqual(result, {"name": "Bob", "age": 25})
        # Ensure the query_user method was called with the correct argument
        mock_db_client.query_user.assert_called_once_with(1)


if __name__ == "__main__":
    unittest.main()