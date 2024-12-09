# Intro_project 🎉

A mini project written in Python 3.12, showcasing the use of modern tools and best practices in software development.  
This project utilizes:

- **Poetry** 🛠️ – for virtual environment and dependency management,
- **mypy** ✅ – for static type checking,
- **pytest** 🧪 – for unit testing.

---

## Project Overview 📚

The project implements a simple `BankAccount` class with the following functionalities:

- Creating a bank account with an initial balance,
- Depositing and withdrawing funds,
- Handling errors, such as trying to withdraw more money than available.

The project also includes unit tests to ensure code correctness.

---

## Requirements 🖥️

- **Python** 3.12+
- **Poetry** 1.6.1 or newer
- **mypy** 1.5.0 or newer
- **pytest** 7.0.0 or newer

---

## Installation 🚀

### 1. Clone the repository:
   ```bash
   git git@github.com:Kinetics20/intro_project.git
   cd intro_projekt
```

### 2.  Install dependencies using Poetry:
```bash
poetry install
```

### 3. Activate the virtual environment:

```bash
# Linux/macOS
poetry shell
```
```bash
# Windows (Command Prompt or PowerShell)
poetry shell
```
### 4. Install `mypy` for static type checking:
```bash
# Linux/macOS
pip install mypy

# Windows (Command Prompt or PowerShell)
pip install mypy
```

### 5. Install `pytest` for running tests:
```bash
# Linux/macOS
pip install pytest

# Windows (Command Prompt or PowerShell)
pip install pytest
```
### Running Tests 🧪
```bash
pytest
```
---

### Type Checking ✅
```bash
mypy bank_account.py
```

## Features 🔧

### `BankAccount` Class

- `__init__(owner: str, account_number: str, balance: Decimal = Decimal("0.0")) -> None`  
  Creates a bank account.

- `deposit(amount: Decimal) -> None`  
  Deposits funds into the account (only positive amounts are allowed).

- `withdraw(amount: Decimal) -> None`  
  Withdraws funds from the account (the amount cannot exceed the current balance).

- `get_balance() -> str`  
  Returns the balance formatted as "xx.xx PLN".

---

## Contribution 🤝

Feel free to submit pull requests with improvements and suggestions.  
This project was created for educational purposes and to improve Python skills! 🌟

---