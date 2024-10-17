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

# Streamlit app styling
st.markdown(
    """
    <style>
    /* Background Styling */
    .stApp {
        background-image: url('https://images.unsplash.com/photo-1606788075761-9a7694ff5df1');
        background-size: cover;
        background-position: center;
    }
    /* Main title styling */
    .main-title {
        font-size: 36px;
        color: #2E86C1;
        text-align: center;
        font-weight: bold;
        margin-bottom: 20px;
        text-shadow: 2px 2px #F0F3F4;
    }
    /* Button styling */
    .convert-button, .clear-button {
        width: 100%;
        height: 40px;
        font-size: 18px;
        font-weight: bold;
        border-radius: 5px;
        color: white;
    }
    .convert-button {
        background-color: #4CAF50;
    }
    .clear-button {
        background-color: #e74c3c;
    }
    /* Conversion history styling */
    .history-entry {
        color: #FFFFFF;
        font-weight: 500;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Main title
st.markdown('<p class="main-title">🌡️ Temperature Converter</p>', unsafe_allow_html=True)

# Layout: columns for input and output
col1, col2 = st.columns(2)

# Temperature Conversion
with col1:
    conversion_type = st.radio("Choose the conversion type:", ("Celsius to Fahrenheit", "Fahrenheit to Celsius"))

    if conversion_type == "Celsius to Fahrenheit":
        celsius = st.number_input("Enter temperature in Celsius:", format="%.2f")
        if st.button("Convert", key="convert1", help="Convert Celsius to Fahrenheit"):
            fahrenheit = celsius_to_fahrenheit(celsius)
            st.session_state["history"].append(f"{celsius}°C = {fahrenheit:.2f}°F")
            st.success(f"{celsius}°C is equal to {fahrenheit:.2f}°F")
            
    elif conversion_type == "Fahrenheit to Celsius":
        fahrenheit = st.number_input("Enter temperature in Fahrenheit:", format="%.2f")
        if st.button("Convert", key="convert2", help="Convert Fahrenheit to Celsius"):
            celsius = fahrenheit_to_celsius(fahrenheit)
            st.session_state["history"].append(f"{fahrenheit}°F = {celsius:.2f}°C")
            st.success(f"{fahrenheit}°F is equal to {celsius:.2f}°C")

# Display Conversion History
with col2:
    st.write("### Conversion History")
    if st.session_state["history"]:
        for entry in st.session_state["history"][-5:]:  # Show last 5 conversions
            st.markdown(f'<p class="history-entry">{entry}</p>', unsafe_allow_html=True)
    else:
        st.write("No conversions yet.")

# Clear history button
if st.button("Clear History", key="clear", help="Clear conversion history"):
    st.session_state["history"].clear()
    st.info("History cleared.")
