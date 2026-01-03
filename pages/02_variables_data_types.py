import streamlit as st

# Page configuration
st.set_page_config(page_title="Variables & Data Types", layout="wide")
st.title("2: Variables and Data Types")

st.info("""
        **Summary of the chapter:**
        - A variable is what we use to store information in a program.
        - Three primitive data types: `int` (integer), `float` (floating point number), and `str` (string).
        - `int` is used to store integers, while `float` is used to store floating point numbers (decimal numbers).
        - `str` is used to store strings (text).
        - Variables can be assigned a value using the assignment operator (`=`).
        - Variable names must follow certain rules to be valid.
        - We can convert between data types using the `int()`, `float()`, and `str()` functions.
        """)

st.markdown("---")

# Introduction
st.header("2.1: Introduction")
st.markdown("""
            A variable is what we use to store information in a program. If the information can be represented as some sort of tangible value or object (e.g. a number or some text), then we can store in a variable. For Python to understand the information being stored, it has specific data types that it can work with. The core three are `int`, `float`, and `str`.

            The first few sections will cover over the primitive (basic) data types for storing numbers and characters and how to store this data (with variables). The core of any project is how to store and manipulate data, and this first chapter is the foundation of having Python remember and use data! Also, as you use external datasets or files, you will need to know how to store and manipulate data in a way that Python can understand, and this is the foundation of that.
            """)

st.markdown("---")

# Number data types
st.header("2.2: Number data types")
st.markdown("""
            `int` and `float` are used to store numbers. `int` is used to store **int**eger values, while `float` is used to store **float**ing point values (decimal numbers). An example of an `int` is `1`, while an example of a `float` is `1.5`. Note that as long as the number has a decimal point, it will be stored as a `float`, even if the number itself could be rewritten as an `int` (e.g. `1.0` is a `float` even though 1 does not inherently have a fractional part).
            """)

# Create a table of examples of ints and floats
st.markdown("""
            Here are some examples of `int` and `float` values:
            """)
st.table([
    {"float": "1.5", "int": "1"},
    {"float": "2.0", "int": "2"},
    {"float": "-2.12345", "int": "-212345"}
])

# Ask the student whether a value is an int or a float
st.subheader("Quiz: `int` or `float`?")
st.markdown("""
            **Q1: Is 0.0 an `int` or a `float`?**
            """)
answer_int_or_float_zero = st.radio("Question 1: Is 0.0 an int or a float?", ["int", "float"], key="num_q1", index=None, label_visibility="collapsed")
if answer_int_or_float_zero == "float":
    st.success("Correct! Even though 0.0 is equal to 0, it is still a `float` because it has a decimal point.")
elif answer_int_or_float_zero == "int":
    st.error("Incorrect. Even though 0.0 is equal to 0, it is still a `float` because it has a decimal point.")

st.markdown("""
            **Q2: Is 123 an `int` or a `float`?**
            """)
answer_int_or_float_123 = st.radio("Question 2: Is 123 an int or a float?", ["int", "float"], key="num_q2", index=None, label_visibility="collapsed")
if answer_int_or_float_123 == "int":
    st.success("Correct! 123 is an `int` because it does not have a decimal point.")
elif answer_int_or_float_123 == "float":
    st.error("Incorrect. 123 is an `int` because it does not have a decimal point.")

st.markdown("---")

# String data type
st.header("2.3: String data type")
st.markdown("""
            `str` is used to store **string** values. A string is a sequence of characters. An example of a `str` is `"Hello, world!"`. Notice the use of quotes to indicate that the value is a string. These quotes are not part of the string itself, but are used to indicate that the value is a string. Without these quotes, Python would think you are typing some code instead. Also notice that the quotes can be single or double quotes, but they must be consistent (i.e. the string must be enclosed in the same type of quotes).
            """)
st.markdown("""
            **Note 1:** A string can be empty, which is represented by two quotes with nothing in between. For example, `""` is a valid `str` value.

            **Note 2:** A string cannot *contain* the same quote character that is used to enclose the string. For example, `"Hello, world!"` is a valid `str` because the string is enclosed in double quotes, but `"Hello, world!"` is not a valid `str` because the string is enclosed in double quotes and contains a double quote.
            """)

# Create a table of examples of strings
st.markdown("""
            Here are some examples of valid and invalid `str` values:
            """)
