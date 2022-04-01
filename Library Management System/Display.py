#--------------------to display Header after entering the system-----------------
def header():
    print('='*80)
    print('\t \t    Welcome to Library Management System. \n \t \tFollow the instructions below for any query')
    print('='*80)

#---------------------to display available books in library-----------------------
def showbooks(stock_list):
    print('These are the available books'+'\n')
    print('| Book ID |\t\tBook Name\t\t| \tWriter\t\t|    Quantity    |   Price')
    for book in stock_list:
        print('|',book[0]," "*(6-len(book[0])),
              '|',book[1]," "*(34-len(book[1])),
              '|',book[2]," "*(20-len(book[2])),
              '|',book[3]," "*(13-len(book[3])),
              '|',book[4]," "*(10-len(book[4])))
        
#--------------------------to display menu for the system----------------------------
def showmenu():
    print('\n')
    print('Enter 1 to Display all available books.')
    print('Enter 2 to Request a book to borrow.')
    print('Enter 3 to Return a borrowed book.')
    print('Enter 4 to Exit the System.')
    print('\n')
    
#-------------------------------to update stock file after the program is run and stock values are changed-----------------------------
def fileupdate(stock_list):
    fileupdate =open('Stock.txt','w')
    for each_item in stock_list:
        each_item[-1] = str(each_item[-1])
        line = ','.join(each_item) + ('\n')
        fileupdate.write(line)
    fileupdate.close()

