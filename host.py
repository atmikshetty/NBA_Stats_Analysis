import streamlit as st
import pickle

lr = pickle.load(open('nba_stat.pkl', 'rb'))

st.title('NBA 3 Point % Predictor')

GP = st.number_input('Enter the Games Played: ')
Min = st.number_input('Enter the Minutes Played: ')
FGM = st.number_input('Enter the Field Goals Made: ')
FGA = st.number_input('Enter the Field Goals Attempted: ')
FGP = st.number_input('Enter the Field Goals Percentage: ')
TPM = st.number_input('Enter the Three Pointers Made: ')
TPA = st.number_input('Enter the Three Pointers Attempted: ')
enc = st.number_input('Insert any number: ')

final = [[GP,Min,FGM,FGA,FGP,TPM,TPA,enc]]

if st.button('Predict'):
    result = lr.predict(final)
    st.header(result)

st.caption('Made by Atmik Shetty.')