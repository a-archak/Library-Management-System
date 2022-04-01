#---------------defining function to handle all borrow action------------
def borrow_action(stock_list):
    borrow_list = []
    count = 0
    #getting bookid of book from user which user wants to borrow
    borrow_id = input('Enter ID of book you want to borrow:')

    #to check if stock has requested book
    for each_value in stock_list:
        if (each_value[0] == borrow_id):

            #to check quantity of requested book
            if(int(each_value[3]) > 0):
                print('\n')
                print('='*80)
                print('\t\t\tBook is available.')
                print('='*80)
                print('\n')

                #decreasing quantity of book that is borrowed
                quantity = int(each_value[3])-1
                each_value[3] = str(quantity)

                #creating loop to append borrowed books details in list
                for each in each_value:
                    borrow_list.append(each)

            #notifying user if quantity of requested book is 0
            elif(int(each_value[3]) <= 0):
                print('\n')
                print('='*80)
                print('Requested book is currently unavailable.')
                print('='*80)
                print('\n')
                
        #notifying user if input id doesnot matches any book ID in library stock
        elif (each_value[0] != borrow_id):
            count = count + 1
            
            if (count == len(stock_list)):
                print('\n')
                print('='*80)
                print('\t\tThe book you are looking for is currently unavailable')
                print('='*80)
                print('\n')
                return borrow_action(stock_list)                       
    return borrow_list

#-------------------------------------to create receipt of borrowed books----------------------------
def borrow_receipt(borrowedbooks_list,date_time):
    #taking names as input and checking if name has other characters than alphabet
    fname = input('Enter your first name:')
    lname = input('Enter your last name:')
    name = fname + ' ' + lname
    if (fname.isalpha() == True and lname.isalpha() == True):
        #creating a receipt file of borrower's name
        receiptfile= open(fname + "'s Borrow Receipt.txt", "a")
        receiptfile.write('-'*90+'\n\n')
        receiptfile.write('\t\t\t' + " Borrow Receipt:")
        receiptfile.write('\n\n')
        receiptfile.write("Date and time of book borrow:" + '\t\t' +  str(date_time))
        receiptfile.write('\n\n')
        receiptfile.write("Name of borrower:" + name)
        receiptfile.write('\n\n')
        receiptfile.write("Book ID \t\t Book Name \t\t\tPrice")
        receiptfile.write('\n\n')
        sum_ = 0
        #iterating through borrowlist and appending list values in file
        for value in borrowedbooks_list:
            value[-1] = float(value[-1].replace('$',""))
            #taking total sum of price
            sum_ = float(value[-1]) + sum_
            sum_ = round(sum_,2)
            receiptfile.write(str(value[0]) + '\t\t\t' + str(value[1]) + '\t\t\t' +'$' + str(value[-1]) + '\t\t' + '\n')
        receiptfile.write('\n\n')
        receiptfile.write('-'*90)
        receiptfile.write('\n')
        receiptfile.write("Total Price:" + '\t\t\t\t\t\t' + '$' + str(sum_))
        receiptfile.write('\n\n')
        receiptfile.write("Note: Books returned after 10 days will be fined.")
        receiptfile.write('\n\n')
        receiptfile.write('-'*90)
        receiptfile.close()
        #showing receipt in shell
        print('\n')
        print('='*80)
        print('\t\t Here is your receipt.')
        #showing report in shell
        borrow_inshell = open(fname + "'s Borrow Receipt.txt",'r')
        for line in borrow_inshell:
            line = line.replace('\n','')
            print(line)
        print('\n')
        print('\t\t\tThankyou for borrowing books from us.')
        print('='*80)
        
    else:
        #if entered name is invalid
        print('='*80)
        print('\t \t \tThis name cannot be accepted.')
        print('='*80)
        return borrow_receipt(borrowedbooks_list,date_time)
