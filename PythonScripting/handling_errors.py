""" Receives inputs as String """
cks = input("Input the amount of cookies for this Party: ")
peeps = input("Input the amount of People for this Party: ")

def party_planner(cookies, people):
    leftovers = None
    num_each = None
    # TODO: Add a try-except block here to
    #       make sure no ZeroDivisionError occurs.
    while True:
        try:
            num_each = int(cookies) // int(people)
            leftovers = int(cookies) % int(people)
            print("{} cookies per person and {} leftovers".format(num_each, leftovers))
            break
        except (TypeError, ValueError):
            print("Input a number instead of a string!")
            break
        except ZeroDivisionError:
            print("Input a number greater than Zero")
            break
        except KeyboardInterrupt:
            print("Program interrupted")
            break

""" Calls the function using the amount of cookies and people """
party_planner(cks, peeps)

"""
Solution developed by Juno - Udacity to this problem
------------
def party_planner(cookies, people):
    leftovers = None
    num_each = None

    try:
        num_each = cookies // people
        leftovers = cookies % people
    except ZeroDivisionError:
        print("Oops, you entered 0 people will be attending.")
        print("Please enter a good number of people for a party.")

    return(num_each, leftovers)
"""
