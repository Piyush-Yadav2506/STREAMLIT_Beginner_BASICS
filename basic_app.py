import streamlit as st

st.title("Basis App")
st.subheader("This is a beginner friendly Streamlit basic app to get familiar with the basic Streamlit Structure.")
st.text("Welcome to your first interaction.")

choice = st.selectbox("Your favourite food:",['Indian','Mexican','Chinese','Russian','Continental',
                                     'Korean','Thai'])
st.write(f"You selected {choice}. Excellent Choice/n Have a Nice Day")