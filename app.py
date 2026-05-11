import streamlit as st

# Custom Styling
st.set_page_config(page_title="Mechanical Toolset", page_icon="⚙️")

# --- HEADER SECTION ---
st.title("⚙️ Mechanical Unit Converter & Density Checker")
st.markdown(f"""
**Name:** M ALIABDULLAH  
**Roll Number:** 25-ME-208
""")
st.divider()

# --- SIDEBAR NAVIGATION ---
option = st.sidebar.selectbox("Select Function", ["Unit Converter", "Material Density Checker"])

# --- UNIT CONVERTER ---
if option == "Unit Converter":
    st.header("🔄 Unit Converter")
    
    category = st.selectbox("Category", ["Length", "Pressure", "Mass"])
    
    col1, col2 = st.columns(2)
    
    if category == "Length":
        with col1:
            val = st.number_input("Value", value=1.0)
            unit_from = st.selectbox("From", ["Meters", "Millimeters", "Inches", "Feet"])
        
        # Conversion logic to Meters
        to_meters = {"Meters": 1.0, "Millimeters": 0.001, "Inches": 0.0254, "Feet": 0.3048}
        meters_val = val * to_meters[unit_from]
        
        with col2:
            unit_to = st.selectbox("To", ["Meters", "Millimeters", "Inches", "Feet"])
            result = meters_val / to_meters[unit_to]
            st.metric("Result", f"{result:.4f} {unit_to}")

    elif category == "Pressure":
        with col1:
            val = st.number_input("Value", value=1.0)
            unit_from = st.selectbox("From", ["Pascal", "Bar", "PSI", "Atm"])
        
        # Conversion logic to Pascal
        to_pascal = {"Pascal": 1.0, "Bar": 100000.0, "PSI": 6894.76, "Atm": 101325.0}
        pa_val = val * to_pascal[unit_from]
        
        with col2:
            unit_to = st.selectbox("To", ["Pascal", "Bar", "PSI", "Atm"])
            result = pa_val / to_pascal[unit_to]
            st.metric("Result", f"{result:.4f} {unit_to}")

# --- DENSITY CHECKER ---
else:
    st.header("⚖️ Material Density Checker")
    
    # Data dictionary (kg/m^3)
    densities = {
        "Steel": 7850,
        "Aluminum": 2700,
        "Copper": 8960,
        "Brass": 8500,
        "Titanium": 4500,
        "Cast Iron": 7200,
        "Water": 1000
    }
    
    selected_material = st.selectbox("Select Material", list(densities.keys()))
    density_val = densities[selected_material]
    
    st.info(f"The density of **{selected_material}** is approximately **{density_val} kg/m³**.")
    
    volume = st.number_input("Enter Volume (m³)", value=1.0)
    mass_calc = density_val * volume
    st.success(f"Estimated Mass: **{mass_calc:.2f} kg**")

st.sidebar.markdown("---")
st.sidebar.write("Developed for Mechanical Engineering Dept.")
