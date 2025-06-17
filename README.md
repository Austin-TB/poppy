# Poppy
I hate bloating my mid-tier system with the resource heavy NVIDIA app, just for the driver udpates. That's why I created `Poppy` - a Windows application that checks for NVIDIA graphics driver updates. It scrapes the web to fetch the latest driver version from the web and compares it with the current version installed on your system.

## Prerequisites
- Active internet connection
- Nvidia GTX/RTX GPU(s)

## Installation
There is an installable [setup file](https://github.com/Austin-TB/poppy/releases/download/beta/poppy.Setup.1.0.0.exe) which gives you a faster launch, and a [portable version](https://github.com/Austin-TB/poppy/releases/download/beta/Poppy.exe) that doesn't require installation. You can download from the releases tab too.

## Running the Application

To run the Driver Update Checker:

1. Double-click on `Poppy.exe` to launch the application.

## Usage

Once the application is running:

1. Click the "Check Update" button to fetch the current graphics driver version and the latest available version.
2. The application will display the current version installed and the latest version available from NVIDIA. It will also indicate whether an update is available, and redirect you to the download URL (from NVIDIA).

## Improvements I'm working on
Currently working on:
- doing the scraping on cloud
- error handling for devices without NVIDIA-GPU
  
If you have suggestions for improvements or have encountered bugs, please feel free to contact me! 😊
