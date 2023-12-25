import streamlit as st 
import pickle

model = pickle.load(open(model.pkl','rb'))

st.title('Predicting if messages is positive or not')

message = st.text_input('Enter a message')
submit = st.button("Predict")
if submit:
    prediction = model.predict([message])
    
    print(prediction)
    st.write(prediction)