st.table([
    {"Valid": "\"Hello, world!\"", "Invalid": "\'Hello, world!\""},
    {"Valid": "\'12345\'", "Invalid": "\"12345"},
    {"Valid": "\"Tony\"", "Invalid": "Tony"},
])
st.markdown("""
            The left side of the table all have some sort of text (letters, numbers, etc.) enclosed by a pair of double or single quotes. The right side of the table shows incorrect syntax with either mixmatched types of quotes or just missing quotes.
            """)

# Ask the student whether a value is a valid string or not
st.subheader("Quiz: Is the string valid?")
st.markdown("""
            **Q1: Is `'Hello, world!'` a valid `str`?**
            """)
answer_string_hello_world_validity = st.radio("Question 1: Is the string 'Hello, world!' with single quotes valid?", ["Yes", "No"], key="str_q1", index=None, label_visibility="collapsed")
if answer_string_hello_world_validity == "Yes":
    st.success("Correct! `'Hello, world!'` is a valid `str` because it is enclosed in single quotes.")
elif answer_string_hello_world_validity == "No":
    st.error("Incorrect. `'Hello, world!'` is a valid `str` because it is enclosed by the same type of quotes! Single or double quotes are both valid.")

st.markdown("""
            **Q2: Is `'Howdy''` a valid `str`?**
            """)
answer_string_howdy_validity = st.radio("Question 2: Is the string 'Howdy'' valid (note the extra quote)?", ["Yes", "No"], key="str_q2", index=None, label_visibility="collapsed")
if answer_string_howdy_validity == "No":
    st.success("Correct! `'Howdy''` is invalid because it is both enclosed in single quotes and contains a single quote.")
elif answer_string_howdy_validity == "Yes":
    st.error("Incorrect. `'Howdy''` is invalid because it is both enclosed in single quotes and contains a single quote. To use the single quote, use double quotes instead to enclose the string (e.g. `\"can't\")`")

st.markdown("""
            **Q3: Is `'\"cat'` a valid `str`?**
            """)
answer_string_quote_cat_validity = st.radio("Question 3: Is the string '\"cat' valid (starts with single quote, contains double quote)?", ["Yes", "No"], key="str_q3", index=None, label_visibility="collapsed")
if answer_string_quote_cat_validity == "Yes":
    st.success("Correct! `'\"cat'` is a valid `str` because it is enclosed in double quotes and contains a single quote.")
elif answer_string_quote_cat_validity == "No":
    st.error("Incorrect. `'\"cat'` is a valid `str` because it is enclosed in double quotes and contains a single quote.")

st.markdown("""
            **Q4: Is `'\"` a valid `str`?**
            """)
answer_string_mismatched_quotes_validity = st.radio("Question 4: Is the string '\" valid (mismatched quote types)?", ["Yes", "No"], key="str_q4", index=None, label_visibility="collapsed")
if answer_string_mismatched_quotes_validity == "No":
    st.success("Correct! `'\"` is not a valid string because the quotes are different. A string can be empty, but it cannot be enclosed in different types of quotes.")
elif answer_string_mismatched_quotes_validity == "Yes":
    st.error("Incorrect. `'\"` is not a valid string because the quotes are different. A string can be empty, but it cannot be enclosed in different types of quotes.")

st.header("Confusing Strings")
st.error("""
            Often strings can look empty but are actually not. The most common mistake is to consider whitespaces as just blank space. However, remember that even a whitespace is still considered to be a character. This means that `" "` is a valid `str` value, and is not empty. A way to think about the whitespace is that it takes up space, and thus is a character.

            The other confusion comes with numbers. For example, `"123"` is a `str` value, not an `int` or `float` value. Although the contents of the string is what we would consider a number, Python sees the quotes and treats the contents as characters. It just happens that those characters form a number to us. Now we can leverage this to convert strings into actual numbers, which we will cover in the "Typecasting" section later on.
            """)

st.markdown("---")

# Variable assignment
st.header("2.4: Variable Assignment")
st.markdown("""
            To store these values in a variable, the variable needs to be created and assigned. The syntax for this is:
            ```python
            variable_name = value
            ```

            If `variable_name` already exists, it will be overwritten with the new value. Otherwise, a new variable will be created with that value. Notice that the variable name is on the left side of the assignment operator (`=`) and the value is on the right side. This is *always* the case, and is a key concept to remember when programming.

            Note that if a variable is written on the right side, then it is assumed that we want to assign the *value* of that variable to the variable on the left. For example, if we have `x = 1` and `y = x`, then `y` will be assigned the value `1`.
            """)

