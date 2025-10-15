import streamlit as st
import pandas as pd
import pickle

st.set_page_config(page_title="Predict DNF", page_icon="🚦")

# Load models
model = pickle.load(open('rfc_model.pkl', 'rb'))
encoder = pickle.load(open('encoder.pkl', 'rb'))
data = pickle.load(open('lists.pkl','rb'))

st.title("🚦 F1 Race Outcome Prediction")

st.markdown("Enter race details below to predict whether the driver will **Finish** or **DNF**.")

with st.form("dnf_form"):
    grid = st.number_input("Grid Position", min_value=1, max_value=24, step=1)
    year = st.number_input("Year", min_value=1950, max_value=2024, step=1)
    age = st.number_input("Driver Age", min_value=18, max_value=59, step=1)

    driver = st.selectbox("Driver", data['drivers'])
    constructor = st.selectbox("Constructor", data['constructors'])
    circuit_id = st.number_input("Circuit ID", min_value=1, max_value=100, step=1)

    submitted = st.form_submit_button("Predict 🚀")

if submitted:
    input_df = pd.DataFrame([[year, age, grid, driver, constructor, circuit_id]],
                            columns=['year', 'age', 'grid', 'driverRef', 'constructorRef', 'circuitId'])

    encoded_cols = encoder.transform(input_df)
    prediction = model.predict(encoded_cols)[0]

    st.subheader("🏁 Prediction Result")

    if prediction == 0:
        st.error("🚨 The driver is likely to **DNF (Did Not Finish)**.")
    else:
        st.success("✅ The driver is likely to **finish the race!**")

    with st.expander("🔍 View Encoded Input Data"):
        st.dataframe(encoded_cols)
