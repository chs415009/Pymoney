#!/usr/bin/env python
# coding: utf-8

# In[2]:


import sys

class Record:

    def __init__(self, category, description, amount):
        """Represent info of a record."""
        self._category = category
        self._description = description
        self._amount = amount
        
    @property
    def category(self): return self._category
    
    @property
    def description(self): return self._description

    @property
    def amount(self): return self._amount

    

class Records:
    
    def __init__(self):
        """Represent a list of all the 'Record's and the initial amount of money."""
        self._initial_money, self._records = self._initialize()

        
    def _initialize(self):
        """create or read a list of all the 'Record's and the initial amount of money."""
        initial_money = 0
        records = []

        #讀取上次存取紀錄，若無紀錄則初始化
        try:
            with open('records.txt', 'r') as fh:
                print('Welcome back!')
                initial_money = int(fh.readline())
                for l in fh.readlines():
                    records.append( Record(l.split()[0], l.split()[1], int(l.split()[2])) )
                
        except (FileNotFoundError, ValueError):
            try:
                initial_money = int(input('How much money do you have?\n'))
                
            except ValueError:
                print('Invalid value for money. Set to 0 by default.')
                initial_money = 0

        return initial_money, records

    
    def add(self, input_record, categories):
        """add new contents to the records."""
        #分割輸入的字串，再利用Record()分別記錄各自收支項目
        try:       
            new_records=[]
            for item in input_record.split(', '):                
                new_records.append(item.split())
                
            for record in new_records:                       
                #檢查category是否存在
                if categories.is_category_valid(item.split()[0]) == False:
                    sys.stderr.write('The specified category is not in the category list.\nYou can check the category list by command "view categories".\nFail to add a record.\n')
                else:
                    self._records.append( Record(record[0], record[1], int(record[2])) )
                
        except IndexError:
            sys.stderr.write('The format of a record should be like this:            meal breakfast -50.\nFail to add a record.\n')
        except ValueError:
            sys.stderr.write('Invalid value for money.\nFail to add a record.\n')

            
    def view(self):
        """View all the records info and total money."""
        print('Category        Description          Amount')
        print('=============== ==================== ======')
        
        total_money = self._initial_money
        for record in self._records:            
            total_money += record.amount            
            print(f'{record.category:<15} {record.description:<20} {record.amount:<}')
            
        print('===========================================')
        print(f'Now you have {total_money} dollars.\n')

        
    def delete(self, delete_record):
        """Delete the specific record by selecting order from 'view'."""
        try:
            #利用輸入的數字選擇要刪除records內容的位置            
            minus = int(self._records[int(delete_record)].amount)
            self._records.pop(int(delete_record))
            self._initial_money -= minus

        except (ValueError, IndexError):
            print('Invalid format. Fail to delete a record.')

            
    def find(self, target_categories):
        if target_categories is None:
            sys.stderr.write('Invalid input. Please enter a valid category name.\n')
            return
        
        #印出篩選後結果
        print(f'Here\'s your expense and income records under category "{category}" :')
        print('Category        Description          Amount')
        print('=============== ==================== ======')

        total_amount = 0
        for record in self._records:
            if record.category in target_categories:
                total_amount += record.amount
                if record.amount >= 0:
                    print(f'{record.category:<15} {record.description:<20} {record.amount:<}')
                else:
                    print(f'{record.category:<15} {record.description:<20} {record.amount:<}')

        print('===========================================')
        print(f'The total amount above is {total_amount}.')

           
    def save(self):
        with open('records.txt', 'w') as fh:
            fh.write(f'{self._initial_money}\n')
            
            #將record_list的內容加上newline以方便後續讀取 若已有newline則不重複加上
            w_records = []
            
            for record in self._records:
                fh.write(f'{record.category} {record.description} {record.amount}\n')


class Categories:

    def __init__(self):
        """Set the nested category list."""
        self._categories = ['expense', ['food', ['meal', 'snack', 'drink'], 'transportation', ['bus', 'railway']], 'income', ['salary', 'bonus']]

        
    def view(self, categories = None, order = -1):
        """Represent to view the nested categories."""        
        if categories == None:
            categories = self._categories
                
        if type(categories) in {list}: 
            for i in categories: 
                self.view(i, order + 1)
        else: print(f'{"  "*order}-{categories}')
        
                
    def is_category_valid(self, category, categories = None):
        """Determine whether the category exist."""
        if categories is None:
            categories = self._categories
            
        if category in categories : 
            return True        
        else:
            error = 0
            for i in categories:

                if type(i) in {list}:
                    if self.is_category_valid(category, i) != True:
                        error = 1
                    else:
                        return True

            if error == 1 :
                return False 

            
    def find_subcategories(self, category):
        """Determine the nested category of 'find'."""
        def find_subcategories_gen(category, categories, found=False):            
            if type(categories) == list:  
                for index, child in enumerate(categories):
                    
                    yield from find_subcategories_gen(category, child, found)
                    if child == category and index + 1 < len(categories) and type(categories[index + 1]) == list:                        
                        yield from find_subcategories_gen(category, categories[index + 1], True)
            else:  
                if categories == category or found:
                    yield categories

        return list(find_subcategories_gen(category, self._categories))



categories = Categories()
records = Records()

while True:
    command = input('\nWhat do you want to do (add / view / delete / view categories / find / exit) ? ')
    
    if command == 'add':
        input_record = input('Add some expense or income records with category, description, and amount (separate by spaces): \n(cat1 desc1 amt1, cat2 desc2 amt2, cat3 desc3 amt3, ...)\n')
        records.add(input_record, categories)
        
    elif command == 'view':
        records.view()
        
    elif command == 'delete':
        delete_record = input('Which record do you want to delete? \n(Enter "0" for the first record of "view", "1" for the second...)\n')
        records.delete(delete_record)
        
    elif command == 'view categories':
        categories.view()
        
    elif command == 'find':
        category = input('Which category do you want to find? ')
        target_categories = categories.find_subcategories(category)
        records.find(target_categories)
        
    elif command == 'exit':
        records.save()
        break
        
    else:
        sys.stderr.write('Invalid command. Try again.\n')


# In[ ]:




