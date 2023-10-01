# EcoSight-Geek-a-thon-project
<details>
    <summary>Table of Contents</summary>
    <ol>
        <li>
            <a href="#Overview">Overview</a>
        </li>
        <li>
            <a href="#meet_the_team">Meet The Team</a>
        </li>
        <li>
            <a href="#EchoLife-analysis">Ecotech Environment Sustainability Analysis</a>
        </li>
        <ul>
            <li><a href="#project-overview">Project Overview</a></li>
            <li><a href="#team-members">Team Members</a></li>
            <li><a href="#instructions">Instructions</a></li>
            <li><a href="#QNA">QNA</a></li>
            <li><a href="#key-findings">Key Findings</a></li>
            <li><a href="#conclusion">Conclusion</a></li>
            <li><a href="#data-source">Data Source</a></li>
            <li><a href="#acknowledgments">Acknowledgement</a></li>
        </ul>
    </ol>
</details >

<h2 id="Overview">
 <img src="https://media2.giphy.com/media/QssGEmpkyEOhBCb7e1/giphy.gif?cid=ecf05e47a0n3gi1bfqntqmob8g9aid1oyj2wr3ds3mg700bl&rid=giphy.gif" width="25" class="overviews"><b> Overview</b>
</h2>
This is a repository of us 3 team members on this great hackathon organised by GeeksForGeeks.This data science project has been an exciting journey that blends the power of data science with web development to create an innovative application that combines analytical insights with a user-friendly online interface. We are enthusiastic about showcasing our skills in our domains.We worked on data related to various fields related to environmental concerns such as Carbon footprint analysis, Satellite Image Classification and many more.
Video presentation available - <a href="https://youtu.be/Wlp6DpsPWmw?feature=shared">here</a>
<img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif"><br><br>
<h2 id="meet_the_team">
<img src="https://media.giphy.com/media/W5eoZHPpUx9sapR0eu/giphy.gif" width="30px" alt="Git"/>&nbsp;<b>Meet The Team</b>
 </h2>

<ul>
    <li>
        <strong>Data Scientist /Backend :</strong> Shibam Roy - A passionate and skilled Data Analyst with a profound love for
        coding. His extensive knowledge of various programming languages and frameworks enables him to undertake complex
        data analysis projects. From childhood, Shibam has been dedicated to coding, resulting in an impressive
        portfolio of remarkable projects. He has knowledge in C++ , Python, Data Science, and DSA. His analytical mindset, creativity, and effective communication make him a
        valuable asset to any data-driven team. 
    </li>
    <br>
    <li>
        <strong>Front-end developer/ UI designer:</strong> Ankush roy - An integral member of the our team, known for his exceptional front-end development skills, mathematical acumen, and mastery of C++. His artistic eye elevates user experiences, while his passion for mathematics enriches data insights.
    </li>
    <li>
        <strong>Data Scientist :</strong> Swadhin Maharana  - A dynamic and accomplished individual who stands at the forefront of the exciting intersection of Data Science and Python programming. With an insatiable curiosity and a passion for unraveling complex patterns in data, Swadhin has established himself as a distinguished expert in his field.
    </li>
   
</ul>
<img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif"><br>

<h1 id="EchoLife-analysis">
    <img src="https://media.giphy.com/media/iY8CRBdQXODJSCERIr/giphy.gif" width="35"><b>EcoSight Environment Sustainability Analysis </b>
</h1>

<h2 id="project-overview">
    <b>Project Overview</b>
</h2>

Introducing the EcoSight  Analytics by our team for the GeeksforGeeks EcoTech Hackathon. Our project combines a carbon footprint calculator, emission reduction tips, satellite image classification, air quality index data analysis and empowering users to make informed decisions for a sustainable future. With interactive visualizations and a technology stack including Python, Django, and HTML,CSS,Javascript our project promotes greener lifestyles and fosters global environmental awareness.

<h2 id="project-overview">
    <b>Team Members</b>
</h2>

- Shibam Roy: Data Scientist / Back-end developer
- Ankush Roy: Front-end Developer/ UI Designer
- Swadhin Maharana: Data Scientist

<h2 id="instructions">
<b>Instructions for usage </b>
</h2>

