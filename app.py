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
    /* Background gradient */
    .reportview-container {
        background: linear-gradient(120deg, #a1c4fd, #c2e9fb);
        padding: 1rem;
    }
    
    /* Main title styling */
    .main-title {
        font-size: 36px;
        color: #fff;
        text-align: center;
        font-weight: bold;
        padding: 0.5rem;
        border-radius: 10px;
        background-color: #3B8BBE;
        box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.2);
    }

    /* Button styling */
    .stButton>button {
        background-color: #3B8BBE;
        color: white;
        border-radius: 8px;
        padding: 0.5rem 1.5rem;
        font-size: 1rem;
        font-weight: bold;
        box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.2);
        transition: all 0.3s ease;
    }
    
    .stButton>button:hover {
        background-color: #5390D9;
        color: #FFFFFF;
        transform: scale(1.05);
    }

    /* Clear history button */
    .clear-button {
        background-color: #f44336;
        color: white;
        border-radius: 8px;
        padding: 0.5rem 1.5rem;
        font-size: 1rem;
        font-weight: bold;
        box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.2);
        transition: all 0.3s ease;
    }
    
    .clear-button:hover {
        background-color: #e53935;
        color: #FFFFFF;
        transform: scale(1.05);
    }

    /* History container styling */
    .history-container {
        background: rgba(255, 255, 255, 0.7);
        padding: 1rem;
        border-radius: 10px;
        box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.2);
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown('<div class="main-title">🌡️ Temperature Converter</div>', unsafe_allow_html=True)

# Layout: columns for input and output
col1, col2 = st.columns(2)

with col1:
    # Selection of conversion type
    conversion_type = st.radio("Choose the conversion type:", ("Celsius to Fahrenheit", "Fahrenheit to Celsius"))
    
    if conversion_type == "Celsius to Fahrenheit":
        celsius = st.number_input("Enter temperature in Celsius:", format="%.2f")
        if st.button("Convert"):
            fahrenheit = celsius_to_fahrenheit(celsius)
            st.session_state["history"].append(f"{celsius}°C = {fahrenheit:.2f}°F")
            st.success(f"{celsius}°C is equal to {fahrenheit:.2f}°F")
            
    elif conversion_type == "Fahrenheit to Celsius":
        fahrenheit = st.number_input("Enter temperature in Fahrenheit:", format="%.2f")
        if st.button("Convert"):
            celsius = fahrenheit_to_celsius(fahrenheit)
            st.session_state["history"].append(f"{fahrenheit}°F = {celsius:.2f}°C")
            st.success(f"{fahrenheit}°F is equal to {celsius:.2f}°C")

# Display Conversion History
with col2:
    st.write("### Conversion History")
    st.markdown('<div class="history-container">', unsafe_allow_html=True)
    if st.session_state["history"]:
        for entry in st.session_state["history"][-5:]:  # Display the last 5 conversions
            st.write(entry)
    else:
        st.write("No conversions yet.")
    st.markdown('</div>', unsafe_allow_html=True)

# Clear history button
if st.button("Clear History", key="clear"):
    st.session_state["history"].clear()
    st.info("History cleared.")
