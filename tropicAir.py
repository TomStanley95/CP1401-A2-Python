# I think they should be global variables due to the way Im going to code this program
# orders keeps a track of all orders, whereas currentOrder tracks the prices for an individual order
orders = []
currentOrder = [0, 0, 0]


def getUserName():
    # Gets the users name and welcomes them to the ordering system, returns name to the main() variable of userName
    step = str("name")
    choice = str(input("Please enter your name:"))
    choice = choice.replace(" ", "")
    name = str(errorCheck(step, choice))
    print("\nWelcome " + str(name) + " to the tropic airlines ordering system")
    return name


def mainMenu(userName):
    # This function is the main menu for the program takes the username as input and returns the user choice
    # to the main() variable of userChoice
    step = str("mainMenu")
    print("\nTropic Airline ticket Ordering System")
    print("\n(I)nformation \n(O)rder ticker \n(E)xit")
    choice = str(input("Please make a menu selection:"))
    choice = choice.lower()
    choice = choice.replace(" ", "")
    choice = errorCheck(step, choice)
    if choice == "i":
        print("\nThank you for choosing Tropical Airlines for your air travel needs.\n"
              "You will be asked questions regarding what type of ticket you would "
              "like to purchase as well as destination information.\n"
              "We also offer 50% discounted fares for children.")
        print("\nTropic Airline ticket Ordering System")
        print("\n(I)nformation \n(O)rder ticker \n(E)xit")
        choice = str(input("Please make a menu selection:"))
        choice = choice.lower()
        choice = choice.replace(" ", "")
    if choice == "e":
        final(userName)
    if choice == "o":
        return choice


def traveler(userName):
        # This function determines if the ticket is for another person if so gets their name, takes userName as input
        # returns anotherPerson to main()
        step = str("traveler")
        print("\n" + userName + ", is this ticket for:")
        print("\n(Y)ou \n(S)omeone else")
        choice = str(input("Please make a menu selection:"))
        choice = choice.lower()
        choice = choice.replace(" ", "")
        choice = errorCheck(step, choice)
        if choice == "s":
            step = str("another")
            anotherPerson = str(input("\nEnter the name of the person travelling:"))
            anotherPerson = anotherPerson.replace(" ", "")
            choice = anotherPerson
            anotherPerson = str(errorCheck(step, choice))
            return anotherPerson
        else:
            anotherPerson = str("No")
            return anotherPerson


def returnTrip():
    # asks the user if it is a return trip, returns the boolean value tripReturn to the main() variable of returnType
        step = str("returnTrip")
        print("\nIs this a return trip(R) or One-Way(O)?")
        choice = str(input("Please make a menu selection:"))
        choice = choice.lower()
        choice = choice.replace(" ", "")
        choice = errorCheck(step, choice)
        if choice == "r":
            tripReturn = True
            return tripReturn
        else:
            tripReturn = False
            return tripReturn


def destination(returnType):
    # Determines the cost of travelling to a destination selected by the user, takes the boolean value
    # of returnType as input and outputs to the global variable of the list currentOrder
    # returns the value of destination to the variable tripLocation in main()
        step = str("destination")
        cairns = int(400)
        sydney = int(575)
        perth = int(700)
        if returnType == True:
            tripType = str('return')
        else:
            tripType = str('one-way')
        print("\nPlease select the destination for your " +
              tripType + " trip.Fare prices are listed below.\n"
                         '(C)airns -$'+str(cairns)+'\n(S)ydney - $'+str(sydney)+'\n(P)erth - $'+str(perth))

        choice = str(input("Please make a menu selection:"))
        choice = choice.lower()
        choice = choice.replace(" ", "")
        choice = errorCheck(step, choice)
        if choice == "c":
            currentOrder[0] = cairns
            destination = str("Cairns")
            return destination
        elif choice == "s":
            currentOrder[0] = sydney
            destination = str("Sydney")
            return destination
        elif choice == "p":
            currentOrder[0] = perth
            destination = str("Perth")
            return destination


def fareClass():
    # Determines the cost of the flight class, returns a value to the global  list variable currentOrder
    # returns the variable seatClass to the main() variable of seatClass
    step = str("fare")
    business = int(275)
    economy = int(25)
    frugal = int(0)
    print("Please choose the type of fare. Fees are displayed below and are in addition to the basic fare\n"
          "Please note choosing frugal means you will not be offered a seat choice.")
    print('(B)usiness - $' + str(business) + '\n(E)conomy - $' + str(economy) + '\n(F)rugal - $' + str(frugal))
    choice = str(input("Please make a menu selection:"))
    choice = choice.lower()
    choice = choice.replace(" ", "")
    choice = errorCheck(step, choice)
    if choice == "b":
        currentOrder[1] = business
        fareClass = str("Business")
        return fareClass
    elif choice == "e":
        currentOrder[1] = economy
        fareClass = str("Economy")
        return fareClass
    elif choice == "f":
        currentOrder[1] = frugal
        fareClass = str("Frugal")
        return fareClass


def seatType(seatClass):
    # Takes seatClass as input ,Asks the user what type of seat they want
    # return a value to the global variable currentOrder , returns the variable seatType to main()
    # variable of seat
    step = str("seat")
    window = int(75)
    aisle = int(50)
    middle = int(-25)
    if seatClass != "Frugal":
        print("Please choose the seat type. Choosing the middle seat will deduct 25 from the total fare.")
        print('(W)indow -$' + str(window) + '\n(A)isle-$' + str(aisle) + '\n(M)iddle -$' + str(middle))
        choice = str(input("Please make a menu selection:"))
        choice = choice.lower()
        choice = choice.replace(" ", "")
        choice = errorCheck(step, choice)
        if choice == "w":
            currentOrder[2] = window
            seatType = str("Window")
            return seatType
        elif choice == "a":
            currentOrder[2] = aisle
            seatType = str("Aisle")
            return seatType
        elif choice == "m":
            currentOrder[2] = middle
            seatType = str("Middle")
            return seatType
    else:
        currentOrder[2] = 0
        seatType = str("None-Frugal selected")
        return seatType


