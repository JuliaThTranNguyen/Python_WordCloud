#This is an example of "Python - WordCloud"
##Author: T.H.JuliaRosy - TranHien
##Main language: Python
###_______________________________________________________

#IMPORTING LIBRARIES
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS
from PIL import Image


#IMPORTING DATASET FROM ANY ".TXT" FILE
###Allows readable access to ".txt" file
read_text = open ('pythontext.txt', 'r').read()

#SHAPE OF ANY OBJECTS TO GENERATE WORDCLOUD (OPTIONAL)
###Import image to np.array
python_shape = np.array(Image.open('python.png'))

#GENERATE WORDCLOUD
###STOPWORDS CAN BE EDITED : stopwords=set(list(STOPWORDS)+["the_word_which_needs_to_be _deleteled"])
GEN_WORD_CLOUD = WordCloud (
    stopwords=STOPWORDS,
    mask=python_shape,
    background_color= "white",
    contour_color= "black",
    contour_width=3,
    min_font_size=3,
    #colormap="Set2",
    #collocations=False,
    max_words=400 ).generate(read_text)

plt.imshow(GEN_WORD_CLOUD)
plt.axis("off")
plt.show()





