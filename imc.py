import streamlit as st

poids = st.number_input(" donnez le poids (kg) : ")
taille = st.number_input(" donnez la taille (m) : ")

if st.button(" calcul "):
    
    IMC = poids / (taille ** 2)

    if IMC < 18.5:
        st.warning(" maigre ")

    elif 18.5 <= IMC < 25:
        st.success(" poids normal ")

    elif 25 <= IMC < 30:
        st.warning(" surpoids ")

    elif IMC >= 30:
        st.warning(" obèse ")
    else:
        st. info("ceci n'est pas un nombre")
