import streamlit as st

st.title("8: Functions")
st.markdown("---")

st.header("8.1: Introduction")
st.markdown("""
            Functions are a way to group re-usable code together. It's kinda of like a template of code that you can use over and over again. They're also core to a lot of programming ideaologies like object-oriented programming and functional programming. Also, a lot of other languages just naturally use functions (or methods), so learning about functions will also help you learn other langauges.
            """)

st.markdown("---")

st.header("8.2: Function Structure")
st.markdown("""
            To define a function, you use the `def` keyword. Then, you give the function a name, and then you put the code you want to run inside the function in a code block.

            ```python
            def howdy():
                print("Howdy!")
            ```

            Now this isn't particularly useful, but it's a function! Note a very important detail: the addition of the parentheses right after the function name. This is super important and actually mandatory for functions. I'll discuss what these do later, but for now, just know that they need to be there for a proper function definition. The structure of a function is split into two parts: the function definition and the function body. The first line with the `def` keyword is the function definition. The rest of the code block is the function body. The name of the function is essentially a variable name, so variable name rules still apply (e.g. can't overlap with a pre-existing variable name, can't share the same name as an pre-existing keyword). The function body just needs to be indented and be valid Python code.
            """)

# Quiz about function structure
st.subheader("Quiz: Function Structure")
st.markdown("""
            **Q1:** What keyword is used to define a function?
            """)
answer_function_definition_keyword = st.radio("Question 1: Which keyword defines a function in Python?", ["recipe", "def", "define", "make"], key="function_structure_1", index=None, label_visibility="collapsed")
if answer_function_definition_keyword == "def":
    st.success("Correct! The `def` keyword is used to define a function.")
elif answer_function_definition_keyword is not None:
    st.error("Incorrect. The `def` keyword is used to define a function.")

st.markdown("""
            **Q2:** No matter what, what must come after the function name?
            """)
answer_function_syntax_after_name = st.radio("Question 2: What punctuation must follow a function name?", ["brackets", "curly braces", "square brackets", "parentheses"], key="function_structure_2", index=None, label_visibility="collapsed")
if answer_function_syntax_after_name == "parentheses":
    st.success("Correct! A pair of parentheses are used to define the parameters of the function.")
elif answer_function_syntax_after_name is not None:
    st.error("Incorrect. A pair of parentheses are used to define the parameters of the function.")

st.markdown("---")

# Talk more about the definition, specifically parameters
st.header("8.3: Parameters")
st.markdown("""
            Consider a function to be like a recipe. It has a list of ingredients and a list of steps to follow. It can be said that the list of steps is the function body. But what about the ingredients? Before I answer that, let's discuss a bit more about what the ingredients really represent. For a recipe, the ingredients are what the chef deems necessary to make the dish. However, what you use for those ingredients is up to you, as long as they're the same type. If you're asking to get chicken eggs, the branding of the chicken eggs doesn't really matter since in the end, you're still using chicken eggs. So, the ingredients define the types of "inputs" that you need in order to follow the instructions correctly. If you miss an ingredient or get the wrong type of ingredient, the recipe won't work and might actually be dangerous.

            For a function, the code equivalent of ingredients is what we call the parameters. Parameters dictate what values the function needs in order to work correctly. For example, if you're asked to make a function that adds three numbers together, you need three parameters: one for each number. But what is used as a parameter? Well, it's just variables! Take the following example:

            ```python
            def add_three_numbers(a, b, c):
                print(a + b + c)
            ```

            For this function, the parameters are `a`, `b`, and `c`. These parameters are actually variables that belong to the function that hold the values you will later pass into the function (i.e. the ingredients you bought for the recipe). Just as the recipe trusts that you got the right ingredients, Python also trusts that you'll give it proper values for it to add. You could give the function three strings (although that would be weird considering the function name) or three floats or three ints or a mix of floats and ints.

            Note that these parameters are private to the function. This means that you cannot access them outside of the function, and they will not interfere with variables outside of the function, *even* if they have the same name. This will be discussed in more detail later.
            """)

# Quiz about parameters
st.subheader("Quiz: Parameters")
st.markdown("""
            **Q1:** Where are the parameters defined?
            """)
