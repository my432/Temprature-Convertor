# Install Streamlit by running: pip install streamlit
import streamlit as st

# Temperature conversion functions
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

# Initialize conversion history
if "history" not in st.session_state:
    st.session_state["history"] = []

# Streamlit app
st.markdown(
    """
    <style>
    .main-title {
        font-size: 32px;
        color: #4B8BBE;
        text-align: center;
        font-weight: bold;
    }
    .convert-button {
        background-color: #4CAF50;
        color: white;
    }
    .clear-button {
        background-color: #f44336;
        color: white;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown('<p class="main-title">🌡️ Temperature Converter</p>', unsafe_allow_html=True)

# Layout: columns for input and output
col1, col2 = st.columns(2)

with col1:
    # Selection of conversion type
    conversion_type = st.radio("Choose the conversion type:", ("Celsius to Fahrenheit", "Fahrenheit to Celsius"))
    
    if conversion_type == "Celsius to Fahrenheit":
        celsius = st.number_input("Enter temperature in Celsius:", format="%.2f")
        if st.button("Convert", key="convert1"):
            fahrenheit = celsius_to_fahrenheit(celsius)
            st.session_state["history"].append(f"{celsius}°C = {fahrenheit:.2f}°F")
            st.success(f"{celsius}°C is equal to {fahrenheit:.2f}°F")
            
    elif conversion_type == "Fahrenheit to Celsius":
        fahrenheit = st.number_input("Enter temperature in Fahrenheit:", format="%.2f")
        if st.button("Convert", key="convert2"):
            celsius = fahrenheit_to_celsius(fahrenheit)
            st.session_state["history"].append(f"{fahrenheit}°F = {celsius:.2f}°C")
            st.success(f"{fahrenheit}°F is equal to {celsius:.2f}°C")

# Display Conversion History
with col2:
    st.write("### Conversion History")
    if st.session_state["history"]:
        for entry in st.session_state["history"][-5:]:  # Display the last 5 conversions
            st.write(entry)
    else:
        st.write("No conversions yet.")

# Clear history button
if st.button("Clear History", key="clear"):
    st.session_state["history"].clear()
    st.info("History cleared.")

# Add padding for a more professional look
st.markdown("<br><br>", unsafe_allow_html=True)
