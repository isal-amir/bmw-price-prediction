import streamlit as st
from predict import predict_price

st.title(' BMW Car Price Predictor')

st.write('Predict the resale pricec of a BMW car using a Machine Learning Model')


# ===== INPUT =====

car_model = st.selectbox(
    'Model',[' 5 Series', ' 6 Series', ' 1 Series', ' 7 Series', ' 2 Series',
       ' 4 Series', ' X3', ' 3 Series', ' X5', ' X4', ' i3', ' X1', ' M4',
       ' X2', ' X6', ' 8 Series', ' Z4', ' X7', ' M5', ' i8', ' M2',
       ' M3', ' M6', ' Z3']
)

year = st.slider("year", 1990, 2024)

transmission = st.selectbox(
    "Transmission",
    ['Automatic', 'Manual', 'Semi-Auto']
)

mileage = st.number_input('mileage')

fuelType = st.selectbox(
    'Fuel Type',
    ['Diesel', 'Petrol', 'Other', 'Hybrid']
)

tax = st.number_input('Yearly Tax')

mpg = st.number_input('Miles per Galon')

engineSize = st.slider('Engine Size', 0.6, 6.6)

# ========== Process ========

if st.button("Predict Price"):
    input_data = {
        "model": car_model,
        "year": year,
        'transmission': transmission,
        'mileage': mileage,
        "fuelType": fuelType,
        "tax": tax,
        "mpg": mpg,
        "engineSize": engineSize
    }

    price = predict_price(input_data)
    st.success(f'estimated Car Price: ${price:,.2f}')