# Pi FPV Camera
A simple python script to make a FPV camera with DVR <BR>

## How it works :
* Capure live video from Pi Camera module 
* Send it to av out pin on raspberry pi 
* Will wait for button to be pushed or radio control signal to start recording or capture image
* If button pushed or signal recived will recored video on SD Card

## Components :
* Raspberry Pi zero w
* Pi camera module
* Push button
* Some wires

## Wiring :
* Connect Camera to camera module port
* Connect status led to GPIO 5
* Connect push button to GPIO 7
* connect AV out pin to your transmitter

## To Do :
* Better radio control impelementation
* Create OSD function 
