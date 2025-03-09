
import streamlit as st
import pandas as pd

st.title("Unit Converter")

unit_types = {
    "Length": {"m": 1, "cm": 0.01, "km": 1000, "ft": 0.3048, "in": 0.0254},
    "Weight": {"kg": 1, "g": 0.001, "lb": 0.4536, "oz": 0.02835},
    "Temperature": {"Celsius": 1, "Fahrenheit": lambda c: (c * 9/5) + 32, "Kelvin": lambda c: c + 273.15},
    "Volume": {"L": 1, "mL": 0.001, "gal": 3.78541, "qt": 0.946353}
}


def convert_units(unit_type, from_unit, to_unit, value):
    try:
        value = float(value)
        if unit_type == "Temperature":
            if from_unit == "Celsius":
                if to_unit == "Fahrenheit":
                    return unit_types[unit_type][to_unit](value)
                elif to_unit == "Kelvin":
                    return unit_types[unit_type][to_unit](value)
                else:
                    return value
            elif from_unit == "Fahrenheit":
                if to_unit == "Celsius":
                    return (value - 32) * 5/9
                elif to_unit == "Kelvin":
                    return (value - 32) * 5/9 + 273.15
                else:
                    return value
            elif from_unit == "Kelvin":
                if to_unit == "Celsius":
                    return value - 273.15
                elif to_unit == "Fahrenheit":
                    return (value - 273.15) * 9/5 + 32
                else:
                    return value

        else:
            return value * unit_types[unit_type][from_unit] / unit_types[unit_type][to_unit]
    except (ValueError, KeyError):
        return "Invalid input"


selected_unit_type = st.selectbox("Select Unit Type", list(unit_types.keys()))
from_unit = st.selectbox("From Unit", list(unit_types[selected_unit_type].keys()))
to_unit = st.selectbox("To Unit", list(unit_types[selected_unit_type].keys()))
value = st.text_input("Enter Value")


if st.button("Convert"):
    result = convert_units(selected_unit_type, from_unit, to_unit, value)
    st.success(f"Converted Value: {result}")

