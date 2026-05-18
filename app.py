import streamlit as st

# Title with your name
st.title("Mechanical Unit Converter & Density Checker")
st.markdown("### Abdul Wahab Khan | Roll No: 25-ME-32")

st.write("---")

# Sidebar selection
option = st.sidebar.selectbox(
    "Select Function",
    ["Unit Converter", "Density Checker"]
)

# ---------------- UNIT CONVERTER ----------------
if option == "Unit Converter":
    st.header("🔄 Unit Converter")

    category = st.selectbox(
        "Select Category",
        ["Length", "Mass", "Temperature"]
    )

    # LENGTH
    if category == "Length":
        value = st.number_input("Enter value")

        unit_from = st.selectbox("From", ["meter", "centimeter", "millimeter"])
        unit_to = st.selectbox("To", ["meter", "centimeter", "millimeter"])

        # Convert to meters first
        if unit_from == "meter":
            base = value
        elif unit_from == "centimeter":
            base = value / 100
        elif unit_from == "millimeter":
            base = value / 1000

        # Convert to target
        if unit_to == "meter":
            result = base
        elif unit_to == "centimeter":
            result = base * 100
        elif unit_to == "millimeter":
            result = base * 1000

        st.success(f"Converted Value: {result}")

    # MASS
    elif category == "Mass":
        value = st.number_input("Enter value")

        unit_from = st.selectbox("From", ["kg", "gram"])
        unit_to = st.selectbox("To", ["kg", "gram"])

        if unit_from == "kg":
            base = value
        elif unit_from == "gram":
            base = value / 1000

        if unit_to == "kg":
            result = base
        elif unit_to == "gram":
            result = base * 1000

        st.success(f"Converted Value: {result}")

    # TEMPERATURE
    elif category == "Temperature":
        value = st.number_input("Enter value")

        unit_from = st.selectbox("From", ["Celsius", "Fahrenheit"])
        unit_to = st.selectbox("To", ["Celsius", "Fahrenheit"])

        if unit_from == "Celsius" and unit_to == "Fahrenheit":
            result = (value * 9/5) + 32
        elif unit_from == "Fahrenheit" and unit_to == "Celsius":
            result = (value - 32) * 5/9
        else:
            result = value

        st.success(f"Converted Value: {result}")

# ---------------- DENSITY CHECKER ----------------
elif option == "Density Checker":
    st.header("⚖️ Density Checker")

    mass = st.number_input("Enter Mass (kg)")
    volume = st.number_input("Enter Volume (m³)")

    if st.button("Calculate Density"):
        if volume != 0:
            density = mass / volume
            st.success(f"Density = {density} kg/m³")

            # Material check
            if density < 1000:
                st.info("Material is likely less dense (like wood or plastic)")
            elif 1000 <= density <= 8000:
                st.info("Material is medium density (like metals)")
            else:
                st.info("Material is very dense (like heavy metals)")
        else:
            st.error("Volume cannot be zero!")