# Quiz: Assign a value to a variable
st.subheader("Quiz: Value Assignment")
st.markdown("""
            **Q1: Assign the value `123` to the variable `x`**
            """)
answer_assign_123_to_x = st.radio("Question 1: Choose the correct syntax to assign 123 to variable x", ["x = 123", "123 = x", "= 123 x", "x 123 ="], key="var_q1", index=None, label_visibility="collapsed")
if answer_assign_123_to_x == "x = 123":
    st.success("Correct! `x = 123` is the correct syntax to assign the value `123` to the variable `x`.")
elif answer_assign_123_to_x == "123 = x":
    st.error("Incorrect. The variable needs to be on the left side of the assignment operator (`=`) and the value needs to be on the right side.")
elif (answer_assign_123_to_x == "= 123 x") or (answer_assign_123_to_x == "x 123 ="):
    st.error("Incorrect. The assignment operator needs to be in the middle, with the name of the variable on the left and the value on the right.")

st.markdown("""
            **Q2: Suppose we have the following code:**
            ```python
            a = 1
            b = 4
            a = 7
            b = 8
            a = b
            ```

            **What is the final value of `a`?**
            """)
answer_variable_reassignment_final_value = st.radio("Question 2: After multiple reassignments, what is the final value of variable a?", ["1", "4", "7", "8"], key="var_reassign_q1", index=None, label_visibility="collapsed")
if answer_variable_reassignment_final_value == "8":
    st.success("Correct! The final assignment of `a` was the value of `b`. `b`'s final value is `8`, so `a` is assigned the value `8`.")
elif answer_variable_reassignment_final_value == "4":
    st.error("Incorrect. `b` did have the value `4` initially, but it was overwritten by the value `8` right before `a` took on the value of `b`. This means that when `a = b` is executed, `b` was already changed to `8`, and thus `a` is assigned the value `8`.")
elif answer_variable_reassignment_final_value == "7":
    st.error("Incorrect. `a` was assigned a different value two lines after with `a = b`. This means that `a` is now assigned the value `8` since `b` is 8 at the time of that assignment.")
elif answer_variable_reassignment_final_value == "1":
    st.error("Incorrect. `a` gets assigned two more different values after the initial assignment of `1`. With the final assignment being `a = b`, `a` is assigned the value stored in `b`, which is `8`.")
st.markdown("---")

# Naming conventions
st.header("2.5: Naming conventions")
st.markdown("""
            When naming variables, there are some rules to follow to avoid errors and confusion with either Python or other programmers. Some "rules" are stylistic in nature: they just follow what other programmers done have for a while, and it helps make your code more readable. Other rules however are extremely strict and will cause errors or very unexpected behaviors if not followed.
            """)

# Hard rules
st.subheader("2.5.1: Hard rules")
st.markdown("""
            As previously said, some rules, if ignored, will cause errors or very unexpected behaviors. These are the hard rules that you must follow:

            - Variable names can **only** contain letters, numbers, and underscores (`_`)
            - Variable names cannot start with a number
            - Variable names cannot be the same as a Python keyword
            - Variable names cannot be the same as a built-in function name

            That above list is not *entirely* exhaustive, but it works well enough. If you are unsure about whether a variable name is valid, you can always check the [Python documentation](https://docs.python.org/3/reference/lexical_analysis.html#identifiers).
            """)

# Soft rules
st.subheader("2.5.2: Soft rules")
st.markdown("""
            These rules are more like guidelines. They are not enforced by Python, but it is a good idea to follow them to make your code more readable.

            - Variable names should be in lowercase
            - Variable names should be short and concise
            - Variable names for constant values should be in all caps
            - Be consistent in how spacing is used:
              - Either use underscores (e.g. `my_variable`)
              - Or use camel case (e.g. `myVariable`)
            
            There are other rules, but these are the most obvious ones.
            """)

# Quiz on valid variable names
st.subheader("Quiz: Valid variable names")
st.markdown("""
            **Q1: Choose the valid variable name:**
            """)
