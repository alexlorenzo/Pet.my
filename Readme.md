## Kaggle Competition: Pet.my ##

We divide the Competition in 4 parts:

- **Data Preparation** : This is the part of the competition i.e. downloading data, extracting features and creating features.

- **Data Description** : Analyze graphically and statistically the impact of each features on **Adoption Speed**.

- **Multi Class Models** : Implement XGboost, LightGBM, Decision Tree, Random Forest and stack all the models together to improve the prediction.

- **Image Multi Class** : Implement Convolutional Neural Network to class images (pending)

### Requirements ###

You need Python 3.1 or later to run the file **Pet.my.ipynb**.

The following packages are necessary for this notebook:

- numpy 
- pandas
- zipfile
- PIL (`image extraction`)
- io
- cv2
- json 
- objectpath
- seaborn
- matplotlib
- wordcloud

### Files used  

All training file of the Kaggle Competition are included: 

- Train.csv
- breed_labels.csv
- color_labels.csv
- state_labels.csv
- train_metadata.zip (`for storage reason zip file are not saved in this GitHub``)
- train_images.zip
- train_sentiment.zip


### Conclusion on Data Description Analysis
The category **0** (pet was adopted on the same day as it was listed) concerns only 3% of the Dataset. The prediction will be hard for this category.  
Features that have an impact on *Adoption Speed*:  

- Type: cats are adopted faster than dogs
- Mixed gender are adopted slower certainly due to the obligation to adopt more than one pet. 
- An animal with more fur is adopted faster
- Younger pets are adopted faster
- Small pets are adopted faster 
- Mixed Breed seem to be adopted faster
- Free cats seem to have an impact on the Adoption
- Most Pets are adopted faster in Selangor and slower in Pulan Pinang and Kuala Lumpur. Selangor is the suburb of Kuala Lumpur.
- The bigger rescuer seem to have faster adoption
- Higher Sentiment Score -> fast adoption
- If the Pet Name is missing than the adoption is slower
- Topicality and the image description seem to have an impact 
- SVD and NMF variables are important features for Adoption Speed  
- Open source like the GDP per region have an impact on Adoption Speed

Features with no impact or less impact on *Adoption Speed*:  

- Vaccinated, Dewormed and Sterilized seem to have no impact on Adoption Speed?   
- Colors seem to have no impact  

### Conclusion on Multi Class Models





