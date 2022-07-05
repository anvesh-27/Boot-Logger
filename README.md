# Boot Logger
A simple tool to log the time of boot and the person who booted your PC.

## Installation
You need to have python3 to run this

### Install Python Requirements

```
pip install -r requirements.txt
```

## Run

### Configure
You need to download the files and save them in a directory called "Boot_Logger".
Navigate to 
```
C:\Users\User\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup 
```
Replace User with your own User's name.

Save the start.bat file in that location.
Edit the start.bat file and replace  ```E:\Boot_Logger```  with the complete path of your directory where you have stored your ```Boot_logger.py```

You might want to check your camera port if you get an error regarding the image capture and replace it in the Boot_logger.py Line 16

### Usage
You are all set to go. Each time your PC boots logs will be stored in the Log file in the directory you saved you python script. The images of the person who booted your machine will be saved in that same directory.