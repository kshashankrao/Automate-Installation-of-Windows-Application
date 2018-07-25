# Pip install pywinauto
from pywinauto.application import Application as App
import pywinauto
import time

# Add the absolute file path
app = App().start("D:\Anaconda3-4.2.0-Windows-x86_64.exe")
time.sleep(1)

# Add the correct window name
ctrl = app["Anaconda3 4.2.0 (64-bit) Setup"]

'''
Working:
It tries to find the clicable button (simulation of mouse)
But the mouse movement cannot be seen
'''
# Actions to be performed based on the observations

####################################################
ctrl.NextButton.click()
ctrl.IAgree.click()
ctrl.NextButton.click()
ctrl.NextButton.click()
time.sleep(1)
ctrl.Install.click()
ctrl.Finish.wait('enabled', timeout=30)
ctrl.Finish.click()
ctrl.wait_not('visible')
######################################################
