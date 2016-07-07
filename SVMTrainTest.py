#SVMTrainTest.py

#import statements
import cv2
import numpy as np
from sklearn import metrics
from sklearn.svm import SVC
from sklearn.cross_validation import train_test_split
from sklearn.preprocessing import Imputer

#Read in the directory where the positive and negative samples are
ncsv="/home/pinosjxp/Desktop/Senior/negative/NegativeImages.csv"
pcsv="/home/pinosjxp/Desktop/Senior/positive/PositiveImages.csv"

#Begin the SVM training
nMatrix=np.loadtxt(ncsv,dtype=str,delimiter=",")
pMatrix=np.loadtxt(pcsv,dtype=str,delimiter=",")
nMatrix=np.asarray(nMatrix,dtype=np.float32)
pMatrix=np.asarray(pMatrix,dtype=np.float32)

dataset = np.concatenate([nMatrix, pMatrix], axis=0)

labels = [i for i in dataset[:,-1]]
data = dataset[:,0:-1]
data[data==0.0]=np.nan
imp=Imputer(missing_values='NaN',strategy='mean')
idata=imp.fit_transform(data)
print(idata)
data_train,data_test,target_train,target_test=train_test_split(idata,labels,test_size=0.3)
model=SVC(C=0.01,kernel='linear', class_weight='auto')
print(data_train.shape)
#print(target_train.shape)
model.fit(data_train,target_train)
    
opencv_data_train=np.float32(data_train)
opencv_target_train=np.int32(target_train)     
svm = cv2.ml.SVM_create()
svm.setGamma(5.383)
svm.setC(2.67)
svm.setKernel(cv2.ml.SVM_LINEAR)
svm.setType(cv2.ml.SVM_C_SVC)
svm.train(opencv_data_train,0,opencv_target_train)
svm.save("hog_classifier.xml")  
print(model)
expected=target_test
predicted=model.predict(data_test)
target_names = ['Not Human', 'Human']

#print the confusion matrix and classification report
print(metrics.classification_report(expected,predicted,target_names=target_names))
print(metrics.confusion_matrix(expected,predicted))
