# Define Empty lists
d = None  
data = None  
description=[]
imageid=[]

# Read Zip File and Export a Dataset with the Score and the ID
with zipfile.ZipFile(r'C:\Users\alorenzodebrionne\Documents\Kaggle\train_metadata.zip', "r") as z:
   for filename in z.namelist():  
      with z.open(filename) as f:  
          data = f.read()
          d = json.loads(data.decode("utf-8"))
          if 'labelAnnotations' in d:
             json_tree = objectpath.Tree(d['labelAnnotations'])
             image_metadata = tuple(json_tree.execute('$..description'))
             image_metadata = pd.DataFrame(list(image_metadata),columns=["label"])
             # Transpose to have 1 line per image
             image_metadata = image_metadata.transpose()
             # Count the number of columns
             col= len(image_metadata.columns)-1
             #Concatenate all columns
             image_metadata['image_metadata']=image_metadata.iloc[:,0:col].apply(lambda x: ','.join(x), axis=1)
             #Keep only all description variables
             image_metadata = image_metadata[['image_metadata']] 
             description.append(image_metadata.iloc[0,0])
         
         
             imageid.append(filename.replace('.json',''))

# Output with sentiment data for each pet
image_metadata = pd.concat([ pd.DataFrame(imageid, columns =['ImageId']) ,pd.DataFrame(description, columns =['label'])],axis =1)

#Per petID you have multiple picture let's transpose to have one line per Pet

# create the PetId variable
image_metadata['PetID'] = image_metadata['ImageId'].str.split('-').str[0]
#Tranpose the table 
image_metadata_raw = image_metadata.groupby('PetID').label.apply(list)
image_metadata_raw=pd.DataFrame(image_metadata_raw.tolist(), index=image_metadata_raw.index)
#Rename the variables
image_metadata_raw.columns = ['image_meta_' + str(col) for col in image_metadata_raw.columns]

image_metadata_raw.to_csv(r"C:\Users\alorenzodebrionne\Documents\BusinessDecision\Projects\Kaggle\image_metadata.csv")