answer_parameter_definition_location = st.radio("Question 1: Where are function parameters defined?", ["in the function body", "outside the function", "inside the parentheses"], key="parameters_1", index=None, label_visibility="collapsed")
if answer_parameter_definition_location == "inside the parentheses":
    st.success("Correct! The parameters are defined inside the parentheses after the function name.")
elif answer_parameter_definition_location is not None:
    st.error("Incorrect. The parameters are defined inside the parentheses after the function name.")

st.markdown("---")

# Talk about calling functions
st.header("8.4: Calling Functions")
st.markdown("""
            To call a function, you just need to use the function name with the parentheses. Using the `add_three_numbers` function from the previous section, you could call it like this:

            ```python
            add_three_numbers(1, 2, 3)
            ```

            You can see three distinct differences between calling a function and defining a function:
            - The `def` keyword is not used
            - The parameters are replaced with actual values
            - The function body is entirely missing

            Without the `def` keyword, Python understands that you are not making a function but rather asking Python to execute the function with the given values. Note that the technical term for a value you give to a function is called argument. Admittedly, I do mix up the two terms sometimes, but usually with context, you'll understand what is meant even if someone mixes up the two terms.

            When this function is executed, Python will first assign each value to its corresponding parameter (variable) in the function. This assignment is done in order: the first argument is assigned to the first parameter, the second argument is assigned to the second parameter, and so on. In this case, `1` is assigned to `a`, `2` is assigned to `b`, and `3` is assigned to `c`. Then, the function body is executed, which in this case is printing the sum of the values of `a`, `b`, and `c`. This simplifies to `print(1 + 2 + 3)`, which outputs `6`.

            Note that the number of arguments must match the number of parameters. There are special cases where you don't need to match, but for now, until you learn those special cases, you must match the number of arguments to the number of parameters.
            """)

# Quiz about calling functions
st.subheader("Quiz: Calling Functions")
st.markdown("""
            **Q1:** What is the output of the following code?
            ```python
            def multiply_three_numbers(a, b, c):
                print(a * b * c)

            multiply_three_numbers(2, 3, 5)
            ```
            """)
answer_function_call_output = st.text_input("Question 1: Enter the output when calling multiply_three_numbers(2, 3, 5) (hit Enter to submit)", key="calling_functions_1", label_visibility="collapsed")
if answer_function_call_output == "30":
    st.success("Correct! The function is called with the arguments `2`, `3`, and `5`. These are assigned to the parameters `a`, `b`, and `c` in the function. Multiplying them together gives `30`.")
elif len(answer_function_call_output) > 0:
    st.error("Incorrect! The function is called with the arguments `2`, `3`, and `5`. These are assigned to the parameters `a`, `b`, and `c` in the function. Multiplying them together gives `30`.")

st.markdown("""
            **Q2:** What is the output of the following code?
            ```python
            def multiply_three_numbers(a, b, c):
                print(a * b * c)
            multiply_three_numbers(2, 3, 5, 7)
            ```
            """)
answer_function_too_many_arguments = st.radio("Question 2: What happens when calling the function with 4 arguments instead of 3?", ["30", "210", "105", "error"], key="calling_functions_2", index=None, label_visibility="collapsed")
if answer_function_too_many_arguments == "error":
    st.success("Correct! The function is called with the arguments `2`, `3`, and `5`, and `7`. However, the function only has three parameters. This will cause an error due to there being more arguments than parameters.")
elif answer_function_too_many_arguments is not None:
    st.error("Incorrect! The function is called with the arguments `2`, `3`, and `5`, and `7`. However, the function only has three parameters. This will cause an error due to there being more arguments than parameters.")

st.markdown("---")