def age():
    # Determines the age of the user, returns age to the main() variable userAge
    step = str("age")
    travelAge = int(input("\nHow old is the person travelling? Travellers under 16 years old will receive a 50% discount"
                    " for the fare:"))
    choice = travelAge
    travelAge = errorCheck(step, choice)
    return travelAge


def ticketFor(userName, anotherPerson):
    # outputs who the ticket is for , takes userName and anotherPerson as input
    if anotherPerson == "No":
        print('\nTicket for: ' + userName)
    else:
        print('\nTicket for: ' + anotherPerson)


def listCosts(returnType, tripLocation, seatClass, seat, userAge):
    # lists the costs of the ticket and other info, takes returnType, tripLocation, seatClass, seat and userAge as input
    # uses the global variable currentOrder for values
    if returnType == True:
        print(str(tripLocation) + '(return)' + '-$' + str(currentOrder[0]))
    else:
        print(str(tripLocation) + '-$' + str(currentOrder[0]))
    print(str(seatClass) + '-$' + str(currentOrder[1]))
    print('Seat ' + str(seat) + '-$' + str(currentOrder[2]))
    if userAge < 16:
        print('Age-' + str(userAge) + ' (eligible for child ticket)')
    else:
        print('Age-' + str(userAge) + ' (not eligible for child ticket)')


def totalCost(userAge):
    # Calculates the total cost and applies a discount if necessary, takes userAge as an input and appends the value
    # in the global variable orders
    discount = .5
    # discount of 50% = .5
    if userAge < 16:
        fareTotal = sum(currentOrder) - (sum(currentOrder) * discount)
        print('\nTotal price:$' + str(fareTotal))
        orders.append(fareTotal)
    else:
        fareTotal = sum(currentOrder)
        print('\nTotal price:$' + str(fareTotal))
        orders.append(fareTotal)


def final(userName):
    # This function creates the message when a user selects (E)xit, takes userName as input and calls the values
    # from the global variables to create the message.
    ordersString = []
    length = len(orders)
    finalTotal = ' $' + str(sum(orders))
    if length > 1:
        for x in range(0, length):
            ordersString.append('$' + str(orders[x]))
        print("\n" + userName + ', your orders are: ' + str(ordersString).replace("[", "")
              .replace("]", "").replace("'", "") +
              '. Your final total is:' +
              finalTotal +
              ' .Thank you for visiting Tropical Airlines')
        quit()
    else:
        ordersString = ['$' + str(orders).strip("[]").strip("''")]
        print("\n" + userName + ', your order is: ' + str(ordersString).replace("[", "").replace("]", "")
              .replace("'", "") +
              '. Your final total is:' +
              finalTotal +
              ' .Thank you for visiting Tropical Airlines')
        quit()


def main():
    # the controller of the program many value are stored here and every function but final(userName) is called here
    userName = getUserName()
    userChoice = mainMenu(userName)
    while userChoice != "e":
        anotherPerson = traveler(userName)
        returnType = returnTrip()
        tripLocation = destination(returnType)
        seatClass = fareClass()
        seat = seatType(seatClass)
        userAge = age()
        print("\nCalculating fare...\n")
        ticketFor(userName, anotherPerson)
        listCosts(returnType, tripLocation, seatClass, seat, userAge)
        totalCost(userAge)
        userChoice = mainMenu(userName)


def errorCheck(step, choice):
    # error checking function, takes step and user input as choice and returns user input back to the function that
    # called it, step is assigned locally in each function.
    if step == "name":
        while choice == "":
            name = str(input("Error!\nPlease enter your name:"))
            name = name.replace(" ", "")
            return name
        return choice
    elif step == "mainMenu":
        while choice != "i" and choice != "o" and choice != "e":
            choice = str(input("\nError! Please make a valid menu selection:"))
            choice = choice.lower()
            choice = choice.replace(" ", "")
            return choice
        return choice
    elif step == "traveler":
        while choice != "y" and choice != "s":
            choice = str(input("Error!\nPlease make a valid menu selection:"))
            choice = choice.lower()
            choice = choice.replace(" ", "")
            return choice
        return choice
    elif step == "another":
        while choice == "":
            choice = str(input("\nError!\nPlease enter the name of person travelling?:"))
            choice.replace(" ", "")
            return choice
        return choice
    elif step == "returnTrip":
        while choice != "r" and choice != "o":
            choice = str(input("Error!\nPlease make a valid menu selection:"))
            choice = choice.lower()
            choice = choice.replace(" ", "")
            return choice
        return choice
    elif step == "destination":
        while choice != "c" and choice != "s" and choice != "p":
            choice = str(input("Error!\nPlease make a correct menu selection:"))
            choice = choice.lower()
            choice = choice.replace(" ", "")
            return choice
        return choice
    elif step == "fare":
        while choice != "b" and choice != "e" and choice != "f":
            choice = str(input("Error!, Please make a valid menu selection:"))
            choice = choice.lower()
            choice = choice.replace(" ", "")
            return choice
        return choice
    elif step == "seat":
        while choice != "w" and choice != "a" and choice != "m":
            choice = str(input("Error!, Please make a valid menu selection:"))
            choice = choice.lower()
            choice = choice.replace(" ", "")
            return choice
        return choice
    elif step == "age":
        while choice < 0 or choice >= 90:
            choice = int(input("Error! Invalid value\nPlease enter a valid value"))
            return choice
        return choice


main()
