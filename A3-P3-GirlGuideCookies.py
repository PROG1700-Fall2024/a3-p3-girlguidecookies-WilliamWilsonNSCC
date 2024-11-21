#Program 3 – Girl Guide Cookies
#Description:   The organizers of the annual Girl Guide cookie sale event want to raise 
#               the stakes on the number of cookies sold and are offering cool prizes to
#               those guides who go above and beyond in their sales efforts. The organizers
#               want a program to print the guide list and their prizes.

#Student #: William Wilson   
#Student Name: w0457754

#num of guides -int
#Guides Names -list within the 2D list
#Boxes sold -list int
#output names to prices -2D List
#prizes won are between average and totalBoxSold

# xGuides = []
# boxSold = []

# def girlGuides(xGuides, boxSold):
def girlGuides():
    xGuides = []
    boxSold = []
    numOfGuides = int(input("Please input the number of Guides:  "))

    for i in range(numOfGuides):
        while True:
            nameOfGuides = input(f"Please enter the name of Guild # {i+1}: ")
            if nameOfGuides.isalpha():
                break
            else:
                print("You entered an invalid entry, please try again!")

        while True:
            guideSales = input(f"Please enter the number of boxes sold by guide {nameOfGuides}: ")
            if guideSales.isnumeric():
                break
            else:
                print("You did not enter a number!")

        xGuides.append(nameOfGuides)
        boxSold.append(guideSales)

def main():
    # YOUR CODE STARTS HERE, each line must be indented (one tab)

    girlGuides()






    # YOUR CODE ENDS HERE

main()