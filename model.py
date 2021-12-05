import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import pickle
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score


US_video=pd.read_csv("USvideos.csv")

US_video.drop(["tags","description","title","channel_title","publish_time", "video_id","thumbnail_link"],axis=1,inplace=True)
data1=US_video.copy(deep=True)
data1["comments_disabled"]=(data1["comments_disabled"]=="True").astype(int)
data1["ratings_disabled"]=(data1["ratings_disabled"]=="True").astype(int)
data1["video_error_or_removed"]=(data1["video_error_or_removed"]=="True").astype(int)
data1["likes"]=np.log(data1["likes"])
data1["dislikes"]=np.log(data1["dislikes"])
data1["views"]=np.log(data1["views"])
data1["comment_count"]=np.log(data1["comment_count"])
data1["views"]=data1["views"].replace([np.inf,-np.inf],np.nan)
data1["dislikes"]=data1["dislikes"].replace([np.inf,-np.inf],np.nan)
data1["likes"]=data1["likes"].replace([np.inf,-np.inf],np.nan)
data1["comment_count"]=data1["comment_count"].replace([np.inf,-np.inf],np.nan)

data1.isnull().sum()
data1.dropna(axis=0,how='any',inplace=True)
data1=pd.get_dummies(data1,drop_first=True)
x1=data1.drop("likes",axis=1,inplace=False)
x1 = data1[['category_id', 'views', 'dislikes',
       'comment_count', 'comments_disabled', 'ratings_disabled',
       'video_error_or_removed']]
x=x1.copy()

# us_yt2=us_yt2.drop(['trending_date','publish_date', 'days_diff','publish_year','ratings_disabled', 'video_error_or_removed','publish_time', 'tags'],axis=1)

categories=pd.get_dummies(x['category_id'], drop_first=True)
categories.head()
x=pd.concat((x,categories),axis=1)
x=x.drop(['category_id'],axis=1)
y=data1["likes"]
x=x.values
y=data1["likes"].values

x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.3,random_state=0)
# print(x_train[0])
lgr=LinearRegression(fit_intercept=True)
fit_model=lgr.fit(x_train,y_train)

prediction=lgr.predict(x_test)



filename = 'finalized_model.sav'
pickle.dump(lgr, open("model.pkl", 'wb'))
model=pickle.load(open("model.pkl",'rb'))