# spam-ham

Data set : https://github.com/diazonic/Machine-Learning-using-sklearn/edit/master/Datasets/spam.tsv

step-1 :- split the given data (Tokanization)


step-2 :- trian and test the data by the Pipelinevectorizer or Tfidfvectorizer from sklearn 
         * when using Pipelinevectorizer the data is trained by the fit in text_model by the SVC(support vectorizer classifier)
         * when using Tfidfvectorizer the data is trained by the fit_transform and 
           test the data by transform.
step-3 :- saving your model with complete pipeline (Serialization(dump) and deserialization(load)).
         * pickle
         *Joblib
         *sklearn.Json
step-4 :- dump the saved model by Joblib 
step-5 :- load the saved model in another google colab  
step-6 :- deploye the spam-ham classifier  by using the pyngrok and streamlit.
