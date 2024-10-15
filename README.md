# 5.2 for Loops

#### **Learning Objective:**  
You will write Python functions to solve a variety of problems using for loops. This will help you build your skills in looping, string manipulation, and working with numbers.

---

### **Task 1: Numbers in a String**  
Write a function that takes in a number and returns a string of all numbers from 1 to the given number, separated by spaces.

**Function Signature:**
```python
def numbers_in_string(num: int) -> str:
    """
    Return a string containing numbers from 1 to num, separated by spaces.
    """
    pass
```

**Example:**
```python
print(numbers_in_string(5))  # Output: "1 2 3 4 5 "
```

---

### **Task 2: Factorial**

The factorial of a number is the product of all positive integers less than or equal to that number. For example, the factorial of 5 (written as 5!) is `5 * 4 * 3 * 2 * 1 = 120`.
  
Factorials grow very quickly as the number increases. For example, `7! = 7 * 6 * 5 * 4 * 3 * 2 * 1 = 5040`.

Write a function that returns the factorial of a given number.

**Function Signature:**
```python
def factorial(n: int) -> int:
    """
    Return the factorial of the given number n.
    """
    pass
```

**Example:**
```python
print(factorial(5))  # Output: 120
```

---

### **Task 4: Count the "a"s in a String**

Write a function that takes a string and returns the number of occurrences of the letter "a" (case-insensitive).

**Function Signature:**
```python
def count_as(s: str) -> int:
    """
    Return the number of "a" characters in the string s.
    """
    pass
```

**Example:**
```python
print(count_as("Apples and Bananas"))  # Output: 5
```

---

### **Task 5: Multiples of 3**

Write a function that takes in a number and returns a string of all the numbers from 3 to that number that are multiples of 3.

**Function Signature:**
```python
def multiples_of_3(num: int) -> str:
    """
    Return a string of all multiples of 3 from 1 to num, separated by spaces.
    """
    pass
```

**Example:**
```python
print(multiples_of_3(10))  # Output: "3 6 9 "
```

---

### **Task 6: Number Pyramid**

Write a function that takes in a number and prints a pyramid. The top level should be 1, and each subsequent level should contain numbers from 1 to that level number.

**Function Signature:**
```python
def number_pyramid(num: int) -> None:
    """
    Print a pyramid of numbers from 1 to num.
    """
    pass
```

**Example:**
```python
number_pyramid(5)
# Output:
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5
```

---

### **Task 7: Multiplication Table**

Write a function that takes a number `num` and prints a multiplication table from 1 to `num`. Each line should display the product of `num` and each number, formatted using an f-string.

**Function Signature:**
```python
def multiplication_table(num: int) -> None:
    """
    Print a multiplication table for the given number num.
    """
    pass
```

**Example:**
```python
multiplication_table(3)
# Output:
# 3 * 1 = 3
# 3 * 2 = 6
# 3 * 3 = 9
```

---

### **Task 8: Count Words with "cat"**

Write a function that takes in a list of words and returns a count of how many words contain the substring "cat" (case-insensitive).

**Function Signature:**
```python
def count_cat_words(words: list) -> int:
    """
    Return the count of words that contain 'cat' in the list of words.
    """
    pass
```

**Example:**
```python
words = ["catalog", "catapult", "dog", "scatter", "concatenate"]
print(count_cat_words(words))  # Output: 4
```
