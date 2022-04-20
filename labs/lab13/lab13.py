"""
Name: Ethan Greene
Lab13.py

Problem: Practicing real life application python programming with stocks simulation!

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""

def trade_alert(filename):
    opener = open(filename, "r")
    reader = opener.read()
    splitter = reader.split(" ")
    seconds = 0
    for nums in splitter:
        seconds += 1
        if eval(nums) > 830:
            print("WARNING, trade volume has breached 830 "
                  "per second at timestamp: {}".format(seconds))
        elif eval(nums) == 500:
            print("ALERT, trade volume equals 500 per second at time stamp: {}."
                  " Make sure you are paying attention".format(seconds))
    opener.close()

