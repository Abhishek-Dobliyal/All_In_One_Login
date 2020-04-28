# All_In_One_Login

A small GUI to login at various platforms. Written in Python3


# Dependencies

-> selenium ( pip install selenium [ Windows Users ] / pip3 install selenium [ Mac/Linux Users ] )

# Executing the Script

-> Navigate to the cloned repo directory using Terminal/ PowerShell

-> Type in 
   
   python main.py ( Windows Users )
   python3 main.py ( Mac/Linux Users )

# Note : 

1. Need a compatible webdriver for your Browser. Kindly install the webbriver for your browser before executing the script.

2. In the file main.py, make the following changes according to your webdriver

 For Example : If you use Chrome, then change the driver variable of every function according to your Broswer. 
               After changes, it should look like this : driver = webdriver.Chrome()
                 
               For Firefox, driver = webdriver.Firefox()
               For Safari, driver = webdriver.Safari()

3. Keep main.py, icon (folder) in the same directory

4. The Front End of the website(s) may change, so this tool may not work in future.
