print("Cleaning Procedure starting . . .")
print(".")
print(".")
print(".")

while True:
    
    status_A = input("Agent is in tiles A. This tiles is ______")
    if status_A == "power off":
        print("The agent has finished it work for now.")
        break
    if status_A == "dirty":
        print("Agent is cleaning dirt.")
    
    status_B = input("Going to tiles B. This tiles is ______")
    if status_B == "power off":
        print("The agent has finished it work for now.")
        break
    if status_B == "dirty":
        print("Agent is cleaning dirt.")

    print("Waiting . . .")
    print(".")
    print(".")
    print(".")
    print("Moving to the next tiles . . .")
    print(".")
    print(".")
    print(".")