answer_valid_variable_name_choice = st.radio("Question 1: Which of these is a valid Python variable name?", ["123", "my_variable", "my.Variable", "my-variable", "my variable"], key="var_name_q1", index=None, label_visibility="collapsed")
if answer_valid_variable_name_choice == "my_variable":
    st.success("Correct! `my_variable` is a valid variable name because it contains only letters, numbers, and underscores, and does not start with a number.")
elif answer_valid_variable_name_choice == "123":
    st.error("Incorrect. `123` is not a valid variable name because it starts with a number.")
elif answer_valid_variable_name_choice == "my.Variable":
    st.error("Incorrect. `my.Variable` is not a valid variable name because it contains a period. Remember, no punctuation is allowed other than underscores!")
elif answer_valid_variable_name_choice == "my-variable":
    st.error("Incorrect. `my-variable` is not a valid variable name because it contains a hyphen. Remember, no punctuation is allowed other than underscores!")
elif answer_valid_variable_name_choice == "my variable":
    st.error("Incorrect. `my variable` is not a valid variable name because it contains a space. Remember, no spaces are allowed in variable names!")

st.markdown("---")

# Casting to a different data type
st.header("2.6: Typecasting")
st.markdown("""
            We can also convert between data types using the `int()`, `float()`, and `str()` functions. This is particularly useful when we want to do something with a value that is only possible for certain data types. For example, we can use `int()` to conver a string into an integer, so we can do math.

            These three functions return an entirely new value, and do not modify the original value that they are called on. For example, if we have `x = '123'` and we call `int(x)`, then `x` will still be `'123'` and the function will return `123` (the integer value of the string `'123'`).

            The table below shows the possible conversions:
            """)

st.table(
    [
        {
            "Function": "`str()`",
            "Convertible Types": "`int`, `float`",
            "Example 1": "`str(1)` = `\"1\"`",
            "Example 2": "`str(1.0)` = `\"1.0\"`"
        },
        {
            "Function": "`int()`",
            "Convertible Types": "`float`, `str`",
            "Example 1": "`int(1.0)` = `1`",
            "Example 2": "`int(\"1\")` = `1`"
        },
        {   
            "Function": "`float()`",
            "Convertible Types": "`int`, `str`",
            "Example 1": "`float(1)` = `1.0`",
            "Example 2": "`float(\"1.0\")` = `1.0`"
        }
    ]
)

st.markdown("""
            When converting a string to a number, just think about whether the value looks like a number if you remove the quotes. For example, `\"123\"` without the quotes is `123`, which is an integer. This means you can convert to both an `int` and a `float`.

            When converting a `float` to an `int`, the decimal point and anything after it is removed. For example, `int(1.9999)` will return `1`. When converting any number to a string, just add quotes around the number. For example, `str(1.0)` will return `\"1.0\"`.
            """)

st.subheader("Most Common Mistake")
st.error("""
            We know that converting a `float` to an `int` will remove the decimal point and anything after it, but what happens if you try to convert a string that contains a decimal number to an `int`? An error occurs!
            """)
st.markdown("""

            When you convert a string to an `int`, you need to see if the value without the quotes is an integer. For example, `\"123.45\"` without the quotes is `123.45`, which is not an integer. This means that `int(\"123.45\")` will return an error. Do not make the assumption that `int()` will also truncate the decimal point for you. You would need to convert to a `float` first and then to an `int` to get the integer part of the number. Below shows the side by side comparison of the incorrect and correct way to do this conversion.

            ```python
            # Incorrect
            int(\"123.45\")

            # Correct
            int(float(\"123.45\"))
            ```
            """)

st.subheader("The not as common mistake")
st.error("""
            The other mistake people do is not assigning the new value to a variable. 
            
        """)
st.markdown("""
            When you convert the type, it stores the new value. However, you need to store it yourself in a variable if you want to use it later:

            ```python
            # Can't use this value later
            str(123)

            # Need to assign it to a variable
            x = str(123)
            ```

            With that code snippet, `x` will hold onto `\"123\"`, and we can use it later.
            """)

st.subheader("Quiz: Typecasting")
st.markdown("""
            **Q1: What is the final value of `y`?**
            ```python
            x = 123
            y = str(x)
            ```
            """)
