# Quiz 1 – Python Basics & Control Structures

## Question 1
Which of the following is NOT a valid Python variable name?

**Options:**
- A. my_var
- B. _hidden
- C. 2nd_value
- D. userName

<details>
<summary><strong>Show Answer</strong></summary>

**Answer: C. 2nd_value**

**Explanation:** In Python, variable names cannot begin with a digit. Valid names can include letters, digits, and underscores, but must start with a letter or underscore. That's why my_var, _hidden, and userName are fine, but 2nd_value is invalid.
</details>

---

## Question 2
What is the output of the following code?

```python
x = 3.0
y = 2
print(type(x + y))
```

**Options:**
- A. `<class 'int'>`
- B. `<class 'float'>`
- C. `<class 'str'>`
- D. Error

<details>
<summary><strong>Show Answer</strong></summary>

**Answer: B. `<class 'float'>`**

**Explanation:** Arithmetic with a float and an integer always promotes to float in Python (implicit type conversion). This is called type coercion, and it prevents data loss from truncation.
</details>

---

## Question 3
What will this code print?

```python
s = "Python"
print(s[0], s[-1], s[2:5], s[::-1])
```

**Options:**
- A. P n tho nohtyP
- B. P n yth nho
- C. P n tho nohtyP
- D. Error

<details>
<summary><strong>Show Answer</strong></summary>

**Answer: A. P n tho nohtyP**

**Explanation:**
- `s[0]` → first character "P"
- `s[-1]` → last character "n"
- `s[2:5]` → substring from index 2 up to 5 → "tho"
- `s[::-1]` → reverses the string → "nohtyP"

This tests slicing with both positive and negative indices.
</details>

---

## Question 4
Which operator is used for floor division in Python?

**Options:**
- A. /
- B. //
- C. %
- D. **

<details>
<summary><strong>Show Answer</strong></summary>

**Answer: B. //**

**Explanation:** The // operator performs integer division, discarding the decimal part. For example, 10 // 3 gives 3. In contrast, / gives floating-point division, % gives remainder, and ** is exponentiation.
</details>

---

## Question 5
What is the result of this code?

```python
print(bool(0), bool(""), bool([]), bool("Python"))
```

**Options:**
- A. False False False True
- B. True False True True
- C. False True False True
- D. Error

<details>
<summary><strong>Show Answer</strong></summary>

**Answer: A. False False False True**

**Explanation:** In Python, 0, "" (empty string), and empty containers (lists, tuples, sets, dicts) evaluate as False. Any non-empty string (like "Python") is True.
</details>

---

## Question 6
Which function takes input from the user?

**Options:**
- A. scanf()
- B. input()
- C. read()
- D. raw_input()

<details>
<summary><strong>Show Answer</strong></summary>

**Answer: B. input()**

**Explanation:** input() always returns data as a string, regardless of what the user types. In Python 2, there was raw_input(), but in Python 3, input() replaced it.
</details>

---

## Question 7
What is the output?

```python
x = 5
if x > 10:
    print("A")
elif x > 3:
    print("B")
else:
    print("C")
```

**Options:**
- A. A
- B. B
- C. C
- D. Error

<details>
<summary><strong>Show Answer</strong></summary>

**Answer: B. B**

**Explanation:** The first condition x > 10 is False. The elif x > 3 is True, so it prints "B". Python checks conditions in order and executes only the first True block.
</details>

---

## Question 8
Which operator is used for logical negation?

**Options:**
- A. !
- B. not
- C. ~
- D. neg

<details>
<summary><strong>Show Answer</strong></summary>

**Answer: B. not**

**Explanation:** In Python, not negates a boolean. For example, not True → False. ! is not valid in Python (unlike some other languages). ~ is bitwise negation, not logical.
</details>

---

## Question 9
What will this loop output?

```python
for i in range(1, 5, 2):
    print(i, end=" ")
```

**Options:**
- A. 1 2 3 4
- B. 1 3
- C. 1 3 5
- D. Error

<details>
<summary><strong>Show Answer</strong></summary>

**Answer: B. 1 3**

**Explanation:** range(start, stop, step) produces 1, 3. The stop value 5 is not included.
</details>

---

## Question 10
Which statement immediately ends the current loop iteration and continues with the next one?

**Options:**
- A. stop
- B. break
- C. exit
- D. continue

<details>
<summary><strong>Show Answer</strong></summary>

**Answer: D. continue**

**Explanation:** continue skips the rest of the current loop body and jumps to the next iteration. break exits the loop entirely.
</details>

---

## Question 11
What is the output?

```python
count = 0
while count < 3:
    print(count, end=" ")
    count += 1
```

**Options:**
- A. 0 1 2
- B. 1 2 3
- C. Infinite loop
- D. Error

<details>
<summary><strong>Show Answer</strong></summary>

**Answer: A. 0 1 2**

**Explanation:** Loop starts at count = 0. It increments by 1 each time until count < 3 is False.
</details>

---

## Question 12
Predict the output:

