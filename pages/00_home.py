import streamlit as st

st.title("Home")

# Tell users what the layout is
st.markdown("""
            Welcome to this Intro to Python notes collection! It was designed as a quick reference for the basics of Python. Each page has a different set of topics and contains examples and questions to test your understanding. **This is a work in progress, so expect to see updates and changes in the near future!**
            """)

st.markdown("---")

st.header("Teaching Philosophy")
st.markdown("""
            My teaching methodology revolves in-depth explanation with quizzes along the way to help reinforce the material and ties to real-world applications so you can see the practicality of the material. To me, the most difficult part of learning how to code is realizing how to employ these concepts when you're actually trying to solve a problem or create something. I hope this engineering-esque approach is a fun blend of learning and satisfaction of making something!

            Within each chapter is: a summary of the chapter, followed by the actual content. This content consists of the material itself, examples, quizzes, figures, and videos. There are also mini projects to help you practice the material and familiarize yourself with key practices and patterns.
            """)
st.markdown("---")

# Course Outline
st.header("Course Outline")

# Getting Started
st.subheader("Getting Started")
st.markdown("""
**Module 0: Home**  
Welcome and course navigation

**Module 1: Setup**  
Install Python, configure your PATH, and choose an IDE (repl.it, VSCode, or PyCharm)
""")

# Fundamentals
st.subheader("Fundamentals")
st.markdown("""
**Module 2: Variables and Data Types**  
 - Numeber data types: `int` and `float`
 - String data type: `str`
 - Variable assignment
 - Naming conventions
 - Typecasting

**Module 3: Basic Output**  
 - Printing to the console
 - Printing multiple values
 - Adjusting `print()` behavior
 - f-strings
 - Formatting the f-string insertions

**Module 4: Basic Math Operations**  
 - Overview
 - Using math operations
 - Rules regarding math with certain data types

**Module 5: User Input**  
 - Using `input()`
 - Typecasting
""")

# Problem-Solving
st.subheader("Problem-Solving & Design")
st.markdown("""
**Module 6: Planning and Design**  
 - Input, Processing, and Output
""")

# Control Flow
st.subheader("Control Flow")
st.markdown("""
**Module 7: Conditionals**  
 - Boolean data type
 - `if` keyword
 - Relational operators
 - `and` and `or` keywords
 - `elif` and `else` keywords
 - Nested conditionals

**Module 8: Functions**  
 - Function structure
 - Parameters and return values
 - Calling functions
 - Scope
 - Return statements
 - Pass by reference, pass by value

**Module 9: Loops**  
 - `for` loops
 - `range()` function
 - `while` loops
""")

# Functions
st.subheader("Data Structures")
st.markdown("""
**Module 10: Lists**
""")


st.markdown("---")

st.header("About the Author")
st.markdown("""
            Howdy, my name is Anthony Pham, and I am currently pursuing a Master's of Science in Engineering Technology at Texas A&M! I started teaching myself Python with the help and encouragement of my dad when I was 10 years old, and I have been coding as a hobby ever since! I also love tutoring my friends, and I am blessed to have the privilege to help teach Python to freshmen engineering students at my university as a peer teacher for three years during my undergrad!

            My love of Python started with a book called "Hello World!: Computer Programming for Kids and Other Beginners, 2nd Edition" by Warren and Carter Sande. It is my belief that with the right starting point, anyone can learn how to code and enjoy it too! I have made this mini-textbook as a free way for students and anyone else curious about Python to learn the basics of Python in an interactive way. There are other resources out there for sure, but I just wanted to add in my own twist to the mix, using my personal experience from self-teaching and teaching others.
            
            Within this mini-textbook, I have included notes, questions, and code snippets to play with! Soon, I plan to add labs (mini projects), projects, and videos as well! If you have any feedback, please feel free to contact me at [anthony.ha.pham@gmail.com](mailto:anthony.ha.pham@gmail.com).
            """)

st.markdown("---")
st.caption("© 2025 Anthony Ha-Anh Pham | Licensed under [GNU GPL 3.0](https://www.gnu.org/licenses/gpl-3.0.html) | View source code on [GitHub](https://github.com/RicePandaaaa/TonyIntroToPython)")