# PyMoney: Personal Finance Management Tool

![Python Version](https://img.shields.io/badge/python-3.6+-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)

**PyMoney** is a lightweight, command-line personal finance management application written in Python. It provides a simple yet powerful way to track your expenses, categorize transactions, and manage your budget effectively.

## 🌟 Features

- **Simple CLI Interface**: Easy-to-use command line interface for quick interaction
- **Transaction Management**: Add, view, and delete financial transactions
- **Category System**: Hierarchical category structure for detailed expense tracking
- **Search Functionality**: Find transactions by category or other criteria
- **Data Persistence**: Automatic saving of transaction data between sessions
- **User-friendly Validation**: Robust error handling with clear user feedback

## 📥 Installation

### Option 1: Direct Download
1. Download the script directly from:
   ```
   https://github.com/chs415009/Pymoney/blob/main/Pymoney.py
   ```
2. No additional dependencies required - just pure Python!

### Option 2: Clone Repository
```bash
git clone https://github.com/chs415009/Pymoney.git
cd Pymoney
python Pymoney.py
```

## 🚀 Quick Start Guide

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

- **Data Storage**: Transaction data is stored in a plaintext file for easy access and portability
- **Error Handling**: Comprehensive input validation with user-friendly error messages
- **Category Structure**: Intelligent hierarchical category implementation

## 🛠️ Future Development Plans

- Data visualization for expense analysis
- Budget setting and tracking
- Import/export functionality for CSV files
- Multi-account support
- Financial goal tracking

## 📜 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 👨‍💻 About the Developer

PyMoney was developed as a demonstration of Python programming skills and software architecture design. The application showcases:

- Clean code organization
- Object-oriented design principles
- Effective error handling
- User experience considerations
- Data persistence implementation

---

**PyMoney** - Simplifying personal finance management through elegant code and practical functionality.
