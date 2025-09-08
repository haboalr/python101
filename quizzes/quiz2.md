# Python Quiz 2 - Functions & Importing Modules

## Question 1
Which keyword is used to define a function in Python?

**Options:**
- A. function
- B. def
- C. define
- D. func

<details>
<summary>Answer</summary>

**B. def**

**Explanation:** Functions are defined with the `def` keyword in Python. This is followed by the function name, parentheses with optional parameters, and a colon to begin the function body.
</details>

---

## Question 2
What is the output of this function call?

```python
def greet():
    print("Hello!")

greet()
```

**Options:**
- A. Hello!
- B. greet
- C. None
- D. Error

<details>
<summary>Answer</summary>

**A. Hello!**

**Explanation:** The function prints "Hello!" when called. The `print()` statement inside the function outputs the text to the console.
</details>

---

## Question 3
What is the output?

```python
def square(x):
    return x * x

print(square(4))
```

**Options:**
- A. 8
- B. 16
- C. x * x
- D. Error

<details>
<summary>Answer</summary>

**B. 16**

**Explanation:** `square(4)` returns 4 * 4 = 16. The function takes the parameter 4 and multiplies it by itself.
</details>

---

## Question 4
Which is a correct function definition?

**Options:**
- A. `def f x: return x + 1`
- B. `def f(x): return x + 1`
- C. `function f(x) return x + 1`
- D. `f(x): return x + 1`

<details>
<summary>Answer</summary>

**B. `def f(x): return x + 1`**

**Explanation:** Correct Python function syntax requires the `def` keyword, function name, parameters in parentheses, and a colon. Option A is missing parentheses, option C uses wrong syntax, and option D is missing the `def` keyword.
</details>

---

## Question 5
What does this function return?

```python
def add(a, b):
    return a + b

print(add(2, 3))
```

**Options:**
- A. 5
- B. 23
- C. Error
- D. a + b

<details>
<summary>Answer</summary>

**A. 5**

**Explanation:** The function adds the two integer parameters: 2 + 3 = 5. Since both arguments are integers, mathematical addition is performed, not string concatenation.
</details>

---

## Question 6
What is the output of this function?

```python
def identity(x):
    return x

result = identity("Python")
print(result)
```

**Options:**
- A. identity
- B. Python
- C. x
- D. Nothing

<details>
<summary>Answer</summary>

**B. Python**

**Explanation:** The identity function returns whatever value is passed to it. Since "Python" is passed as an argument, it returns the string "Python".
</details>

---

## Question 7
What happens if a function has no return statement?

**Options:**
- A. It returns 0
- B. It returns None
- C. It returns an error
- D. It prints its name

<details>
<summary>Answer</summary>

**B. It returns None**

**Explanation:** Python functions return `None` by default if no explicit return statement is given. `None` is a special value in Python that represents the absence of a value.
</details>

---

## Question 8
What is the output?

```python
def power(base, exponent=2):
    return base ** exponent

print(power(3))
```

**Options:**
- A. 6
- B. 3
- C. 9
- D. Error

<details>
<summary>Answer</summary>

**C. 9**

**Explanation:** The function uses a default parameter value. Since no exponent is provided, it uses the default value of 2, so 3² = 9. Default parameters allow functions to be called with fewer arguments.
</details>

---

## Question 9
What is the result of this lambda function?

```python
f = lambda x: x + 5
print(f(2))
```

**Options:**
- A. 7
- B. x + 5
- C. 2 + 5
- D. Error

<details>
<summary>Answer</summary>

**A. 7**

**Explanation:** Lambda functions are anonymous functions. This lambda takes x and returns x + 5. When called with f(2), it returns 2 + 5 = 7.
</details>

---

## Question 10
What is true about lambda functions?

**Options:**
- A. They must be named
- B. They are used for large programs
- C. They are anonymous functions
- D. They are used to define modules

<details>
<summary>Answer</summary>

**C. They are anonymous functions**

**Explanation:** Lambda functions are anonymous (unnamed) functions that can be defined inline. They're typically used for short, simple functions that can be expressed in a single expression.
</details>

---

## Question 11
Which of the following is a recursive function?

**Options:**
- A. 
```python
def repeat():
    print("Again")
```

