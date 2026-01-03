import streamlit as st

st.title("1: Setup")

st.write("---")

# Python Installation
st.header("1.1: Python Installation")

st.write("""
        Python is a popular programming language that is easy to learn and use. It is a general-purpose language that can be used for a wide range of applications.

        Other people have very detailed and verified guides for installing Python. I personally recommend Real Python's guide for installing Python [here](https://realpython.com/installing-python/).
        """)

st.subheader("1.1.1: By Operating System")
st.write("""
        - [Windows](https://realpython.com/installing-python/#windows-how-to-install-python-using-the-official-installer)
        - [Mac](https://realpython.com/installing-python/#macos-how-to-install-python-using-the-official-installer)
        - [Linux](https://realpython.com/installing-python/#linux-how-to-check-or-get-python)
        """)
st.write("---")

# IDE Setup
st.header("1.2: IDE Setup")

st.write("""
        An IDE (Integrated Development Environment) is a software application that allows you to more easily write and test your code. For Python, there are several options to choose from:
        """)
        

st.subheader("1.2.1: IDE Options")
st.write("""
        - [VSCode](https://code.visualstudio.com/): Accessible online and offline, great as a flexible code editor, not as powerful as PyCharm
          - Offline IDE (just install to your computer)
          - Lightweight and fast
          - Customizable with extensions
          - Works for various languages, not just Python
        - [PyCharm](https://www.jetbrains.com/pycharm/): Extremely powerful for Python, but all the Python features can be a bit overwhelming
          - Offline IDE (just install to your computer)
          - Powerful and feature-rich
          - Made specifically for Python
          - Community (free) version is slightly limited but still very powerful
        - [Spyder](https://www.spyder-ide.org/): Made for data science, but can be used for other purposes
          - Offline IDE (just install to your computer)
          - Made for data science
          - Comes with a lot of useful features for data science

        My personal recommendation is VSCode. It is a very powerful code editor that is free and open source. The installation process is pretty simple, and there's a lot of personalization options with extensions. However, feel free to try all sorts of IDEs (or look at videos of people using them on YouTube) and see which one you like best.
        As long as you can make a `.py` file and run it with Python, you are good to go.
        """)

st.subheader("1.2.2: Installation Guides")
st.write("""
        The installation guides for the three mentioned IDEs are below:
        - [Install repl.it](https://repl.it/languages/python3)
        - [Install VSCode](https://code.visualstudio.com/docs/setup/setup-overview)
        - [Install PyCharm](https://www.jetbrains.com/pycharm/download/#section=windows)
         
        If you are using your own IDE, it should have its own installation guide online somewhere.
        """)

st.markdown("---")
st.caption("© 2026 Anthony Ha-Anh Pham | Licensed under [GNU GPL 3.0](https://www.gnu.org/licenses/gpl-3.0.html) | View source code on [GitHub](https://github.com/RicePandaaaa/TonyIntroToPython)")
