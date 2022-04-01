
#-----------------------Defining function to handle every return action-----------------------------
def return_action(stock_list):
    return_list = []
    count = 0
    #getting bookID of book from user which user wants to return 
    return_id = input('Enter ID of book you want to return:')

    #getting number of days user had the book for
    return_days = input('How many days has it been since you borrowed the book?\n')

    try:
        return_days = int(return_days)

    except:
        print('='*80)
        print('\t\t\t Days are accepted only in integer form.')
        print('='*80)
        return return_action(stock_list)
    
    #to check if stock ever had requested book that is to be returned
    for each_value in stock_list:
        
        if (each_value[0] == return_id):

            #showing message that book is accepted and increasing quantity of returned book
            print('\n')
            print('='*80)
            print('\t\t\tBook is accepted.')
            print('='*80)
            print('\n')

            #increasing quantity
            quantity = int(each_value[3]) + 1
            each_value[3] = str(quantity)

            #creating loop to append returned books details in list
            for each in each_value:
                return_list.append(each)
                
            #checking number of days and adding fine accordingly
            if (int(return_days) < 10):
                fine = 0
                

            elif (int(return_days) > 10):
                fine = (2/100)*(return_days - 10)
            #appending fine to list
            return_list.append(float(fine))
                
        #notifying user that book  cannot be accepted if book was never in stock 
        elif (each_value[0] != return_id):
            count = count + 1
            #showing  message when book which was never in stock is returned
            if (count == len(stock_list)):
                print('='*80)
                print('\t\t\tBook cannot be accepted.')
                print('='*80)
                return return_action(stock_list)
                    
    return return_list
    return fine

#-------------------------------------to create receipt of returned books--------------------
def return_receipt(returnedbooks_list,date_time):
    #taking names as input and checking if name has other characters than alphabet
    fname = input('Enter your first name:')
    lname = input('Enter your last name:')
    name = fname + ' ' + lname
    if (fname.isalpha() == True and lname.isalpha() == True):
        receiptfile= open(fname + "'s Return Receipt.txt", "a")
        receiptfile.write('-'*90+'\n\n')
        receiptfile.write('\t\t\t' + " Return Receipt:")
        receiptfile.write('\n\n')
        receiptfile.write("Date and time of book returned:" + '\t\t' +  str(date_time))
        receiptfile.write('\n\n')
        receiptfile.write("Name of returner:" + name)
        receiptfile.write('\n\n')
        receiptfile.write("Book ID \t\t Book Name \t\t\tPrice \t\t\tFine")
        receiptfile.write('\n\n')
        sum_ = 0
        for value in returnedbooks_list:
            value[-2] = float(value[-2].replace('$',""))
            sum_ = value[-2] + sum_ + value[-1]
            sum_ = round(sum_,2)
            receiptfile.write(str(value[0]) + '\t\t\t' + str(value[1]) + '\t\t\t' +'$' + str(value[-2]) + '\t\t' + '$' + str(value[-1])+ '\n')
        receiptfile.write('\n\n')
        receiptfile.write('-'*90)
        receiptfile.write('\n')
        receiptfile.write("Total Price:" + '\t\t\t\t\t\t' + '$' + str(sum_))
        receiptfile.write('\n\n')
        receiptfile.write("Note: Only those Books returned after 10 days are fined.")
        receiptfile.write('\n\n')
        receiptfile.write('-'*90)
        receiptfile.close()
        #showing receipt in shell
        print('\n')
        print('='*80)
        print('\t\t Here is your receipt.')
        return_inshell = open(fname + "'s Return Receipt.txt",'r')
        for line in return_inshell:
            line = line.replace('\n','')
            print(line)
        print('\n')
        print('\t\t\tThankyou for returning the books.')
        print('='*80)
           
    else:
        print('='*80)
        print('\t \t \tThis name cannot be accepted.')
        print('='*80)
        return returnreceipt(returnedbooks_list,date_time)
