import pandas as pd 
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
import matplotlib.pyplot as plt
#dilutedwines = AOD280/OD315 of diluted wines 

def WineDecisionTreeAlogrithm(Data):

   
    features_name = ['Alcohol','Malicacid','Ash','Alcalinityofash','Magnesium','Totalphenols','Flavanoids','Nonflavanoidphenols','Proanthocyanins','Colorintensity','Hue','dilutedwines','Proline']
    #print("Name of Features :",features_name)
    
    Class = Data.Class

    Alcohol = Data.Alcohol
    Malicacid =Data.Malicacid
    Ash = Data.Ash
    Alcalinityofash =Data.Alcalinityofash
    Magnesium = Data.Magnesium
    Totalphenols = Data.Totalphenols
    Flavanoids = Data.Flavanoids
    Nonflavanoidphenols = Data.Nonflavanoidphenols
    Proanthocyanins = Data.Proanthocyanins
    Colorintensity = Data.Colorintensity
    Hue = Data.Hue
    dilutedwines = Data.dilutedwines
    Proline = Data.Proline

    

    features = list(zip(Alcohol, Malicacid ,Ash, Alcalinityofash, Magnesium ,Totalphenols , Flavanoids, Nonflavanoidphenols,Proanthocyanins,Colorintensity,Hue,dilutedwines,Proline ))
    Data_train,Data_test,Target_train,Target_test = train_test_split(features ,Class, test_size =0.5)

    Classifer = DecisionTreeClassifier()

    Classifer.fit(Data_train ,Target_train)
    Predictions = Classifer.predict(Data_test)

    Accuracy =accuracy_score(Target_test ,Predictions)

    return Accuracy



def WineKNN(Data):
    features_name = ['Alcohol','Malicacid','Ash','Alcalinityofash','Magnesium','Totalphenols','Flavanoids','Nonflavanoidphenols','Proanthocyanins','Colorintensity','Hue','dilutedwines','Proline']
    #print("Name of Features :",features_name)
    
    Class = Data.Class

    Alcohol = Data.Alcohol
    Malicacid =Data.Malicacid
    Ash = Data.Ash
    Alcalinityofash =Data.Alcalinityofash
    Magnesium = Data.Magnesium
    Totalphenols = Data.Totalphenols
    Flavanoids = Data.Flavanoids
    Nonflavanoidphenols = Data.Nonflavanoidphenols
    Proanthocyanins = Data.Proanthocyanins
    Colorintensity = Data.Colorintensity
    Hue = Data.Hue
    dilutedwines = Data.dilutedwines
    Proline = Data.Proline

    

    features = list(zip(Alcohol, Malicacid ,Ash, Alcalinityofash, Magnesium ,Totalphenols , Flavanoids, Nonflavanoidphenols,Proanthocyanins,Colorintensity,Hue,dilutedwines,Proline ))
    Data_train,Data_test,Target_train,Target_test = train_test_split(features ,Class, test_size =0.5)

    model = KNeighborsClassifier()

    model.fit(Data_train ,Target_train)
    Predictions = model.predict(Data_test)

    Accuracy =accuracy_score(Target_test ,Predictions)

    return Accuracy
    


def main():
    border ="-"*80

    print(border)
    print("Wine Predictor Case Study")
    print(border)

    Data =pd.read_csv('WinePredictor(1).csv') 
    print("Size of Actual Data Set : ",len(Data))
    print(border)

    Accurancy = WineDecisionTreeAlogrithm(Data)
    print("Accurancy of Wine Predictor Case Study by Decision Tree Alogrithm ::",Accurancy)
    print(border)

    Accurancy1 = WineKNN(Data)
    print("Accurancy of Wine Predictor Case Study by KNN Alogrithm ::",Accurancy1)
    print(border)

    X =[Accurancy]
    Y = [0]
    plt.scatter(X,Y)
    plt.show()
    
    X =[Accurancy1]
    Y = [0]
    plt.scatter(X,Y)
    plt.show()
    


if __name__ == "__main__":
    main()