import streamlit as st 
import pickle

# Sửa tên file thành 'model.pkl'
model = pickle.load(open('model.pkl', 'rb'))

st.title('Predicting if messages are positive or not')

message = st.text_input('Enter a message')
submit = st.button("Predict")
if submit:
    prediction = model.predict([message])
    st.write(prediction)
