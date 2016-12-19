# automatic-phonecalls

Built with skype and skype4py. Let's the user make automated calls and interact with the keypad using skype.

I was calling an office the other day, and they had not implemented a telephone-queue system. So it was really frustrating to have to call again and again. On every call I had to press certain keys to navigate to the specific office I had to talk to. Using skype you can call straight from the linux-terminal, but it does not allow you to automatically "press buttons". So it is still a hassle. That's why I wrote this little tool.

I recommend using it together with a cronjob.

## Installing
It was tested on Ubuntu 16.04

To get it working I installed skype4py and python-gobject:

```
pip install skype4py
sudo apt-get install python-gobject
```

## Usage

First you have to call the number to get the path you need to take to reach your destination.
So find out what numbers or symbols you need to press in order to reach your destination.

```
--number/user 004607077711188"
--number/user bob.dylan"
--key1 to key10"

Exit using Ctrl-C or hang up in the skype-interface

Example:
python call.py --number/user 004607077711188 --key1 2 --key2 1 --key3 7
python call.py --number/user happycow --key1 2 --key2 1 --key3 7
```
