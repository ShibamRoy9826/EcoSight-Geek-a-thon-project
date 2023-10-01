THE STEPS TO RUN THIS SATELLITE IMAGE CLASSIFICATION MODEL
------------------------------------------------------------------
1.Make sure to install python in your computer, in cause you don't have it installed, you can install it from Python's official website

2.Please download the model to your computer from here: https://drive.google.com/file/d/1wGak27pnl5WaG2U6FSi16g6oJLu9Cg4d/view?usp=drive_link

3.Once, you're done please install a few requirements, which you can do by running a few commands in your terminal/command prompt: Commands to run:

-------------------------

pip install tensorflow
pip install numpy

--------------------------

And as soon as it's done, create a new .py file or python file, and add the follwing code:

################################################################################################
import numpy
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image

# You may change this file path if you have a different one
model=load_model("SuperImpModel.h5")

# Please make sure to change this image path to your input image
img = image.load_img("ChangeThisToYourImgPath", target_size=(224,224))
x = image.img_to_array(img)
x = numpy.expand_dims(x, axis=0)
x = x / 255.0

preds = model.predict(x)
print(preds)
# The predictions are in this order:
# agriculture ,mine,empty,blooming ,blow,clear,cloudy,convolutionary Mine,cultivation,deforestation,haze,partlyCloudy,primary,road,logging,pollution,water
# For example the first element in this list is the probability of agriculture

##################################################################################################
You can change the inputs to get your required results, and that's how simple it is to use our model!
Thanks for reading and your curiousity to check our model!
Hope you like it:)