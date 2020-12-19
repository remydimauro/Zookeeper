# Save the input in this variable
ticket = input()

# Add up the digits for each half
tickets = list(ticket)
half1 = (int(tickets[0]) + int(tickets[1]) + int(tickets[2]))
half2 = (int(tickets[3]) + int(tickets[4]) + int(tickets[5]))

# Thanks to you, this code will work
if half1 == half2:
    print("Lucky")
else:
    print("Ordinary")
