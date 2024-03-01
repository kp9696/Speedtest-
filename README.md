# Speedtest-using Python 
Before Execute this follow these step
Create the Python Script:
Save your Python script as, let's say, speedtest_app.py.

Create a Batch File:
Open a text editor and create a new file with the following content. Save it with a .bat extension, for example, run_speedtest_app.bat.
@echo off
cd /d %~dp0
python speedtest_app.py
Make sure to replace python with the actual command you use to run Python. If your Python command is python3, modify the script accordingly.

Place Both Files in the Same Directory:
Move both the speedtest_app.py and run_speedtest_app.bat files to the same directory.

Run the Batch File:
Double-click on the run_speedtest_app.bat file. This will execute the batch file, which, in turn, runs your Python script.

Make sure you have Python installed on your Windows machine, and the Python executable is in your system's PATH.

This setup allows you to run your Python script with a single click by executing the batch file.
