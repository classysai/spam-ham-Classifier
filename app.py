import streamlit as st
import joblib
model=joblib.load("spam-ham")
st.title('Spam Ham Classifier')
st.image("/content/OIP.jpeg",width=800,)
ip=st.text_input("Enter the message")
op=model.predict([ip])
if st.button("predict"):
  st.title(op[0])
  st.subheader("successfully Done by the sai kian")
