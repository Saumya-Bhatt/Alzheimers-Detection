from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import AdaBoostClassifier
import pickle
from preprocess import clean,split

cleaned_df=clean('oasis_longitudinal.csv')
X_train,X_test,Y_train,Y_test=split(cleaned_df)

logistic_model=LogisticRegression(C=10).fit(X_train,Y_train)
forest_model = RandomForestClassifier(n_estimators=3, max_features=4, n_jobs=4, max_depth=5, random_state=0).fit(X_train,Y_train)
tree_model = DecisionTreeClassifier(random_state=0, max_depth=1, criterion='gini').fit(X_train,Y_train)
adaboost_model=AdaBoostClassifier(n_estimators=3, learning_rate=0.0001, random_state=0).fit(X_train,Y_train)

pickle.dump(logistic_model, open('model_files/logistic.sav', 'wb'))
pickle.dump(forest_model,open('model_files/forest.sav','wb'))
pickle.dump(tree_model,open('model_files/tree.sav','wb'))
pickle.dump(adaboost_model,open('model_files/adaboost.sav','wb'))

