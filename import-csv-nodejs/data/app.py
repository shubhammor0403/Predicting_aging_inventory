from flask import Flask,render_template,url_for,request
from flask_material import Material

import tensorflow as tf
global graph,model
graph = tf.get_default_graph()

# EDA PKg
import pandas as pd 
import numpy as np 

import random
import matplotlib.pyplot as plt
# ML Pkg
from sklearn.externals import joblib
app = Flask(__name__)
Material(app)


#-------------------------------------------------------------------------------------------------------

import numpy as np
from sklearn.externals import joblib
from keras.models import model_from_json

labeleforid_filename = "mainsave/labelid.save"
labeleforcategory_filename = "mainsave/labelcategory.save"
labeleforcompany_filename = "mainsave/labelcompany.save"
labeleforaud_filename = "mainsave/labelaud.save"
onehot_filename = "mainsave/onehot.save"


#loading all the label encoders and onehot encoders
labelencoderforid = joblib.load(labeleforid_filename) 
labelencoderforcategory = joblib.load(labeleforcategory_filename) 
labelencoderforcompany = joblib.load(labeleforcompany_filename) 
labelencoderfortargaud = joblib.load(labeleforaud_filename)
onehotencoder = joblib.load(onehot_filename) 
scaler=joblib.load("mainsave/scaler.save")

#loading the main model now
json_file = open('mainsave/model.json', 'r')
loaded_model_json = json_file.read()
json_file.close()
classifier = model_from_json(loaded_model_json)
# load weights into new model
classifier.load_weights("mainsave/model.h5")
print("Loaded model from disk")
 
# evaluate loaded model on test data
classifier.compile(loss='binary_crossentropy', optimizer='adamax', metrics=['accuracy'])

print('done')

diction = {0:'Move to new inventory',1:'Global dell outlet sale',2:'Use strategies for social media'}
def dostuff(test):
    import numpy as np
    a=np.array(test)
    a[:, 0] = labelencoderforid.transform(a[:,0])
    a[:, 1] = labelencoderforcategory.transform(a[:,1])
    a[:, 2] = labelencoderforcompany.transform(a[:, 2])
    a[:, 3] = labelencoderfortargaud.transform(a[:, 3])
    newaa = onehotencoder.transform(a).toarray()
    newaa=scaler.transform(newaa)
    print(newaa)
    with graph.as_default():
        ans = classifier.predict_classes(newaa)
        ansprob = classifier.predict_proba(newaa)
        ansaa = max(ansprob[0])      
        print("done")
		
    

    
    
    return ans,"Predicted Best strategy to move forward would be: "+diction[ans[0]]+". This would give the item a "+str(int(ansaa*100))+"% chance of being sold"

#----------------------------------------------------------------------------------------------------------
import numpy as np
from sklearn.externals import joblib
from keras.models import model_from_json


labeleforcategory3pl_filename = "new3plsave/labelcategory.save"
labeleforcompany3pl_filename = "new3plsave/labelcompany.save"
labeleforaud3pl_filename = "new3plsave/labelaud.save"
onehot3pl_filename = "new3plsave/onehot.save"

#loading all the label encoders and onehot encoders
 
labelencoderforcategory3pl = joblib.load(labeleforcategory3pl_filename) 
labelencoderforcompany3pl = joblib.load(labeleforcompany3pl_filename) 
labelencoderfortargaud3pl = joblib.load(labeleforaud3pl_filename)
onehotencoder3pl = joblib.load(onehot3pl_filename) 
scalerfor3pl=joblib.load("new3plsave/scaler.save")

#loading the main model now
json_file = open('new3plsave/model.json', 'r')
loaded_model_json = json_file.read()
json_file.close()
classifier3pl = model_from_json(loaded_model_json)
# load weights into new model
classifier3pl.load_weights("new3plsave/model.h5")
print("Loaded model from disk")
 
# evaluate loaded model on test data
classifier3pl.compile(loss='binary_crossentropy', optimizer='adamax', metrics=['accuracy'])

print('done')


dictionary = {0:'id_101: Bangalore',1:'id_102: Delhi',2:'id_103: Chicago',3:'id_104: Manchester'}
def dostufffor3pl(test):
    import numpy as np
    a=np.array(test)
    a[:, 0] = labelencoderforcategory3pl.transform(a[:,0])
    a[:, 1] = labelencoderforcompany3pl.transform(a[:, 1])
    a[:, 2] = labelencoderfortargaud3pl.transform(a[:, 2])
    newaa = onehotencoder3pl.transform(a).toarray()
    newaa=scalerfor3pl.transform(newaa)
    with graph.as_default():
        ans = classifier3pl.predict_classes(newaa)
        ansaa = classifier3pl.predict_proba(newaa)
        print(ansaa)
    return max(ansaa[0]),dictionary[ans[0]],("Predicted Best inventory for selling this item is: "+dictionary[ans[0]]+".")

