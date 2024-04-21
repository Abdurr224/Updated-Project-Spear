import os
import sys
import time
import numpy as np
import pandas as pd
import datetime
import seaborn as sns
import subprocess

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score
from GenericDatasetEngine import GenData
from winotify import Notification, audio

def SpearNotification():
    toast = Notification(app_id= "Spear AntiPhishing Software©",
                         title = "Suspicious Content Detected",
                         msg = "Scan Has Detected Phishing",
                         duration = "short",
                         icon = "")
    toast.set_audio(audio.Default , loop= False)
    toast.show()


def close():
     print("Scan Another File?   Y / N")
     restart = input().upper()
     if restart == "Y":
               subprocess.call([sys.executable, 'Roles Test.py'])
        
     else:
        print("Closing...")
        time.sleep(2)
        sys.exit  




def Gendata():
     print("Would you like to test on a common dataset?   Y / N")
     restart = input().upper()
     if restart == "Y":
               GenData()
        
     if restart == "N":
        print("Closing...")
        time.sleep(2)
        sys.exit()   




def Report():
     with open("Report.txt", 'a') as file:
        file.write("\n")
        file.write("_________________________________________")
        file.write("\n")
        file.write("Workstation Staff ID: ")
        file.write(os.getlogin())
        file.write("\n")
        file.write(datetime.datetime.now().strftime("%d-%b-%Y (%H:%M:%S.%f)"))
        file.write("\n")
        file.write("")
 

def AccData():
         
    #Dataset Preperation
    data = pd.read_csv("Real Set 2.csv")
    data.head()

    data.shape

    data['Body'][0]

    data['Rating'].value_counts()

    data.duplicated().sum()

    data.drop_duplicates(inplace=True)
    data.duplicated().sum()

    data.isnull().sum()

    data.shape

    data['Rating'].value_counts()

    #Train Columns
    X = data['Body'].values
    y = data['Rating'].values

    X_train, X_test, y_train, y_test = train_test_split(X,y, test_size = 0.2 , random_state= 0)

    X_train.shape
    X_test.shape
    y_train.shape
    y_test.shape

    cv = CountVectorizer()
    x_train = cv.fit_transform(X_train)

    x_train.toarray()

    len(x_train.toarray())
    len(x_train.toarray()[0])

    nb = MultinomialNB()

    nb.fit(x_train, y_train)

    x_test = cv.transform(X_test)

    len(x_test.toarray())
    len(x_test.toarray()[0])

    y_pred = nb.predict(x_test)

    acc_score = accuracy_score(y_pred, y_test)
    percentage_acc = round(acc_score * 100)

    acc_score2 = nb.score(x_train,y_train)
    percentage_acc2 = round(acc_score2 * 100)



    print("This Accountant Dataset has:")
    print("Testing Accuracy:", percentage_acc, "%")

    print("Training Accuracy:", percentage_acc2, "%")
    print()
    filename = input('File Name: ')

    try:
        with open(filename, "r") as file:
            email = " ".join(file.read().splitlines())  

        email = [email]


        clean_email = cv.transform(email)
        check = nb.predict(clean_email)[0]
        print()
        if check == 0:
            print("There are no signs of phishing detected in this email ")
            Gendata()
            close()
        else:
            print("There are signs of phishing detected in this email ")
            print("This email will be archived")
            SpearNotification()
            Report()
            with open("Report.txt","a")as f:
             f.write(str(email))
            close()
            sys.exit
    except FileNotFoundError :
             print("File Not Found")        
             close()
if __name__ == "__main__":
    
    pass
