# Pymoney: Personal Finance Management Tool

![Python Version](https://img.shields.io/badge/python-3.6+-blue.svg)
![Project](https://img.shields.io/badge/Project-Academic-green.svg)

**Pymoney** is a command-line personal finance management application developed as an academic project in Python. This tool helps users track expenses, categorize transactions, and monitor their financial status with a simple yet powerful interface.

## 🌟 Features

- **Command-line Interface**: Intuitive text-based user interaction
- **Transaction Management**: Add, view, and delete financial transactions
- **Hierarchical Category System**: Organize expenses with nested categories
- **Advanced Search**: Filter transactions by category and subcategories
- **Data Persistence**: Automatic saving and loading of user data
- **Error Handling**: Robust input validation with helpful feedback

## 📥 Installation

1. Download the script:
   ```
   https://github.com/chs415009/Pymoney/blob/main/Pymoney.py
   ```
2. Run in any Python environment (version 3.6 or higher):
   ```
   python Pymoney.py
   ```

## 🚀 Usage Guide

### First-time Setup
When launching Pymoney for the first time, you'll be prompted to enter your initial balance:

```
How much money do you have? 1000
```

### Available Commands

| Command | Description | Example |
|---------|-------------|---------|
| `add` | Add new transaction(s) | `add food meal breakfast -50` |
| `view` | Display all transactions | `view` |
| `view categories` | Show category hierarchy | `view categories` |
| `delete` | Remove a transaction | `delete 3` |
| `find` | Search by category | `find food` |
| `exit` | Save and quit application | `exit` |

## 📖 Detailed Usage with Examples

### Category Management
View the built-in category hierarchy:

```
> view categories
```

![Category View Example](./readme%20pics/3%20view%20cat.png)

### Adding Transactions
Add transactions using the following format:
```
add [category] [description] [amount]
```

For example:
```
> add food meal lunch -120
```

Add multiple transactions at once:
```
> add food meal lunch -120, transportation bus fare -30
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

- **Object-Oriented Design**: Uses classes (Record, Records, Categories) for data management
- **Recursive Algorithms**: Implements category hierarchy traversal and filtering
- **File I/O**: Handles data persistence through structured text files
- **Error Handling**: Implements comprehensive exception handling
- **Command Parsing**: Features intuitive command interpretation system

## 🎓 Learning Outcomes

This academic project demonstrates proficiency in:

- **Python Programming**: Core language features, data structures, control flow
- **Object-Oriented Programming**: Classes, encapsulation, properties
- **File Handling**: Data persistence, text file operations
- **User Interface Design**: Command-line interface, user experience
- **Input Validation**: Error checking, exception handling, feedback systems

## 🚀 Potential Extensions

- Data visualization for expense analysis
- Budget setting functionality
- Statistical analysis of spending patterns
- GUI development
- Export to CSV/Excel

---

**Pymoney** - A Python academic project demonstrating fundamental programming concepts through a practical financial management application.
