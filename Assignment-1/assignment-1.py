import sys
import uuid
import time
import datetime

def generate_uniqueId():

    x = uuid.uuid4() # Generate random UUID
    ms = time.time_ns() # time in milliseconds
    return uuid.uuid5(x, str(ms)) # return UUID based on random UUID(x) and milliseconds(ms)

def assignment1(username, dt):
    print("Unique Id:", generate_uniqueId()) # print unique Id
    print("User name:", username) # print user name
    # Print Date and time
    print("Date & Time: {}-{}-{} {}:{}:{} {}".format(dt.day, dt.strftime("%b"), dt.year, dt.strftime("%I"), dt.strftime("%M"), dt.strftime("%S"), dt.strftime("%p")))

def main():
    if len(sys.argv)<2:
        print("---Please enter user name---")

    else:
     assignment1(sys.argv[1], datetime.datetime.now())


if __name__ == "__main__":
    # calling the main function
    main()