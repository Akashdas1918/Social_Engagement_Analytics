
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, roc_auc_score, confusion_matrix, classification_report
import joblib
from metrics import add_engagement_metrics

def train_model(posts, model_path="models/viral_potential_model.joblib"):
    data, threshold = add_engagement_metrics(posts)
    features = ["topic","content_format","hook_type","caption_length","reach","retention_rate","likes","comments","shares","saves"]
    X, y = data[features], data["high_viral_potential"]
    cat = ["topic","content_format","hook_type","caption_length"]
    num = [c for c in features if c not in cat]
    prep = ColumnTransformer([
        ("cat", Pipeline([("impute",SimpleImputer(strategy="most_frequent")),("onehot",OneHotEncoder(handle_unknown="ignore"))]), cat),
        ("num", Pipeline([("impute",SimpleImputer(strategy="median")),("scale",StandardScaler())]), num)
    ])
    pipe = Pipeline([("prep",prep),("model",RandomForestClassifier(n_estimators=300,max_depth=10,class_weight="balanced",random_state=42))])
    Xtr,Xte,ytr,yte=train_test_split(X,y,test_size=.2,random_state=42,stratify=y)
    pipe.fit(Xtr,ytr)
    pred=pipe.predict(Xte)
    prob=pipe.predict_proba(Xte)[:,1]
    metrics={"accuracy":accuracy_score(yte,pred),"precision":precision_score(yte,pred,zero_division=0),"recall":recall_score(yte,pred,zero_division=0),"f1":f1_score(yte,pred,zero_division=0),"roc_auc":roc_auc_score(yte,prob),"confusion_matrix":confusion_matrix(yte,pred).tolist(),"classification_report":classification_report(yte,pred,output_dict=True),"label_threshold":threshold}
    joblib.dump(pipe,model_path)
    return pipe, metrics
