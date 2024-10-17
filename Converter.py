import streamlit as st

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

# Streamlit app
st.title("Temperature Converter")

st.sidebar.header("Select Conversion Type")
conversion_type = st.sidebar.selectbox("Choose an option:", ["Celsius to Fahrenheit", "Fahrenheit to Celsius"])

if conversion_type == "Celsius to Fahrenheit":
    celsius = st.number_input("Enter temperature in Celsius:", value=0.0)
    fahrenheit = celsius_to_fahrenheit(celsius)
    st.write(f"{celsius}°C is {fahrenheit:.2f}°F")
else:
    fahrenheit = st.number_input("Enter temperature in Fahrenheit:", value=32.0)
    celsius = fahrenheit_to_celsius(fahrenheit)
    st.write(f"{fahrenheit}°F is {celsius:.2f}°C")
