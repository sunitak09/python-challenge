import os
import csv

csvpath = os.path.join('PyBank/Resources', 'budget_data.csv')

#The total number of months included in the dataset. 
# To calculate total month in column 1, count each row and sum total will give total months.

month_counter = 0

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)

    for row in csvreader:
        month_counter = month_counter + 1




    
#The net total amount of "Profit/Losses" over the entire period
#Add up all the values in the profit/loss column to count total amount. 
# counting will start from row 1 since row 0 is for header.

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)

    total_changes = 0
    net_profit = 0
    net_loss = 0
    profit_counter = 1
    loss_counter = 1
    total_sum = 0
    current_min = 0
    current_max = 0
     
# calculte the positive values as profit and negative values as loss which will give total profit/loss
 #avg change calc: sum of (current data - previous data)/n-1.   
    
    for row in csvreader:
        total_changes = total_changes + int(row[1])

        if int(row[1]) >= 0:
            net_profit = net_profit + int(row[1])
            profit_counter = profit_counter + 1
        else:
            net_loss = net_loss + int(row[1])
            loss_counter = loss_counter + 1
        
    
    counter = 1

    with open(csvpath) as csvfile:
        csvreader = csv.reader(csvfile, delimiter=",")
        csv_header = next(csvreader)
        
#to hold the value in one cell and verify from next, assign both counting cell as row
#for calculating average change, subtract 2nd row from first row  in the profit/loss coulumn and calculating average as total sum/n-1, give the resultant average change.
#

        for row in csvreader:
            if(counter == 1):
                current_row = row
                previous_row = row

            else:
                current_row = row 
                total_sum = total_sum + int(current_row[1]) - int(previous_row[1])

                if int(current_row[1]) - int(previous_row[1]) > current_max:
                    current_max = int(current_row[1]) - int(previous_row[1])
                    name_max = current_row[0]
                    place_max = current_row[1]
                    

                if int(current_row[1]) - int(previous_row[1]) < current_min:
                    current_min = int(current_row[1]) - int(previous_row[1])
                    name_min = current_row[0]
                    place_min = current_row[1]

                previous_row = current_row

            counter += 1


print("Financial Analysis")
print("-------------------")
print(f"Total Months: {month_counter}")

#Total: $22564198
print(f"Total Changes:  ${total_changes}")

#  Average Change: $-8311.11
print(f"Average Change: ${round(total_sum/(counter - 2),2)}")

#  Greatest Increase in Profits: Aug-16 ($1862002)
print(f"Greatest Increase in Profits: {name_max}  (${current_max}")

 # Greatest Decrease in Profits: Feb-14 ($-1825558)#

print(f"Greatest Decrease in Profits: {name_min} (${current_min})")


#file writing
with open('PyBank_Result.txt', 'w') as f:
    f.write("Financial Analysis \n")
    f.write("------------------- \n")
    f.write(f"Total Months: {month_counter} \n")

    #Total: $22564198
    f.write(f"Total Changes:  ${total_changes} \n")

    #  Average Change: $-8311.11
    f.write(f"Average Change: ${round(total_sum/(counter - 2),2)} \n")

    #  Greatest Increase in Profits: Aug-16 ($1862002)
    f.write(f"Greatest Increase in Profits: {name_max}  (${current_max} \n")

    # Greatest Decrease in Profits: Feb-14 ($-1825558)#

    f.write(f"Greatest Decrease in Profits: {name_min} (${current_min})")
    