### Our overall project together:
To check our overall project altogether, you can go to our project website <a href="https://ecosight.pythonanywhere.com/">here</a>
You can explore it and start conserving nature from today onwards:)

### Air Quality Index Model:

1.Make sure to install python in your computer, in cause you don't have it installed, you can install it from <a href="www.python.org">Python's official website</a>

2.Please download the model to your computer from here:
<a href="https://drive.google.com/file/d/1uk9T_NtEy720BXKwOdFRbVcU8C0JGg9D/view?usp=drive_link">here</a>

3.Once, you're done please install a few requirements, which you can do by running a few commands in your terminal/command prompt:
Commands to run:
```bash

pip install joblib
pip install numpy

```

And as soon as it's done, create a new .py file or python file, and add the follwing code:

```python
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

```

You can change the inputs to get your required results, and that's how simple it is to use our model!

### Satellite Image Classification Model

1.Make sure to install python in your computer, in cause you don't have it installed, you can install it from <a href="www.python.org">Python's official website</a>

2.Please download the model to your computer from here:
<a href="https://drive.google.com/file/d/1wGak27pnl5WaG2U6FSi16g6oJLu9Cg4d/view?usp=drive_link">here</a>

3.Once, you're done please install a few requirements, which you can do by running a few commands in your terminal/command prompt:
Commands to run:
```bash

pip install tensorflow
pip install numpy

```

And as soon as it's done, create a new .py file or python file, and add the follwing code:

```python
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
```

You can change the inputs to get your required results, and that's how simple it is to use our model!

### Carbon Footprint Calculator
Carbon Footprint calculator isn't an actual model, its based on data analysis, its basically automated data analysis.
If you still want to check it out, you may do so by looking it the backend files, especially "views.py"

<img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif">
<h2 id="QNA">
<b>QNA</b>
</h2>

### 1.What our project basically targets to do?
=> Our project promotes sustainable environmental development and also features multiple applications such as a carbon footprint calculator , so that people are aware of their own carbon emission contributions, Not only does it calculate the carbon emissions it also suggests recommendations on how we can improve ourselves to have a better future!

Our project also has a Satellite image classification model which basically classifies the situation of any satellite image given to it, this will classify the probability of that particular area of having pollution, water, mine etc.
This can be used to identify your locality in a better way.

That's not all, we also analysed the air pollution index data from 2017 to 2022 and drew out multiple helpful insights, you can check the overall analysis too! This also has a predictive model to find out upcoming air pollution indices especially in India, the model isn't available to run in the website but you can run it locally in your computer(instructions are given near the jupyter notebook , or you can check the other questions too)

### 2.How can you access our project?
=> You are already in the correct place, you can view this overall repository to find out our work.

### 3.How can you run the Air Pollution Index model?
=> Due to github restrictions we can't upload this file here as its quite large, but you can check the python notebook used to make it in the AirQuality folder, besides that you can download the model from <a href="https://drive.google.com/file/d/1uk9T_NtEy720BXKwOdFRbVcU8C0JGg9D/view?usp=drive_link">here</a>.
Just extract the zip file and follow the instructions in the readme.txt

### 4.Which libraries and language are we using?
=> We are using python as a language for the overall logic and we are also using JavaScript in web development.For non-programming languages we are using html and css for web development.When it comes to libraries we are using matplotlib and seaborn because of their wonderful capabilities of creating visualizations, we are also using pandas and numpy for data management ,tensorflow keras for deep learning and sklearn for machine learning.

### 5.How is the backend working?
=> For the backend and server hosting we are using free tier of pythonanywhere. As a framework we are working with Django.

### 6.What is our project for?
=> Our project is solely made for sustainable environment development, we are creating it on the occasion of a wonderful hackathon organised by Geeksforgeeks which is called EchoTech, but besides for the hackathon we are also going to maintain this site after, and further developmental plans would be there for this website.

### 7.What are the future plans for this website?
=> We are going to maintain our website even after this hackathon ends, we already have plans like tourism recommendation system, social media updates on ecology, and many more! the updates would be coming soon be ready!

