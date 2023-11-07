#  countdown program without carriage return charecter 
import time

def countdown(seconds):
    for i in range(seconds, 0, -1):
        print(f"Countdown: {i} seconds")#, end="\r"
    print("Countdown: Time's up!")
    time.sleep(1)
countdown(5)
                #The time.sleep() function is a feature/tool  introduces a delay or pause in the execution of a program or script. In the case of time.sleep(1), it pauses the execution for 1 second.The time.sleep() function is useful in scenarios where you want to introduce a delay or wait period between specific actions or operations in your code.
                #  using excessive or unnecessary sleep statements can negatively impact the performance and responsiveness of your code. It's generally recommended to use it sparingly and only when needed.

# output
# Countdown: 5 seconds
# Countdown: 4 seconds
# Countdown: 3 seconds
# Countdown: 2 seconds
# Countdown: 1 seconds
# Countdown: Time's up!


for i in range(5,0,-1):
        print(i)
# but what is wrong with this ?
# for i in range(5, 0):
#     print(i)
#  the loop doesn't run because the range is empty.
# why   - range(5,0)- is not generating any sequence ?
# The behavior you're observing is due to how the range() function works in Python. When you use range(5, 0), it doesn't generate a sequence because the start value (5) is greater than or equal to the end value (0). In such cases, the range is considered empty, and no sequence of numbers is generated.
# The range() function generates a sequence of numbers that starts from the first argument and goes up to, but not including, the second argument. In your case, since the start value (5) is greater than or equal to the end value (0), there are no numbers within that range to generate.
# for i in range(5, 0, -1):
#     print(i)


#  countdown program with carriage return charecter 
import time

def countdown(seconds):
    for i in range(seconds, 0, -1):
        print(f"Countdown: {i} seconds", end="\r")
        time.sleep(1)
    print("Countdown: Time's up!")

countdown(5)
# output
# Countdown: Time's up!
