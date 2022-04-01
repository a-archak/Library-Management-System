#------------Main python file-----------------

#-----------importing required packages and modules--------------------
import datetime
import Borrow
import Display
import Return

#--------------opening main stock file to and storing its contents in list----------
date_time = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")           #provides current date and time

stock_list = []

borrowedbooks_list = []

returnedbooks_list = []

#appending datas from textfile to list
stock = open('Stock.txt','r')
for line in stock:
    line = line.replace('\n','')
    stock_list.append(line.split(','))
stock.close()

#-----------------------working with user input-------------------------
#------creating method for applying response to user input---------------
def userinput():
    Display.showmenu()        #calling showmenu method from Display module inorder to show the menu to users

    choice_raw = input('Enter your choice:')    #asking user to input their choice to further proceed in system

    #exception handling for userinput
    try:
        choice = int(choice_raw)

        #assigning method for user chosen option
        #choice 1 for displaying books
        if(choice == 1):
            Display.showbooks(stock_list)
            return userinput()
        
        #choice 2 for Borrowing book
        elif(choice == 2):
            loop = True
            #creating loop to get multiple input
            while (loop == True):
               #calling borrow_action method from Borrow module to perform borrow action
                borrower_list = Borrow.borrow_action(stock_list)
                
                #appending borrowed book details in list to later pass on receipt function on Borrow module
                borrowedbooks_list.append(borrower_list)

                #asking if user want to borrow more book
                ask = input('Do you want to borrow another book.\n Enter either "yes" or "no" to continue.\n')
                if (ask.lower() == 'yes'):
                    loop = True
                elif(ask.lower() == 'no'):
                    Borrow.borrow_receipt(borrowedbooks_list,date_time)
                    loop = False
                #if user inputs anything except yes and no
                else:
                    print('\n')
                    print('='*80)
                    print('\t \t \t Invalid input found.\n\t\tBill will now be generated.')
                    print('='*80)
                    print('\n')
                    Borrow.borrow_receipt(borrowedbooks_list,date_time)
                    loop = False
                
                #updating file data after transaction
                Display.fileupdate(stock_list)
            return userinput()

        #choice 3 for returning book
        elif(choice == 3):
            #calling run_action method from Return module
            returner_list = Return.return_action(stock_list)
            
            #appending borrowed book details in list to later pass on receipt function on Borrow module
            returnedbooks_list.append(returner_list)
            Return.return_receipt(returnedbooks_list,date_time)
            #updating file data after transaction
            Display.fileupdate(stock_list)
            return userinput()

        #choice 4 for exiting
        elif(choice == 4):
            print('\n')
            print('='*80)
            print('\t \t \tThankyou for visiting.')
            print('='*80)
            print('\n')

        #if user enters numbers other than suggested
        else:
            print('\n')
            print('='*80)
            print('\t \tInvalid input. Enter either 1,2,3 or 4.')
            print('='*80)
            return userinput()

    except:
        print('='*80)
        print('\t \tInvalid input. Enter either 1,2,3 or 4.')
        print('='*80)
        return userinput()

#-----------------------------calling above methods to run the system------------------------------------------
##print(stock_list)
Display.header()          #calling header method from Display module to display header
Display.showbooks(stock_list)       #calling showbooks method from Display module to display available books for transaction
userinput()