# Scope
st.header("8.5: Scope")
st.markdown("""
            So far, before functions were introduced, variables you created could essentially be accessible everywhere. We call these variables global variables.

            However, with the introduction of functions, variables can now only be accessible from a limited scope. We call these variables local variables. The good and bad thing about local variables is that they are only accessible from the function they are defined in (for this context). This is good because it prevents accidental modification of variables, allowing you to freely use values without worrying about certain operations that permanently alter the value. However, it can be bad because you may need to access those values later, and it gets tricky on how to do that. In the end, this is a net positive, especially as there are ways to deal with the lack of accessibility in other parts of the function.

            As an example, let's redefine the `add_three_numbers` function to return the sum of the doubled value of each parameter:

            ```python
            def add_three_numbers(a, b, c):
                a = a * 2
                b = b * 2
                c = c * 2

                print(a, b, c)
            
            a = 1
            b = 2
            c = 3

            add_three_numbers(a, b, c)
            print(a, b, c)
            ```

            You would get the following output if you ran the code:

            ```
            2 4 6
            1 2 3
            ```

            Note that the top row is the output of the function call, and the bottom row is the output of the print statements outside of the function. The function's `a`, `b`, and `c` are entirely different variables from the global `a`, `b`, and `c`, despite having the same name. Imagine it this way: Python has a ton of storage space for the main program. For the three variables outside of the function, Python created three boxes and named them `a`, `b`, and `c`. However, for the function, Python set aside three more boxes and named them `a`, `b`, and `c` and set them aside along with the function. It is a coincidence that the names are the same, but the variables themselves are not connected. Therefore, whatever the function does to its three boxes has no effect on the outside three boxes.

            A more obvious example is if I switched the order of the arguments:

            ```python
            add_three_numbers(c, b, a)
            ```

            This will output `6 4 2`. This is what happened under the hood:
            - global `c` is the first argument and its value is assigned to the first parameter, which is the local `a`. The function's `a` now stores the value `3` from the global `c`.
            - global `b` is the second argument and its value is assigned to the second parameter, which is the local `b`. The function's `b` now stores the value `2` from the global `b`.
            - global `a` is the third argument and its value is assigned to the third parameter, which is the local `c`. The function's `c` now stores the value `1` from the global `a`.

            This is a rather tricky concept, but once you understand that these variables do not overlap with one another, the confusion that can arise from having similar naming conventions will not be as daunting. Now there are some very important exceptions to this rule, but they will be covered in future sections. Do not worry about them for now. As long as you are just passing in the basic data types (e.g. `str`, `int`, `float`, `bool`), you can safely assume that changing the local parameter will not change its corresponding global argument.
            """)
# Quiz about scope
st.subheader("Quiz: Scope")
# Quick question about local scope
st.markdown("""
            **Q1:** Can local variables be accessed outside of the function they are defined in?
            """)
answer_local_variable_scope = st.radio("Question 1: Can local variables be accessed outside their function?", ["yes", "no"], key="scope_1", index=None, label_visibility="collapsed")
if answer_local_variable_scope == "no":
    st.success("Correct! Local variables are only accessible within the function they are defined in.")
elif answer_local_variable_scope is not None:
    st.error("Incorrect. Local variables are only accessible within the function they are defined in.")

# Question about global vs local
st.markdown("""
            **Q2:** Are global variables changed when they are used as arguments (assume values are of basic data types)?
            """)
answer_global_variable_modification = st.radio("Question 2: Do global variables change when used as function arguments?", ["yes", "no"], key="scope_2", index=None, label_visibility="collapsed")
if answer_global_variable_modification == "no":
    st.success("Correct! Global variables are not changed when they are used as arguments.")
elif answer_global_variable_modification is not None:
    st.error("Incorrect. Global variables are not changed when they are used as arguments. They are stored in local variables that store the same value, but they do not influence the arguments they took values from")

st.markdown("---")

# Talk about return statements
st.header("8.6: Return Statements")
st.markdown("""
            Ok, well with scope, one major issue arises: what if I want to still do something with a value that only exists within the function? If I can't access it outside of the function, how can I use it? I can just return it. Literally. The `return` keyword allows the function call to *store* a value that can be assigned to a variable for future usage. Let's rewrite the original `add_three_numbers` function to return the sum of the three numbers:

            ```python
            def add_three_numbers(a, b, c):
                return a + b + c
            ```

            `return` is the keyword here and note that there are no parentheses as there is with `print()`. That's just how the syntax works. Now, let's call the function and store the result in a variable:

            ```python
            result = add_three_numbers(1, 2, 3)
            print(result)
            ```

            `result` now stores the resulting value from the `add_three_numbers` function call. The analogy I use is imagine Python is a chef. You ask it to make you a cake. It will hold onto the cake until you ask for it. The way you ask for it is to assign the function call to a variable (or just use it in an expression). If you don't use or store the value, Python will just hold onto it until Python is forced to drop the cake to execute the next line of code. In code, this means you want to avoid doing the following:

            ```python
            # Where is the returned value going to be stored or used??
            add_three_numbers(1, 2, 3)
            ```
            """)

