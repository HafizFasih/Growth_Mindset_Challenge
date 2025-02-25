import streamlit as st

def convert_units(value, from_unit, to_unit):
    conversion_factors = {
        "Kilometre": 1000,
        "Metre": 1,
        "Centimetre": 0.01,
        "Millimetre": 0.001,
        "Micrometre": 1e-6,
        "Nanometre": 1e-9,
        "Mile": 1609.34,
        "Yard": 0.9144,
        "Foot": 0.3048,
        "Inch": 0.0254,
        "Nautical Mile": 1852
    }
    
    if from_unit not in conversion_factors or to_unit not in conversion_factors:
        return None
    
    value_in_metres = value * conversion_factors[from_unit]
    converted_value = value_in_metres / conversion_factors[to_unit]
    return converted_value

st.title("Unit Converter")

units = ["Kilometre", "Metre", "Centimetre", "Millimetre", "Micrometre", "Nanometre", "Mile", "Yard", "Foot", "Inch", "Nautical Mile"]

col1, col2 = st.columns(2)

with col1:
    from_unit = st.selectbox("From Unit:", units, key="from_unit")
    value = st.number_input("Enter value:", min_value=0.0, format="%f", key="value")

with col2:
    to_unit = st.selectbox("To Unit:", units, key="to_unit")
    converted_value = st.number_input("Converted value:", value=convert_units(value, from_unit, to_unit) if from_unit != to_unit else value, format="%f", key="converted_value", disabled=True)