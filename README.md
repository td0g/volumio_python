# volumio_python
Controlling Volumio using Python

## Installation

Run sudo apt-get install python3-pip

Run pip3 install rpi.gpio

Copy volumioControl.py into your /home/volumio directory

Run sudo nano /etc/rc.local

Add this line:  python3 /home/volumio/volumioControl.py &
