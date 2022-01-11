import sys
import random
import datetime

def uniqueId(username, dt):
    print("Unique Id:", random.randint(100000, 999999))
    print("User name:", username)
    print("Date & Time: {}-{}-{} {}:{}:{} {}".format(dt.day, dt.strftime("%b"), dt.year, dt.strftime("%I"), dt.strftime("%M"), dt.strftime("%S"), dt.strftime("%p")))

def main():
    if len(sys.argv)<2:
        print("---Please enter user name---")

    else:
     uniqueId(sys.argv[1], datetime.datetime.now())


if __name__ == "__main__":
    # calling the main function
    main()