```python
for i in range(2):
    for j in range(2):
        print(i + j, end=" ")
```

**Options:**
- A. 0 1 1 2
- B. 0 1 2 3
- C. 1 2 3 4
- D. Error

<details>
<summary><strong>Show Answer</strong></summary>

**Answer: A. 0 1 1 2**

**Explanation:** Iterations:
- i=0, j=0 → 0
- i=0, j=1 → 1
- i=1, j=0 → 1
- i=1, j=1 → 2
</details>

---

## Question 13
What will this code print?

```python
x = 0
while x < 5:
    if x % 2 == 0:
        print(x, end=" ")
    x += 1
```

**Options:**
- A. 0 2 4
- B. 1 3 5
- C. 0 1 2 3 4
- D. Infinite loop

<details>
<summary><strong>Show Answer</strong></summary>

**Answer: A. 0 2 4**

**Explanation:** The loop prints only when x % 2 == 0. That condition is True for even numbers. This question checks understanding of while loops + conditions together.
</details>

---

## Question 14
Explain the difference between break and continue with an example.

<details>
<summary><strong>Show Answer</strong></summary>

**break** completely exits a loop.
**continue** skips to the next iteration but keeps looping.

**Example:**
```python
for i in range(5):
    if i == 2:
        continue   # skips printing 2
    if i == 4:
        break      # stops loop entirely
    print(i)
```

This prints: 0 1 3.
</details>

---

## Question 15
What is the output?

```python
total = 0
for i in range(1, 5):
    total += i
print(total)
```

**Options:**
- A. 10
- B. 15
- C. 5
- D. Error

<details>
<summary><strong>Show Answer</strong></summary>

**Answer: A. 10**

**Explanation:** Sum of 1+2+3+4 = 10. This is a typical pattern to accumulate values in a loop.
</details>

---

## Question 16
What is the output?

```python
for i in range(3):
    for j in range(3):
        if i == j:
            print(i, j, end="; ")
```

**Options:**
- A. 0 0; 1 1; 2 2;
- B. 0 0; 0 1; 1 1; 2 2;
- C. 0 0; 1 1; 2 2; 3 3;
- D. Error

<details>
<summary><strong>Show Answer</strong></summary>

**Answer: A. 0 0; 1 1; 2 2;**

**Explanation:** The if i == j ensures only diagonal pairs are printed. This tests logic inside nested loops.
</details>

---

## Question 17
Write a Python program using a loop that prints only the odd numbers from 1 to 10.

<details>
<summary><strong>Show Answer</strong></summary>

```python
for i in range(1, 11):
    if i % 2 != 0:
        print(i)
```

**Explanation:** The modulus operator % checks divisibility. If i % 2 != 0, then i is odd.
</details>

---

## Question 18
Why might you use a while loop instead of a for loop?

<details>
<summary><strong>Show Answer</strong></summary>

A while loop is used when the number of iterations is not known in advance. For example, reading user input until they type "quit", or running until a sensor reaches a certain value. In contrast, a for loop is better when iterating over a fixed range or sequence.
</details>

---

## Question 19
What does this code output?

```python
x = 10
if x > 5 and not (x % 2 == 0):
    print("Odd and >5")
else:
    print("Other")
```

**Options:**
- A. Odd and >5
- B. Other
- C. Error
- D. Nothing

<details>
<summary><strong>Show Answer</strong></summary>

**Answer: B. Other**

**Explanation:** x=10 is > 5 (True), but x % 2 == 0 is True (since 10 is even), so not (True) = False. The whole condition is False, so the else branch executes. This tests understanding of boolean logic.
</details>

---

## Question 20
What will this code print?

```python
for i in range(5, 0, -2):
    print(i, end=" ")
```

**Options:**
- A. 5 4 3 2 1
- B. 5 3 1
- C. 5 0
- D. Error

<details>
<summary><strong>Show Answer</strong></summary>

**Answer: B. 5 3 1**

**Explanation:** range(start, stop, step) → 5, 3, 1. Step = -2 counts downward.
</details>

---

## Question 21
Write a Python program that asks the user for a number and prints whether it is prime or not.

<details>
<summary><strong>Show Answer</strong></summary>

```python
n = int(input("Enter a number: "))
is_prime = True
if n < 2:
    is_prime = False
else:
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            is_prime = False
            break
if is_prime:
    print("Prime")
else:
    print("Not Prime")
```

**Explanation:** This tests loops, conditions, and input. Checking divisors up to sqrt(n) is efficient.
</details>

---

## Question 22
What is the difference between `=`, `==`, and `is` in Python?

<details>
<summary><strong>Show Answer</strong></summary>

- `=` → assignment (stores a value in a variable)
- `==` → equality comparison (checks if two values are equal in value)
- `is` → identity comparison (checks if two variables refer to the same object in memory)

**Example:**
```python
a = [1,2]
b = [1,2]
print(a == b)  # True (same values)
print(a is b)  # False (different memory locations)
```
</details>