#-------------------------------------------------------------------------------------------------------

import numpy as np
from sklearn.externals import joblib

labelsocialeforid_filename = "savedfordell/labelid.save"
labelsocialeforcategory_filename = "savedfordell/labelcategory.save"
labelsocialeforcompany_filename = "savedfordell/labelcompany.save"
labelsocialeforaud_filename = "savedfordell/labelaud.save"
onehotsocial_filename = "savedfordell/onehot.save"


#loading all the label encoders and onehot encoders
labelencoderforidsocial = joblib.load(labelsocialeforid_filename) 
labelencoderforcategorysocial = joblib.load(labelsocialeforcategory_filename) 
labelencoderforcompanysocial = joblib.load(labelsocialeforcompany_filename) 
labelencoderforaudsocial = joblib.load(labelsocialeforaud_filename)
onehotencodersocial = joblib.load(onehotsocial_filename) 
scalersocial=joblib.load("savedfordell/scaler.save")

 
#loading the main model now
modelsocial = joblib.load('savedfordell/rfmodelmain.save')

print('done')

content_array=[]

#this file contains all the possible strategy cases. we take them in an array and concat with our input
with open('cases.txt') as f:
    for line in f:
        content_array.append([c for c in line.rstrip()])
content_array = np.array(content_array)
content_array=content_array.astype(np.int)
content_array=content_array.tolist()

#______________________________________________________________________________________________________



#_______________________________________________________________________________________________________

# print(content_array)

outputdp=[]
#this array contains all the possible combinations in text form. i.e 100100 represented for its strategy text
for i in content_array:
    temparray=[]
    if(i[0]==1):
        temparray.append('Promotions')
    if(i[1]==1):
        temparray.append('Email')
    if(i[2]==1):
        temparray.append('Proper representation')
    if(i[3]==1):
        temparray.append('Discounts')
    if(i[4]==1):
        temparray.append('Bonus items')
    if(i[5]==1):
        temparray.append('Improved location')
    outputdp.append(temparray)

def makecases(array):
    newarr=[]
    for j in content_array:
        newarr.append(array+j)
    newarr=np.array(newarr)
	
	
    
    #using label encoder
    newarr[:,0] = labelencoderforidsocial.transform(newarr[:,0])
    newarr[:,1] = labelencoderforcategorysocial.transform(newarr[:,1])
    newarr[:,2] = labelencoderforcompanysocial.transform(newarr[:,2])
    newarr[:,3] = labelencoderforaudsocial.transform(newarr[:,3])

    newarr=newarr.astype(np.float)
    
    #now transforming to seperate columns using onehot encoder
    encodedarr = onehotencodersocial.transform(newarr).toarray()
    encodedarr=scalersocial.transform(encodedarr)
        
    return encodedarr


def makeprediction(t):
    res=modelsocial.predict_proba(t)
    resa=[]
#     print(res)
    for i in range(len(res)):
        resa.append([i,res[i,1]])
    #sorting the array based on the probability predicted    
    resa = sorted(resa, key=lambda a_entry: a_entry[1], reverse=True)
    return resa       

def doeverythingsocial(a):
	t=makecases(a)
	z=makeprediction(t)
	z=np.array(z)
	l=''
	m=''
	n=''
	
	s1=', '.join(str(x) for x in outputdp[int(z[0,0])])
	l=l+str(0+1)+") "+s1+" will result in "+str(int(z[0,1]*100))+"% chance of being sold.\n"
	s2=', '.join(str(x) for x in outputdp[int(z[1,0])])
	m=m+str(1+1)+") "+s2+" will result in "+str(int(z[1,1]*100))+"% chance of being sold.\n"
	s3=', '.join(str(x) for x in outputdp[int(z[2,0])])
	n=n+str(2+1)+") "+s3+" will result in "+str(int(z[2,1]*100))+"% chance of being sold.\n"
	
	return l,m,n	
	






#-------------------------------------------------------------------------------------------------------


@app.route('/')
def index():
    return render_template("index.html")

