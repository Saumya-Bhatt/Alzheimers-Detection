from sklearn.metrics import confusion_matrix, accuracy_score, recall_score, roc_curve, auc
import pickle
from preprocess import clean,split

def score(filename,disp=True):
    cleaned_df=clean('oasis_longitudinal.csv')
    _,X_test,_,Y_test=split(cleaned_df)

    model=pickle.load(open(filename, 'rb'))
    Y_pred=model.predict(X_test)
    recall=recall_score(Y_test,Y_pred)
    accuracy=accuracy_score(Y_test,Y_pred)
    if disp:
        print(model)
        print(f"Accuracy = {accuracy}")
        print(f"Recall= {recall}")
    return model
    
if __name__=="__main__":
    # load the trained model. if you don't want to display the scores of the model set the argument disp=False.
    model=score('model_files/logistic.sav')