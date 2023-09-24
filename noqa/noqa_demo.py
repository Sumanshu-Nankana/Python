"""
“Noqa” - is a special comment that can be added to your code to suppress specific  limiting or code analysis warnings or errors
that might be raised by tools like Flake8, pylint, mypy. It is useful when you have the legitimate reason to ignore a particular warning or error in your code.


It will suppress the warning in the IDE
We just need to add the comment # noqa at the end of the line (where we have the warning)

Examples -

Unused modules    # F401  (Flake8 message  - https://www.flazke8rules.com/rules/F401.html)

Long line  # E501 (https://www.flake8rules.com/rules/E501.html , characters greater than 79)

Module level import not at the top of file (E402) - https://www.flake8rules.com/rules/E402.html

Two lines after class or function definition (E305)


GitHub Examples - https://github.com/search?q=%23+noqa&type=code
"""
import unused_module # noqa F401

long_line = "This is a very long line which will give warnings in PEP8 and has character more than 79 So we can ignore this warning using noqa appending more words" # noqa E501

import os # noqa

def function1():  # noqa E302
    return "Hello noqa"
if __name__ == "__main__":  # noqa E305
    function1()  # noqa W292