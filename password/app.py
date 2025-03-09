
import streamlit as st
import pint

ureg = pint.UnitRegistry()

st.title("Unit Converter")

st.sidebar.header("Select Unit Type")
unit_types = ["Length", "Weight", "Temperature", "Volume", "Area", "Time"]
selected_unit_type = st.sidebar.selectbox("Unit Type", unit_types)

if selected_unit_type == "Length":
    units = ["meter", "kilometer", "centimeter", "millimeter", "inch", "foot", "yard", "mile"]
elif selected_unit_type == "Weight":
    units = ["kilogram", "gram", "milligram", "pound", "ounce", "ton"]
elif selected_unit_type == "Temperature":
    units = ["celsius", "fahrenheit", "kelvin"]
elif selected_unit_type == "Volume":
    units = ["liter", "milliliter", "gallon", "quart", "pint"]
elif selected_unit_type == "Area":
    units = ["square meter", "square kilometer", "square centimeter", "square foot", "square inch", "acre"]
elif selected_unit_type == "Time":
    units = ["second", "minute", "hour", "day", "week", "month", "year"]
else:
    units = []

if units:
    col1, col2 = st.columns(2)
    with col1:
        from_unit = st.selectbox("From Unit", units)
    with col2:
        to_unit = st.selectbox("To Unit", units)

    value = st.number_input("Enter Value", value=0.0, step=0.1)

    try:
        if value is not None:
            quantity = value * ureg(from_unit)
            converted_quantity = quantity.to(to_unit)
            st.success(f"{value} {from_unit} is equal to {converted_quantity:~.2f} {to_unit}")
    except Exception as e:
        st.error(f"Error: {e}")

st.markdown("---")
st.write("Developed by: [Your Name]")


