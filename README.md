# Facebook Tester
A Selenium-based app, that configures and runs the script for:
* Logging into Facebook account
* Getting friends list
* Retrieving their names and profile links

Python version: 3.7.2

# Requirements
Additional software, required for this program includes:
* Google Chrome
* Chrome web driver binary: http://chromedriver.chromium.org/downloads

Following python modules have to be included:
* selenium 3.141.0

# Preparations
First of all you need to clone this program to your machine. Make sure you have .git installed on your machine. Navigate to a desired location and then execute following command:

```bash
git clone https://github.com/DmitriySolontsevoy/FacebookBrowser.git
```

Next, you need to setup needed python environment. You can install all libs manually, or alternatively you can install them by running this command:

```bash
pip install -r ./requirements.txt 
```

# Configure the project
In the Configs\Configurable\ there's a file, called config.json. This file configurates parameters for paths to files and also sets targets and levels for logging.

Currently, logging can target a text file or console:
* For console output:
  * Enable with "CONSOLE_LOGGING" set to 1, disable with 0
  * Set console logging level with "CONSOLE_LOG_LEVEL":
    * 1 - ERROR
    * 2 - WARN
    * 3 - INFO
    * 4 - DEBUG   
* For text file output:
  * Enable with "TEXT_LOGGING" set to 1, disable with 0
  * Set console logging level with "TXT_LOG_LEVEL":
    * 1 - ERROR
    * 2 - WARN
    * 3 - INFO
    * 4 - DEBUG  

# Launch
To start an application, run a file, called Launcher.py in the root of the project:

```bash
python Launcher.py
```
