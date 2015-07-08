"""
sales_report.py - Generates sales report showing the total number
                  of melons each sales person sold.
"""

salespeople = []
melons_sold = []

f = open("sales_report.txt")
for line in f: # loop over each line in the sales report "f"
    line = line.rstrip() # strip each light of right blank space
    entries = line.split("|") # split each line on the pipe
    salesperson = entries[0] # declare variable saleperson to the first index with is a name in the file
    melons = int(entries[2]) # delcare melons sold by the salesperson as the thrid index

    if salesperson in salespeople: # if this salesperson is is in the list, just add the melon count to thier melons_sold index
        position = salespeople.index(salesperson)
        melons_sold[position] += melons
    else:
        salespeople.append(salesperson) # if this person isnt in the list, add them and thier melon count
        melons_sold.append(melons)


for i in range(len(salespeople)): #print out 
    print "%s sold %d melons" % (salespeople[i], melons_sold[i])
