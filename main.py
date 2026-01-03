import streamlit as st

st.set_page_config(page_title="Intro to Python", layout="wide")

# Create pages
home_page = st.Page("pages/00_home.py", title="Home")
setup_page = st.Page("pages/01_setup.py", title="Setup")
variables_data_types_page = st.Page("pages/02_variables_data_types.py", title="Variables & Data Types")
basic_output_page = st.Page("pages/03_basic_output.py", title="Basic Output")
basic_math_page = st.Page("pages/04_basic_math.py", title="Basic Math Operations")
user_input_page = st.Page("pages/05_user_input.py", title="User Input")
planning_design_page = st.Page("pages/06_planning_and_design.py", title="Planning & Design")
conditionals_page = st.Page("pages/07_conditionals.py", title="Conditionals")
functions_page = st.Page("pages/08_functions.py", title="Functions")
loops_page = st.Page("pages/09_loops.py", title="Loops")
lists_page = st.Page("pages/10_lists.py", title="Lists")

# Simple grouped navigation
pg = st.navigation({
    "Getting Started": [home_page, setup_page],
    "Fundamentals": [variables_data_types_page, basic_output_page, basic_math_page, user_input_page],
    "Problem-Solving & Design": [planning_design_page],
    "Control Flow": [conditionals_page, functions_page, loops_page],
    "Data Structures": [lists_page],
})

pg.run()