# Rossmann-Sales-Prediction

(project repoert available in pdf)

Rossmann operates over 3,000 drug stores in 7 European countries. Currently, Rossmann store managers are tasked with predicting their daily sales for up to six weeks in advance. Store sales are influenced by many factors, including promotions, competition, school and state holidays, seasonality, and locality. With thousands of individual managers predicting sales based on their unique circumstances, the accuracy of results can be quite varied.
You are provided with historical sales data for 1,115 Rossmann stores. The task is to forecast the "Sales" column for the test set. Note that some stores in the dataset were temporarily closed for refurbishment


## Evaluation Criteria:
Submissions are evaluated on the Root Mean Square Percentage Error(RMSPE). Lower the score 
better will be the prediction.


## conclusion:

From results we not observed much of seasonality even small increase of sales in December. But which 
can also be valid considering fact that these are drug stores. So will not be much affected by festival 
season. But it is observed that AvgSales for Rossmann stores are increasing year by year from 2013-2015. 
So as a company it is doing well so AvgSales show growth of 3-5% each year. This is important in 
predicting future sales. 

While performing experiment addition and removal of features such as StoreType, Assortment, Month 
and Year in training data to models not shown much impact on results. Changes in RMSPE score very 
less in each scenario and even not consistent. So we can say that that these features are not impacting 
sales that much. 

In conclusion this is very interesting Data Science problem to solve where feature selection is important 
part of prediction accurately. I was able to successfully forecast daily sales for these stores using Linear 
Regression, Decision Tree Regression and Random Forest Regression models. I also analyzed trends and 
useful insights from results which can be prove to be important for Rossmann. In future I can work on 
other regression methods such as gradient boosting to improve results further. Also there is scope to add 
external real world features about these stores to predict future sales more accurately.


