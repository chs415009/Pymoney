# PyMoney: Personal Finance Management Tool

![Python Version](https://img.shields.io/badge/python-3.6+-blue.svg)
![Project](https://img.shields.io/badge/Project-Academic-green.svg)

**PyMoney** is a command-line personal finance management application developed as an academic project in Python. This application demonstrates fundamental programming concepts including data structures, file handling, and command-line interface design.

## 🌟 Features

- **Command-line Interface**: Demonstrates text-based user interaction
- **Transaction Management**: Add, view, and delete financial transactions
- **Category System**: Hierarchical category structure for expense organization
- **Search Functionality**: Filter transactions by category
- **Data Persistence**: File I/O operations for saving and loading data
- **Error Handling**: Input validation with user feedback

## 📥 How to Run

1. Download the script from:
   ```
   https://github.com/chs415009/Pymoney/blob/main/Pymoney.py
   ```
2. Run in any Python environment (version 3.6 or higher)
   ```
   python Pymoney.py
   ```

## 🚀 Usage Guide

### First-time Setup
When launching PyMoney for the first time, you'll be prompted to enter your initial balance:

```
How much money do you have? 1000
```

If you enter an invalid value, the system will default to 0.

### Available Commands

| Command | Description | Example |
|---------|-------------|---------|
| `add` | Add new transaction(s) | `add 2020-01-01 breakfast -50` |
| `view` | Display all transactions | `view` |
| `view categories` | Show category hierarchy | `view categories` |
| `delete` | Remove a transaction | `delete 3` |
| `find` | Search by category | `find food` |
| `exit` | Save and quit application | `exit` |

## 📖 Detailed Usage Instructions

### Category Management
PyMoney uses a hierarchical category system to help organize your finances. View the built-in categories:

```
> view categories
```

![Category View Example](./readme%20pics/3%20view%20cat.png)

### Adding Transactions
Add transactions using the following format:
```
add [date] [description] [amount]
```

For example:
```
> add 2023-05-10 lunch -120
```

Add multiple transactions at once:
```
> add 2023-05-10 lunch -120 2023-05-10 transportation -30
```

![Add Transaction Example](./readme%20pics/4%20add.png)

### Viewing Transactions
Display all recorded transactions and current balance:
```
> view
```

![View Transactions Example](./readme%20pics/6%20view.png)

### Deleting Transactions
Remove a transaction by referencing its index number:
```
> delete 2
```

The index numbers are displayed when using the `view` command.

![Delete Transaction Example](./readme%20pics/7%20delete.png)

### Finding Transactions
Search for transactions by category:
```
> find food
```

This will display all transactions under the specified category, including its subcategories.

![Find Transactions Example](./readme%20pics/9%20find.png)

### Exiting the Application
To save your changes and exit:
```
> exit
```

**Important**: Changes are only saved when exiting through this command.

## 🔧 Technical Implementation

- **Data Structures**: Uses lists and dictionaries to organize financial data
- **File I/O**: Implements text file reading/writing for data persistence
- **String Parsing**: Demonstrates input parsing and validation
- **Error Handling**: Shows techniques for graceful error management

## 🎓 Learning Outcomes

This academic project demonstrates proficiency in:

- Python programming fundamentals
- Command-line application development
- File handling and data persistence
- Input validation and error handling
- Data organization and retrieval techniques

## 📚 Academic Context

This project was developed as part of a Python Programming course. The assignment focused on applying programming concepts to create a practical utility application with data persistence capabilities.

## 🔄 Potential Extensions

- Data visualization for expense analysis
- Budget setting functionality
- Statistical analysis of spending patterns
- Enhanced reporting capabilities

---

**PyMoney** - A Python academic project demonstrating fundamental programming concepts through practical application.
