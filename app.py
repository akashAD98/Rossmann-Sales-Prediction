from flask import Flask,render_template,request
import pickle
import pandas as pd
import numpy as np
from flask_cors import  cross_origin
#Load pickel file
model = pickle.load(open('model_storetype.pkl', 'rb'))




app = Flask(__name__)

@cross_origin()
@app.route('/')
def home():
    return render_template('index.html')

@cross_origin()
@app.route('/predict',methods=['POST'])
def predict():



# Store	DayOfWeek,Sales,Promo,StateHoliday,SchoolHoliday,CompetitionDistance,Promo2,Month,Year,Day,is_Assortment_a,is_Assortment_b,is_Assortment_c,is_StoreType_a,is_StoreType_b,is_StoreType_c,is_StoreType_d,is_PromoInteval_0,PromoInt_Feb_May_Aug_Nov, PromoInt_Jan_Apr_Jul_Oct

    Store = float(request.form['store'])
    DayOfWeek = float(request.form['dayofWeek'])
    Promo = float(request.form['promo'])
    StateHoliday = float(request.form['stateHoliday'])
    SchoolHoliday = float(request.form['schoolHoliday'])
    CompetitionDistance = float(request.form['competitionDistance'])


    Promo2=request.form['promo2']
    Month = int(request.form['month'])
    Year = int(request.form['year'])
    Day= int(request.form['day'])

    Assortment = request.form["assortment"]

    if (Assortment == 'is_Assortment_a'):
        is_Assortment_a = 1
        is_Assortment_b = 0
        is_Assortment_c = 0


    elif (Assortment == 'is_Assortment_b'):
        is_Assortment_a = 0
        is_Assortment_b = 1
        is_Assortment_c = 0


    elif (Assortment == 'is_Assortment_c'):
        is_Assortment_a = 0
        is_Assortment_b = 1
        is_Assortment_c = 0

    else:
        is_Assortment_a = 0
        is_Assortment_b = 0
        is_Assortment_c = 0



    StoreType = request.form['storeType']
    if (StoreType == 'is_StoreType_a'):

         is_StoreType_a= 1
         is_StoreType_b = 0
         is_StoreType_c= 0
         is_StoreType_d=0
    elif (StoreType == 'is_StoreType_b'):
        is_StoreType_a = 0
        is_StoreType_b = 1
        is_StoreType_c = 0
        is_StoreType_d =0

    elif (StoreType == 'is_StoreType_c'):
        is_StoreType_a = 0
        is_StoreType_b = 0
        is_StoreType_c = 1
        is_StoreType_d = 0

    elif (StoreType == 'is_StoreType_d'):
        is_StoreType_a = 0
        is_StoreType_b = 0
        is_StoreType_c = 0
        is_StoreType_d = 1

    else:
        is_StoreType_a = 0
        is_StoreType_b = 0
        is_StoreType_c = 0
        is_StoreType_d = 0


    data = [Store,DayOfWeek,Promo,StateHoliday,SchoolHoliday,CompetitionDistance,Promo2,Month,Year,Day,is_Assortment_a,is_Assortment_b,is_Assortment_c,is_StoreType_a,is_StoreType_b,is_StoreType_c,is_StoreType_d]
    features_value = [np.array(data)]

    features_name = ['Store','DayOfWeek','Promo','StateHoliday','SchoolHoliday','CompetitionDistance','Promo2','Month','Year','Day','is_Assortment_a','is_Assortment_b','is_Assortment_c','is_StoreType_a','is_StoreType_b','is_StoreType_c','is_StoreType_d']

    df = pd.DataFrame(features_value, columns=features_name)

    myprd = model.predict(df)
    output=round(myprd[0],2)

    # if output < 0:
    #     return render_template('index.html',prediction_texts="Sorry you cannot sell")
    # else:
    #     return render_template('index.html',prediction_text="Item_Outlet_Sales at {}".format(output))

    return render_template('result.html',prediction = output)
    #return render_template('result.html', prediction_text='The Sales production of {} by {} is  {}  price'.format(Item_Identifier,Outlet_ID,output))


if __name__ == "__main__":
    app.run(host='127.0.0.1', port=8000, debug=True)