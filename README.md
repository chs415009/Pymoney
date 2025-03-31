# ~ Pymoney ~
An account book application written in Python.

# Download:
1. Click below ! <br>
https://github.com/chs415009/Pymoney/blob/main/Pymoney.py

2. Copy the code to execute it in any environment for Python.

# Instructions:
This program utilizes a simple command-line interface to interact with the user. <br>
It allows you to input records, categorize them, and perform various actions on your financial data.<br>

## -- Initial Setup --
__1.__ <br>
<img src="./readme pics/0 input money.png" width="800">

* When you first start the program, you can input the amount of money you already have.<br>
* You can also input a negative number.
<br>

__2.__ <br>
<img src="./readme pics/1 input money X.png" width="800">

* If you input an invalid value, such as "a","@"..., the initial money will be set to 0.
<br>

__3.__ <br>
<img src="./readme pics/2 command X.png" width="800">

* After you complete the setup, you can start using the application by entering one of the commands shown in the image.<br>
(add, view, view categories, find, exit)
<br>

## -- View Categories --
__4.__ <br>
<img src="./readme pics/3 view cat.png" width="800">

* Before recording, you can use "view categories" to see the built-in categories that help identify records you want to add.<br>
* The hierarchical structure represents different levels of those categories.
<br>

## -- Add --
__5.__ <br>
<img src="./readme pics/4 add.png" width="800">

* The "add" command must be entered with a specific format (shown in the image).<br>
* You can add one or multiple records at a time.
<br>

__6.__ <br>
<img src="./readme pics/5 add X.png" width="800">

* If you input the wrong format or wrong category, the system will notice you by messages with red background.
<br>

## -- View --
__7.__ <br>
<img src="./readme pics/6 view.png" width="800">

* The "view" command displays all the details of those records and the total money you have now.
<br>

## -- Delete --
__8.__ <br>
<img src="./readme pics/7 delete.png" width="800">

* The "delete" command allows you to remove your previous records.
* You need to enter the number of the orders shown in "view" to delete the record you want.
<br>

__9.__ <br>
<img src="./readme pics/8 delete X.png" width="800">

* If you enter the number out of the "view" list or not a number, the system will notice you by messages with red background.
<br>

## -- Find --
__10.__ <br>
<img src="./readme pics/9 find.png" width="800">

* The "find" command allows you to view records in specific categories.
* For example, if you enter "food", the result will include all the categories under the level of "food" (meal, snack, drink).
<br>

__11.__ <br>
<img src="./readme pics/10 find X.png" width="800">

* If there are no records in specific categories, it'll show nothing.
* The reult of "find" will also be empty if you don't input the correct category. 
<br>

## -- Exit --
__12.__ <br>
<img src="./readme pics/11 exit.png" width="800">

* The "exit" function is used when you want to save records and close the application.
* To notice, if you don't leave with "exit", the modification won't be saved.
<br>

__13.__ <br>
<img src="./readme pics/12 exit back.png" width="800">

* After the previous "exit", the next time you start will skip setting the initial money with the message "Welcome back!" shown.
<br>

__14.__ <br>
<img src="./readme pics/13 txt.png" width="800">

* This image shows the text file for storing the data of those records. 
