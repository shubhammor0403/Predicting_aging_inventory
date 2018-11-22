from flask import Flask,render_template,url_for,request
from flask_material import Material

# EDA PKg
import pandas as pd 
import numpy as np 

# ML Pkg
from sklearn.externals import joblib


app = Flask(__name__)
Material(app)
#-------------------------------------------------------------------------------------------------------

import numpy as np
from sklearn.externals import joblib

labeleforid_filename = "savedfordell/labelid.save"
labeleforcategory_filename = "savedfordell/labelcategory.save"
labeleforcompany_filename = "savedfordell/labelcompany.save"
labeleforaud_filename = "savedfordell/labelaud.save"
onehot_filename = "savedfordell/onehot.save"

#loading all the label encoders and onehot encoders
labelencoderforid = joblib.load(labeleforid_filename) 
labelencoderforcategory = joblib.load(labeleforcategory_filename) 
labelencoderforcompany = joblib.load(labeleforcompany_filename) 
labelencoderforaud = joblib.load(labeleforaud_filename)
onehotencoder = joblib.load(onehot_filename) 

#loading the main model now
model = joblib.load('savedfordell/clf73.save')

print('done')


content_array=[]

#this file contains all the possible strategy cases. we take them in an array and concat with our input
with open('cases.txt') as f:
    for line in f:
        content_array.append([c for c in line.rstrip()])
content_array = np.array(content_array)
content_array=content_array.astype(np.int)
content_array=content_array.tolist()
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
    newarr[:,0] = labelencoderforid.transform(newarr[:,0])
    newarr[:,1] = labelencoderforcategory.transform(newarr[:,1])
    newarr[:,2] = labelencoderforcompany.transform(newarr[:,2])
    newarr[:,3] = labelencoderforaud.transform(newarr[:,3])

    newarr=newarr.astype(np.float)
    
    #now transforming to seperate columns using onehot encoder
    encodedarr = onehotencoder.transform(newarr).toarray()
        
    return encodedarr


def makeprediction(t):
    res=model.predict_proba(t)
    resa=[]
#     print(res)
    for i in range(len(res)):
        resa.append([i,res[i,1]])
    #sorting the array based on the probability predicted    
    resa = sorted(resa, key=lambda a_entry: a_entry[1], reverse=True)
    return resa       

def doeverything(a):
	t=makecases(a)
	z=makeprediction(t)
	z=np.array(z)
	a=''
	b=''
	c=''
	
	s1=', '.join(str(x) for x in outputdp[int(z[0,0])])
	a=a+str(0+1)+") "+s1+" will result in "+str(int(z[0,1]*100))+"% chance of being sold.\n"
	s2=', '.join(str(x) for x in outputdp[int(z[1,0])])
	b=b+str(1+1)+") "+s2+" will result in "+str(int(z[1,1]*100))+"% chance of being sold.\n"
	s3=', '.join(str(x) for x in outputdp[int(z[2,0])])
	c=c+str(2+1)+") "+s3+" will result in "+str(int(z[2,1]*100))+"% chance of being sold.\n"
	
	return a,b,c	
	






#-------------------------------------------------------------------------------------------------------
@app.route('/')
def index():
    return render_template("index.html")

# @app.route('/preview')
# def preview():
#     df = pd.read_csv("data/id_101.csv")
    
#     return render_template("preview.html",df_view = df[['item_id', 'item_category', 'company', 'no_items_recieved', 'no_items_remaining', 'date_recieved', 'selling_price']])


# @app.route('/',methods=["POST"])
# def analyze():
# 	if request.method == 'POST':
# 		inventory_id = request.form['inv_id']
# 		category = request.form['category']
# 		company = request.form['company']
# 		targaud = request.form['targaud']
# 		noofitems = request.form['noofitems']
# 		price = request.form['price']
# 		year = request.form['year']
# 		demandfac = request.form['demandfac']
# 		profit = request.form['profit']

# 		# Clean the data by convert from unicode to float 
# 		sample_data = [[inventory_id,category,company, targaud, noofitems,int(price), int(year), int(demandfac), float(profit)]]
		
# 		# Reloading the Model
# 		for i in sample_data:
# 			a,b,c = doeverything(i)

# 	return render_template('index.html', inv_id=inventory_id,
# 		category=category,
# 		company=company,
# 		targaud=targaud,
# 		noofitems=noofitems,
# 		price=price,
# 		year=year,
# 		demandfac=demandfac,
# 		profit=profit,
# 		result_prediction1=a,
# 		result_prediction2=b,
# 		result_prediction3=c
# 		)


if __name__ == '__main__':
	app.run(debug=True)