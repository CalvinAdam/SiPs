# Statistically improbable phrases
My SiP Algorithm  
The Corpus_production file takes all text files in a folder and trains itself on these texts alone. 
The SiPs file takes these corpi as well as a text to generate the phrases for and prints out the SiPs in Form of
Bigrams and Trigrams.  
To use this algorithm simply install python and then the required packages (pickle, textblob, glob) 
with pip install 'package'. You also need to provide a folder with text files for the Corpus_production 
file to train on. As long as both of these files are in the same folder, the pickle files will 
automatically work.  
By training this algorithm on 831 english wikipedia articles it's output for the Bigrams 
and Trigrams for the website https://en.wikipedia.org/wiki/Paul_the_Apostle#Gnosticism, about the apostle 
Paul was as follows:  
![](sips_paul.JPG)  