@app.route('/preview')
def preview():
    df = pd.read_csv("maindb.csv")
    
    return render_template("preview.html",df_view = df[['item_id', 'item_category', 'company', 'no_items_recieved', 'no_items_remaining', 'date_recieved', 'selling_price']])



move=0

@app.route('/',methods=["POST"])
def analyze():
	if request.method == 'POST':

		if move == 1:
			print("test")
		item_id = request.form['item_id']
		
		df = pd.read_csv("../public/files/maindb.csv")
		i= df.loc[df['item_id'] == (item_id)]
		i=i.loc[i['currently_inventory']==1.0]
		print(i)
		choice = request.form['choice']
		print(choice)
		i=(np.array(i))
		inventory_id = i[0][0]
		inventory_location = i[0][1]
		item_id = i[0][2]
		category = i[0][3]
		company = i[0][4]
		targaud = i[0][5]
		noofitems = i[0][7]
		noofdays = i[0][13]
		price = i[0][9]
		year = i[0][10]
		demandfac =i[0][11]
		profit = i[0][12]
		st=''
		textsuggest2=''
		textsuggest3=''
		result_predictionwhich=''
		# Clean the data by convert from unicode to float 
		# if(choice=="Dell Global Outlet Sale"):
		# 	st="This item has the highest chance of being sold when put up for sale in Dell's Global Outlet."
		# 	result_predictionwhich=2
		import time
		
		print("timertime")

		time.sleep(1.8)
		
		if(choice=="Suggest Best strategy to move forward"):
			sample_data = [[inventory_id,category,company,targaud,noofdays,noofitems,price,year,demandfac,profit]]
			print(sample_data)
			
			# Reloading the Model
			what,st = dostuff(sample_data)
			if(what[0]==0):
				result_predictionwhich="Move to another 3PL"
				sample_data = [[category,company,targaud,price,year,demandfac,profit]]
				pro,reti,textsuggest2 = dostufffor3pl(sample_data)
				print(pro)
				textsuggest2 = "Current inventory of the item: "+inventory_id
				if(inventory_id==reti[0:6]):
					textsuggest3="Item is already in the best inventory. Try adopting some other strategy"
				else:
					textsuggest3="Item is not in the best selling inventory ("+inventory_id+"). If convinient, move the item to "+reti+" as soon as possible as it has a "+str(int(pro*100))+"% chance of being sold there."
			if(what[0]==1):
				result_predictionwhich="Put the item on GDO"
				textsuggest2 = "This item has the highest chance of being sold when put up for sale in Dell's Global Outlet."

			if(what[0]==2):
				result_predictionwhich="Use Social Media Inputs"
				sample_data = [inventory_id,category,company,targaud,noofitems,price,year,demandfac,profit]
				s1,s2,s3 = doeverythingsocial(sample_data)
				
				textsuggest2=s1
				textsuggest3 = s2
			
		if(choice=="Move to new best 3pl"):
			sample_data = [[category,company,targaud,price,year,demandfac,profit]]
			st = "Current inventory of the item: "+inventory_id
			pro,retid,textsuggest2 = dostufffor3pl(sample_data)
			result_predictionwhich="Move to another 3PL"
			print(retid[0:6])
			if(inventory_id==retid[0:6]):
				textsuggest3="Item is already in the best inventory. Try adopting some other strategy"
			else:
				textsuggest3="Item is not in the best selling inventory ("+inventory_id+"). If convinient, move the item to "+retid+" as soon as possible as it has a "+str(int(pro*100))+"% chance of being sold there."
		# if(choice=="Dell Global Outlet Sale"):

		
		if(choice =="Social Media inputs"):
			sample_data = [inventory_id,category,company,targaud,noofitems,price,year,demandfac,profit]
			 
			s1,s2,s3 = doeverythingsocial(sample_data)
			result_predictionwhich="Use social media inputs"
			st=s1
			textsuggest2=s2
			textsuggest3=s3





	return render_template('index.html', 
		inventory_id=inventory_id,
		inventory_location = inventory_location,
		item_id = item_id,
		category=category,
		company=company,
		targaud=targaud,
		noofitems=noofitems,
		price=price,
		year=year,
		demandfac=demandfac,
		profit=profit,
		noofdays=noofdays,
		result_prediction1=st,
		result_predictionwhich=result_predictionwhich,
		result_prediction2=textsuggest2,
		result_prediction3=textsuggest3
		)



if __name__ == '__main__':
	app.run(debug=True)
	app.jinja_env.auto_reload = True
	app.config['TEMPLATES_AUTO_RELOAD'] = True