### 8.How did we come up with this idea?
=> We were really concerned about our environment, moreoever due to the beautful theme of the hackathon organised by GeeksForGeeks, we thought and found out the actual reasons for environmental degradation.Some Key factors are deforestation, and carbon emmissions. Our project exactly aims to spread awareness on that issue.

<img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif">
<h2 id="key-findings">
<b>Key Findings </b>
</h2>

### From Air Quality Index
<ul>
<li>In the year 2020, there was a sudden decrease in the air pollution, and resulted in a good air quality index, Most probably this was due to Corona Virus.</li>
<li>Each year, especially in the month of August, we have good air quality index, this should usually happen due to the phenomenon called "Wet Deposition"</li>
<li>Each day, during the time of 5AM , 12AM and 4-5PM, the air quality index shows a great change.This can be because these are considered as the business hours.</li>
<li>Pollution was at its peak in the year of 2018, it gradually decreased to 2020, and it slightly started to raise by 2021, by which we can predict almost about by this year or maybe the next, it would cross the air pollution of 2017!</li>
</ul>

### From Satellite image classification 
Not much insights were found in this, we trained a deep learning model instead.

### From Carbon Footprint calculation
<ul>
<li>Most of the countries use Oil for their electricity production, which usually exerts about 730g of Carbon per 1KWh, which is a bad news!</li>
<li>On an average electricity costs about $0.16 globally.</li>
<li>Globally, on an average each person emmits about 4.61 tonnes of carbon each year, while the target emmissions are less than or equal to 2.5 tonnes!</li>
<li>Carbon Dioxide mostly from gas is around 1.3 tonnes per year per person!</li>
</ul>

<h2 id="conclusion">
<b>Conclusion</b>
</h2>
In conclusion, the sustainable development of our ecosystem is not just a vision; it's a tangible reality that we are actively shaping through innovation and collective efforts. Our website, equipped with features like Satellite Image Classification, Carbon Footprint Calculator, and Air Quality Index Analysis, is a testament to our commitment to this cause. As we navigate the intricate web of data and technology, we discover the means to harmonize our existence with nature.

While our world is unmistakably progressing towards sustainability, the urgency of our situation cannot be overstated. Climate change and ecological degradation continue to challenge our planet. We must act swiftly, collectively, and decisively to preserve the delicate balance of our environment. Our mission is to not only provide tools for understanding and mitigating environmental impact but also to inspire action.

By embracing sustainable choices and advocating for change, we can accelerate this global transformation. Together, we have the power to safeguard our planet for generations to come. Let's work tirelessly, innovate relentlessly, and inspire one another to move swiftly towards a more sustainable future. Our planet's well-being depends on it.

<img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif">
<h2 id="data-source">
<b>Data Source</b>
</h2>
We are thankful to all the data sources through which we have accessed the data, here are the sources:
<ul>
    <li><a href="https://dewesoft.com/blog/countries-electricity-source">Major source of electricity in each country</a></li>
    <li><a href="https://www.statista.com/statistics/263492/electricity-prices-in-selected-countries/">Electricity prices of each country</a></li>
    <li><a href="https://www.ourworldindata.org/"> CO<sub>2</sub> emmissions data</a></li>
    <li><a href="https://www.kaggle.com/datasets/prosperchuks/amazonsatelliteimages">Amazon Satellite Images Data</a></li>
    <li><a href="https://www.kaggle.com/datasets/fedesoriano/air-quality-data-in-india">Air Quality Index data</a></li>
</ul>

<h2 id="acknowledgements">
<b>Acknowledgements</b>
</h2>

We would like to express our sincere gratitude to GeeksforGeeks for organizing the hackathon that inspired this website. The hackathon was a well-organized and challenging event that provided us with the opportunity to learn new skills, collaborate with talented individuals, and develop this website.
We would also like to thank the following people for their support and guidance throughout the development of this website:
Without your help and support, this website would not have been possible. Thank you!

We would like to give special thanks to GeeksforGeeks for organizing the hackathon that inspired our website. GeeksforGeeks is a leading online platform for learning computer science and programming. It offers a wide range of resources, including tutorials, articles, practice problems, and more. We are grateful for the opportunity to have participated in the hackathon and to have learned so much from the experience.
