import streamlit as st

st.title("Lists")
st.markdown("---")

st.header("Introduction")
st.markdown("""
            So far, variables have been used to store a single value, whether that's one number or one string of text. However, there are times that you want to store multiple values in a single variable. This is where lists come in! There are numerous other data types for storing multiple values, but lists are extremely common and generally are always taught as the first multi-value data type.
            """)

st.markdown("---")
st.header("Syntax")

st.markdown("""
            The syntax for creating a list is:

            ```python
            list_name = [value1, value2, value3, ...]
            ```

            where `list_name` is the name of the list and `value1`, `value2`, `value3`, etc. are the values in the list. 
            """)

st.error("""
            The important detail is that these values, if any exist, are enclosed in *square* brackets. It is critical you use square brackets as curly brackets and tuples are used for much different data structures (dictionaries and tuples respectively).
            """)

st.markdown("""
            Another note is that I said "these values, *if they exist*". A list can store multiple, one, or zero values:

            ```python
            empty_list = []
            single_value_list = [1]
            multiple_values_list = [1, 2, 3]
            ```

            Lists can be edited to have more or less values, so often they are created to be empty and then filled with values later.
            """)


st.markdown("---")
st.caption("© 2025-2026 Anthony Ha-Anh Pham | Licensed under [GNU GPL 3.0](https://www.gnu.org/licenses/gpl-3.0.html) | View source code on [GitHub](https://github.com/RicePandaaaa/TonyIntroToPython)")