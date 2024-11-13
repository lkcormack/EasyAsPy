# underscores_in_python



1️⃣ single leading underscore ("_var"): indicates that the variable is meant for internal use. This is not enforced by the interpreter and is rather a hint to the programmer.

2️⃣ single trailing underscore ("var_"): it's used to avoid conflicts with Python reserved keywords ("class_", "def_", etc.)

3️⃣ double leading underscores ("__var"): Triggers name mangling when used in a class context and is enforced by the Python interpreter. 
What this means is that it should be used to avoid your method is being overridden by a subclass or accessed accidentally.

4️⃣ double leading and trailing underscores ("__var__"): used for special methods defined in the Python language (ex. __init__, __len__, __call__, etc.). They should be avoided to use for your own attributes.

5️⃣ single underscore ("_"): Generally used as a temporary or unused variable. (If you don't use the running index of a for-loop, you can replace it with "_").