answer_typecast_str_from_int = st.radio("Question 1: What is the value of y after converting 123 to a string?", ["123", "\"123\"", "123.0", "\"123.0\""], key="typecast_q1", index=None, label_visibility="collapsed")
if answer_typecast_str_from_int == "\"123\"":
    st.success("Correct! `str(123)` returns `\"123\"`.")
elif answer_typecast_str_from_int == "123":
    st.error("Incorrect. You are being asked for the value of `y`, not `x`.")
elif answer_typecast_str_from_int == "123.0":
    st.error("Incorrect. `str(123)` adds quotes around the number instead of adding the decimal point (which `float()` would do).")
elif answer_typecast_str_from_int == "\"123.0\"":
    st.error("Incorrect. `str(123)` only adds quotes around the number. The decimal point is only added by `float()` (and `float()` would not add the quotes).")

st.markdown("""
            **Q2: What is the final value of `z`?**
            ```python
            z = int(\"123.45\")
            ```
            """)
answer_typecast_int_from_decimal_string = st.radio("Question 2: What happens when converting string \"123.45\" to an integer?", ["123", "\"123.45\"", "Error","123.45"], key="typecast_q2", index=None, label_visibility="collapsed")
if answer_typecast_int_from_decimal_string == "Error":
    st.success("Correct! `int(\"123.45\")` returns an error because the string contains a decimal point. \"123.45\" without the quotes is `123.45`, which is not an integer.")
elif answer_typecast_int_from_decimal_string == "123":
    st.error("Incorrect. `int(\"123.45\")` returns an error because the string contains a decimal point. \"123.45\" without the quotes is `123.45`, which is not an integer.")
elif answer_typecast_int_from_decimal_string == "\"123.45\"":
    st.error("Incorrect. `int(\"123.45\")` returns an error because the string contains a decimal point. \"123.45\" without the quotes is `123.45`, which is not an integer.")
elif answer_typecast_int_from_decimal_string == "123.45":
    st.error("Incorrect. `int(\"123.45\")` returns an error because the string contains a decimal point. \"123.45\" without the quotes is `123.45`, which is not an integer.")

st.markdown("""
            **Q3: What is the final value of `abc`?**
            ```python
            abc = float(\"123.45\")
            ```
            """)
answer_typecast_float_from_string = st.radio("Question 3: What is the value of abc after converting string \"123.45\" to a float?", ["123", "123.45", "Error", "\"123.45\""], key="typecast_q3", index=None, label_visibility="collapsed")
if answer_typecast_float_from_string == "123.45":
    st.success("Correct! `float(\"123.45\")` returns `123.45`.")
elif answer_typecast_float_from_string == "123":
    st.error("Incorrect. The decimal point and the numbers afterward are kept when converting to a `float`. If you casted to `int` though, you would get `123`.")
elif answer_typecast_float_from_string == "Error":
    st.error("Incorrect. The value within the string is a valid number, so it can be converted to a `float`.")
elif answer_typecast_float_from_string == "\"123.45\"":
    st.error("Incorrect. `float()` will not remove the surrouding quotes.")

st.markdown("""
            **Q4: What is the final value of `weight`?**
            ```python
            weight = int(123.45)
            ```
            """)
answer_typecast_int_from_float = st.radio("Question 4: What is the value of weight after converting 123.45 to an integer?", ["123", "123.45", "Error", "\"123.45\""], key="typecast_q4", index=None, label_visibility="collapsed")
if answer_typecast_int_from_float == "123":
    st.success("Correct! `int(123.45)` returns `123`.")
elif answer_typecast_int_from_float == "123.45":
    st.error("Incorrect. Casting to an `int` will remove the decimal point and anything after it.")
elif answer_typecast_int_from_float == "Error":
    st.error("Incorrect. The value without the quotes is a valid integer, so it can be converted to an `int`.")
elif answer_typecast_int_from_float == "\"123.45\"":
    st.error("Incorrect. Casting to an `int` will remove the decimal point and the following digits. Additionally, `int()` does not add any quotes.")


st.markdown("---")
st.caption("© 2026 Anthony Ha-Anh Pham | Licensed under [GNU GPL 3.0](https://www.gnu.org/licenses/gpl-3.0.html) | View source code on [GitHub](https://github.com/RicePandaaaa/TonyIntroToPython)")
