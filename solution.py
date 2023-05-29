import json
import datetime

# Solution 1: The Basic One  (Using Dictionary)
# ---> It will print only those months in which we have expense or revenue.
def getBalanceSheetSolution1(data):

    # Initialize the balanceSheet dictionary
    balanceSheet = {}

    # Looping through revenceData
    for revenue in data['revenueData']:
        if balanceSheet.get(revenue['startDate']):      # Check if date already exists
            balanceSheet[revenue['startDate']] += revenue['amount']
        else:
            balanceSheet[revenue['startDate']] = revenue['amount']

    # Looping through expenseData
    for expense in data['expenseData']:
        if balanceSheet.get(expense['startDate']):      # Check if date already exists
            balanceSheet[expense['startDate']] -= expense['amount']
        else:
            balanceSheet[expense['startDate']] = -expense['amount']

    balanceSheet = dict(sorted(balanceSheet.items()))   # Sort the balanceSheet

    # Print the headers
    print("Balance Sheet:\n")
    print("Year", end="\t")
    print("Month", end="\t")
    print("Amount")

    # Looping through balanceSheet
    for startDate, amount in balanceSheet.items():
        # ISO Format: "yyyy-mm-ddThh:MM:ssZ"
        print(startDate[0:4], end="\t")
        print(startDate[5:7], end="\t")
        print(amount)


# Solution 2:  (Using Dictionary)
# ---> It will print all the months of a year in which we have expense or revenue. Input file can have any number of years. 
def getBalanceSheetSolution2(data):

    # Initialize the balanceSheet dictionary
    balanceSheet = {}
    minYear = datetime.datetime.now().year + 1
    maxYear = 0
    maxMonth = 0

    # Looping through revenceData
    for revenue in data['revenueData']:
        currentYear = int(revenue['startDate'][0:4])
        currentMonth = int(revenue['startDate'][5:7])

        if currentYear < minYear:      # Check for minYear
            minYear = currentYear
        if currentYear == maxYear and currentMonth > maxMonth:
            maxMonth = currentMonth
        if currentYear > maxYear:      # Check for maxYear
            maxYear = currentYear
            maxMonth = currentMonth

        dateString = str(currentYear) + " - " + str(currentMonth)
        if balanceSheet.get(dateString):      # Check if date already exists
            balanceSheet[dateString] += revenue['amount']
        else:
            balanceSheet[dateString] = revenue['amount']

    # Looping through expenseData
    for expense in data['expenseData']:
        currentYear = int(expense['startDate'][0:4])
        currentMonth = int(expense['startDate'][5:7])

        if currentYear < minYear:      # Check for minYear
            minYear = currentYear
        if currentYear == maxYear and currentMonth > maxMonth:
            maxMonth = currentMonth
        if currentYear > maxYear:      # Check for maxYear
            maxYear = currentYear
            maxMonth = currentMonth

        dateString = str(currentYear) + " - " + str(currentMonth)
        if balanceSheet.get(dateString):      # Check if date already exists
            balanceSheet[dateString] -= expense['amount']
        else:
            balanceSheet[dateString] = -expense['amount']

    # Print the headers
    print("Balance Sheet:\n")
    print("Year", end="\t")
    print("Month", end="\t")
    print("Amount")

    # Looping through Years & Months
    for year in range(minYear, maxYear + 1):
        for month in range(1, 13):
            if (year < maxYear) or (year == maxYear and month <= maxMonth):
                dateString = str(year) + " - " + str(month)
                print(year, end="\t")
                print(month, end="\t")
                if balanceSheet.get(dateString):      # Check if date already exists
                    print(balanceSheet[dateString])
                else:
                    print(0)


# Solution 3: The Efficient One  (Using Array)
# ---> This solution is implemented using array which is efficient than the dictionary one.
def getBalanceSheetSolution3(data):
    minYear = datetime.datetime.now().year + 1
    maxYear = 0
    maxMonth = 0

    # Looping through revenueData
    for revenue in data['revenueData']:
        currentYear = int(revenue['startDate'][0:4])
        currentMonth = int(revenue['startDate'][5:7])
        if currentYear < minYear:      # Check for minYear
            minYear = currentYear
        if currentYear == maxYear and currentMonth > maxMonth:
            maxMonth = currentMonth
        if currentYear > maxYear:      # Check for maxYear
            maxYear = currentYear
            maxMonth = currentMonth

    # Looping through expenseData
    for expense in data['expenseData']:
        currentYear = int(expense['startDate'][0:4])
        currentMonth = int(expense['startDate'][5:7])
        if currentYear < minYear:      # Check for minYear
            minYear = currentYear
        if currentYear == maxYear and currentMonth > maxMonth:
            maxMonth = currentMonth
        if currentYear > maxYear:      # Check for maxYear
            maxYear = currentYear
            maxMonth = currentMonth

    # Returns the index based on currentYear & currentMonth
    def getIndex(currentYear, currentMonth):
        return (currentYear * 12 + currentMonth) - (minYear * 12 + 1)        # Transform everything into month-scale & subtract the 0th index-months

    # Initialize the balanceSheet
    balanceSheet = [0] * ((maxYear - minYear) * 12 + maxMonth)

    # Looping through revenueData
    for revenue in data['revenueData']:
        currentYear = int(revenue['startDate'][0:4])
        currentMonth = int(revenue['startDate'][5:7])
        currentIndex = getIndex(currentYear, currentMonth)
        balanceSheet[currentIndex] += revenue['amount']

    # Looping through expenseData
    for expense in data['expenseData']:
        currentYear = int(expense['startDate'][0:4])
        currentMonth = int(expense['startDate'][5:7])
        currentIndex = getIndex(currentYear, currentMonth)
        balanceSheet[currentIndex] -= expense['amount']

    # Print the headers
    print("Balance Sheet:\n")
    print("Year", end="\t")
    print("Month", end="\t")
    print("Amount")

    # Looping through Years & Months
    for year in range(minYear, maxYear + 1):
        for month in range(1, 13):
            if (year < maxYear) or (year == maxYear and month <= maxMonth):
                index = getIndex(year, month)
                print(year, end="\t")
                print(month, end="\t")
                print(balanceSheet[index])



def main():
    jsonFile = open("1-input.json")
    jsonData = json.load(jsonFile)
    getBalanceSheetSolution1(jsonData)

if __name__ == '__main__':
    main()