# Quiz about return statements
st.subheader("Quiz: Return Statements")

# Question about assigning return values to variables
st.markdown("""
            **Q1:** What is the output of the following code?
            ```python
            def add_three_numbers(a, b, c):
                return a + b + c

            add_three_numbers(1, 2, 3)
            ```
            """)
answer_return_without_assignment = st.radio("Question 1: What is output when function returns but value isn't stored?", ["6", "12", "Nothing", "Error"], key="return_statements_1", index=None, label_visibility="collapsed")
if answer_return_without_assignment == "Nothing":
    st.success("Correct! The function is called, however, there is no variable to store the returned value, so it is lost.")
elif answer_return_without_assignment is not None:
    st.error("Incorrect. The function is called, however, there is no variable to store the returned value, so it is lost. Thus, there is no output.")

# Question about using return syntax
st.markdown("""
            **Q2:** What is the correct syntax for a `return` statement?
            """)
answer_return_statement_syntax = st.radio("Question 2: What is the correct syntax for returning a value?", ["return {value}", "return({value})", "return[{value}]"], key="return_statements_2", index=None, label_visibility="collapsed")
if answer_return_statement_syntax == "return {value}":
    st.success("Correct! The value to be returned is just separated from the `return` keyword by a space.")
elif answer_return_statement_syntax is not None:
    st.error("Incorrect. The value to be returned is just separated from the `return` keyword by a space.")

st.markdown("---")

# Pass by reference, pass by value
st.header("Pass by Reference, Pass by Value")
st.markdown("""
            So far, we have been using basic data types as arguments. However, what happens if you use a compound data type (e.g. `list`, `dict`, `tuple`) as an argument? Let's find out. If you can, run the following code and see what you get:

            ```python
            def add_one_to_list(l):
                l.append(1)
            
            my_list = [1, 2, 3]
            add_one_to_list(my_list)
            print(my_list)
            ```

            You should get the following output:

            ```
            [1, 2, 3, 1]
            ```
            
            So, why is this the output? Earlier, we saw that the three global variables were not changed, but in this case, the global variable *did* change. The distinction here is lies in the difference of two concepts: pass by reference and pass by value.

            Imagine that you are in a classroom, and your friend next to you asks for both a pencil and a quiz paper. You go to your desk, grab the pencil, and give it to your friend. You then go to the teacher's desk, grab a copy of the quiz paper, and give it to  your friend.

            In the above scenario, sharing the pencil is an example of pass by reference. You are giving your friend the actual pencil, so any changes to the pencil will be reflected on the actual pencil. However, when you give your friend the quiz paper, you are giving a copy of the quiz paper, not your own actual quiz paper. Functionally, the quiz papers are identical, but what your friend does to their own quiz paper will not affect your quiz paper.

            Now back to Python, passing in integers or floats or strings are all examples of pass by value. A copy of the value is made and passed into the function, so any changes to the value **will not affect** the original value. Although the two values are identical in value, they are not literally the same value. For example, having `a = 1` and `b = 1` does not mean that `a` and `b` are the same variable. They are two different variables with the same value.

            With lists, you are passing in a reference to the list, which means the function is handed the original list, not a copy of the list. The exact definition of a reference is not necessary to understand at this point, but roughly speaking, the reference can be thought of as a piece of paper with the address of the list written on it. The function knows exactly where to find the original list so it can make changes to it. Because of this, the function has access to the original list, not an copy of the list. Thus, the function can and will only modify the original list (as there is no copy of the list to modify).
            """)


st.caption("© 2026 Anthony Ha-Anh Pham | Licensed under [GNU GPL 3.0](https://www.gnu.org/licenses/gpl-3.0.html) | View source code on [GitHub](https://github.com/RicePandaaaa/TonyIntroToPython)")