- B. 
```python
def f(x):
    return x * x
```

- C. 
```python
def f():
    f()
```

- D. 
```python
def f(x):
    return x + 1
```

<details>
<summary>Answer</summary>

**C.**
```python
def f():
    f()
```

**Explanation:** A recursive function is one that calls itself. Option C shows a function that calls itself, making it recursive. However, this particular example would cause infinite recursion since there's no base case to stop the recursion.
</details>

---

## Question 12
How do you import the math module?

**Options:**
- A. import.math
- B. load math
- C. use math
- D. import math

<details>
<summary>Answer</summary>

**D. import math**

**Explanation:** The correct syntax to import a module in Python is `import module_name`. The `import` keyword is used followed by the module name.
</details>

---

## Question 13
What is the output?

```python
import math
print(math.sqrt(16))
```

**Options:**
- A. 8
- B. 4.0
- C. math.sqrt(16)
- D. Error

<details>
<summary>Answer</summary>

**B. 4.0**

**Explanation:** `math.sqrt(16)` computes the square root of 16, which is 4. The result is a float (4.0) because the `sqrt` function always returns a floating-point number.
</details>

---

## Question 14
What is the correct way to import only the sqrt function?

**Options:**
- A. import sqrt from math
- B. from math import sqrt
- C. from sqrt import math
- D. use math.sqrt()

<details>
<summary>Answer</summary>

**B. from math import sqrt**

**Explanation:** The correct syntax to import specific functions from a module is `from module_name import function_name`. This allows you to use `sqrt()` directly without the `math.` prefix.
</details>

---

## Question 15
Which module is used to generate random numbers in Python?

**Options:**
- A. math
- B. randomizer
- C. random
- D. numbers

<details>
<summary>Answer</summary>

**C. random**

**Explanation:** The `random` module is Python's built-in module for generating random numbers. It provides functions like `random()`, `randint()`, `choice()`, and many others for various random operations.
</details>

---

## Question 16
What is the effect of this code?

```python
from math import sqrt as square_root
print(square_root(9))
```

**Options:**
- A. Error
- B. 81
- C. 3.0
- D. sqrt(9)

<details>
<summary>Answer</summary>

**C. 3.0**

**Explanation:** The `as` keyword creates an alias for the imported function. `sqrt` is imported as `square_root`, so calling `square_root(9)` is equivalent to calling `sqrt(9)`, which returns 3.0.
</details>

---

## Question 17
Which statement is true about `import *`?

**Options:**
- A. It imports all functions and variables from a module.
- B. It is always recommended for clean code.
- C. It imports only selected functions.
- D. It creates a new module automatically.

<details>
<summary>Answer</summary>

**A. It imports all functions and variables from a module.**

**Explanation:** `import *` imports all public names from a module into the current namespace. However, this practice is generally discouraged because it can pollute the namespace and make code harder to read and debug.
</details>

---

## Question 18
What is printed?

```python
import random
print(random.randint(1, 1))
```

**Options:**
- A. 0
- B. 1
- C. Error
- D. A random number between 0 and 1

<details>
<summary>Answer</summary>

**B. 1**

**Explanation:** `random.randint(a, b)` returns a random integer between a and b (inclusive). When both bounds are 1, the only possible value is 1, so it always returns 1.
</details>

---

## Question 19
What happens if you try to import a module that does not exist?

**Options:**
- A. It prints a warning
- B. It silently ignores the import
- C. It raises an ImportError
- D. It returns None

<details>
<summary>Answer</summary>

**C. It raises an ImportError**

**Explanation:** If Python cannot find the specified module, it raises an `ImportError` (or `ModuleNotFoundError` in Python 3.3+). This stops program execution unless the error is handled with a try-except block.
</details>

---

## Question 20
Why are modules used in Python?

**Options:**
- A. To increase execution speed only
- B. To organize code and reuse functionality
- C. To prevent syntax errors
- D. To automatically generate classes

<details>
<summary>Answer</summary>

**B. To organize code and reuse functionality**

**Explanation:** Modules are used to organize code into logical units and promote code reusability. They allow you to break large programs into smaller, manageable files and share functionality across multiple programs. This makes code more maintainable and reduces duplication.
</details>
