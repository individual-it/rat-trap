# The totally overengineered rat-trap

## Why?
BECAUSE, why not?

## Hardware
I tried various things before I came up with this particular design.
A pipe (closed at one end) is the basis of the trap. On the open end the pipe has a slot where the flap fits in.
Now I needed something that hold the flap till the rat is in the trap, closes it and locks it in the right moment.
For that I used an old floppy drive and attached a pin attached to the read/write head. The upper part of the disc-drive cover become the flap.
When the trap is armed, a rubber band and the pin attached to the read/write head hold the hatch in position. When released the read/write head pulls back the pin, the rubber band forces the hatch into the slot of the pipe and finally the head pushes the pin back forward into a hole in the hatch to lock it.

As trigger, I used a mouse (a computer mouse). The mouse is placed inside the trap with some food behind it.
The rat has to walk over the mouse to get the food, whenever any button of the mouse is clicked or its moved the trap will lock.

If that is all a bit hard to understand have a look at the pictures, and the video:

<img src="https://github.com/individual-it/rat-trap/raw/main/media/top.jpg" width="80%"/>
<img src="https://github.com/individual-it/rat-trap/raw/main/media/front.jpg" width="80%"/>
<img src="https://github.com/individual-it/rat-trap/raw/main/media/side.jpg" width="80%"/>

[Video of setup & arming](https://github.com/individual-it/rat-trap/raw/main/media/arming-and-releasing.mp4)

## Electronics
The whole thing is powered by an RPi (a pretty old one actually). The RPi has a simple button attached to arm the trap, and some GPIO ports connected to the floppy drive to move the read/write head of it.

- connect 5V & GND of the RPI GPIO to the 5V input of the drive. Don't worry the stepper does not pull too much current, so the RPI won't mind
- connect another GND of the RPI to any of odd (lower row) pins of the FDD, they are all GND
- connect GPIO17 (pin 11) to pin 20 of the FDD (Head Step)
- connect GPIO18 (pin 12) to pin 18 of the FDD (Direction Select)
- use a jumper to shortcut pins 11 & 12 of the FDD (Drive Select 1)

RPI GPIO layout: http://elinux.org/Rpi_Low-level_peripherals#Interfacing_with_GPIO_pins

FDD PIN layout: http://www.interfacebus.com/PC_Floppy_Drive_PinOut.html

## Software
A python script reads the inputs (button & mouse), and controls the read/write head.

The function of the software is pretty simple and should be improved:
1. find a mouse in the device list
1. waiting for the button to be pushed
1. pulls back the head and waits 10 sec. to allow the hunter to place the flap
1. pushed the head into the right position to hold the flap
1. waits for a mouse-event
1. pulls the head completely back
1. pushed the head forward as far as it can
1. as a small bonus it sends a notify.run notification to any device (e.g. mobile)

## Known issues
1. my wireless mouse goes into a sleep mode and then needs two clicks to release, one to wake up, and the next one only sends the event
1. sometimes the event-queue seems not to be cleaned, so the trap is fired as soon as its armed 

## Does it work?
I caught 6 rats with it
![rat trap in action](https://github.com/individual-it/rat-trap/raw/main/media/in-action.gif)
[full res video](https://github.com/individual-it/rat-trap/raw/main/media/in-action.mkv)

## Is it practical?
NO, but who cares, it was fun to build

## Mode ideas for overengineering
- an AI that detacts the rats
