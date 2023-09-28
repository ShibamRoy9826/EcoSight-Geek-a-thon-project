THE STEPS TO RUN THIS AIR QUALITY INDEX PREDICTION MODEL
------------------------------------------------------------------
In case of any issues you may contact shibamroy9826@gmail.com

1.Make sure to install python in your computer, in cause you don't have it installed, you can install it from www.python.org

2.Please download the model to your computer from here:
https://drive.google.com/file/d/1uk9T_NtEy720BXKwOdFRbVcU8C0JGg9D/view?usp=drive_link

3.Once, you're done please install a few requirements, which you can do by running a few commands in your terminal/command prompt:
Commands to run:
---------------------
pip install joblib
pip install numpy

-------------------

And as soon as it's done, create a new .py file or python file, and add the follwing code:

##############################################################
import numpy
import joblib

#The inputs ( Please change these inputs to get your results)
yr=2023
hr=16
mnth=9
day=1

inpArray=numpy.array([[hr,day,yr,mnth]])
# You may change the model directory if you want
model=joblib.load("airQualityModel.pkl")
print(model.predict(inpArray))

###############################################################

You can change the inputs to get your required results, and that's how simple it is to use our model!
Thanks for reading and your curiousity to check our model!
Hope you like it:)