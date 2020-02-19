run = True
number = int(input("What is your number? "))
power = int(input("What is the power? "))
sum = 0


while run:
    if power == 0: # this is the finish point
        print("There you go:", sum)
        break
    elif sum == 0: # this is the starting point
        sum = number * number
        power -= 1
    else: # the rest is done here
        sum = sum * number
        power -= 1
