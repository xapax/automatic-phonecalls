#!python
# ---------------------------------------------------------------------------------------------
#  Python / Skype4Py example that takes a skypename from command line parameter,
#  checks if that skypename is in contact list and if yes then starts a call to that skypename.
#
#  Tested with  Skype4Py version 0.9.28.2 and Skype verson 3.5.0.214


# In order for this script to work you need to download skype4py.
# pip install skype4py
# And also gobject: sudo apt-get install python-gobject

import sys
import Skype4Py
import time
import signal

def usage():
    print "\nUsage:"
    print "First you have to call the number to get the path you need to take to reach your destination."
    print "To find out what numbers or symbols you need to press in ordet to reach your destination."
    print "\n"
    print "--number/user 004607077711188"
    print "--number/user bob.dylan"
    print "--key1 to key10"
    print "\nExample:\n"
    print "python call.py --number/user 004607077711188 --key1 2 --key2 1 --key3 7"
    sys.exit()

help = "--help" in sys.argv

if len(sys.argv) < 2 or help:
    usage()


def handler(signum, frame):
    if(Call):
        Call.Finish()
    sys.exit()

signal.signal(signal.SIGINT, handler)

userNumber = sys.argv[sys.argv.index("--number/user") + 1]
keys = {}
for key in sys.argv:
    numbers = ["1","2","3","4","5","6","7","8","9","10"]
    for nums in numbers:
        if key == "--key" + nums:
            keys["key"+nums] = sys.argv[sys.argv.index("--key"+nums) + 1]


# def signal_handler(signal, frame):
#         print('You pressed Ctrl+C!')
#         # skype.Finish()
#         call.Finish()
#         # CallIsFinished
#         sys.exit(0)
# signal.pause()


# This variable will get its actual value in OnCall handler
CallStatus = 0

# Here we define a set of call statuses that indicate a call has been either aborted or finished
CallIsFinished = set ([Skype4Py.clsFailed, Skype4Py.clsFinished, Skype4Py.clsMissed, Skype4Py.clsRefused, Skype4Py.clsBusy, Skype4Py.clsCancelled]);

def AttachmentStatusText(status):
   return skype.Convert.AttachmentStatusToText(status)

def CallStatusText(status):
    return skype.Convert.CallStatusToText(status)

# This handler is fired when status of Call object has changed
def OnCall(call, status):
    global CallStatus
    CallStatus = status
    print 'Call status: ' + CallStatusText(status)
    print status
    if status == "INPROGRESS":

        # CallStatus = CallIsFinished
        # Sort the dictionary
        for key in sorted(keys.iterkeys()):
            time.sleep(3)
            print "Pressing key " + keys[key]
            call.DTMF = keys[key]


# This handler is fired when Skype attatchment status changes
def OnAttach(status):
    print 'API attachment status: ' + AttachmentStatusText(status)
    if status == Skype4Py.apiAttachAvailable:
        skype.Attach()


# Creating Skype object and assigning event handlers..
skype = Skype4Py.Skype()
skype.OnAttachmentStatus = OnAttach
skype.OnCallStatus = OnCall

# Starting Skype if it's not running already..
if not skype.Client.IsRunning:
    print 'Starting Skype..'
    skype.Client.Start()

# Attatching to Skype..
print 'Connecting to Skype..'
skype.Attach()

# Checking if what we got from command line parameter is present in our contact list
Found = False
Call = skype.PlaceCall(userNumber)


# Loop until CallStatus gets one of "call terminated" values in OnCall handler
while not CallStatus in CallIsFinished:
    pass
