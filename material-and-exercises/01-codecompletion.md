# Exercise 01: Code completion

**Aim**: Learn how to use code completion and use the Inline Chat feature of GitHub Copilot to improve your code.


## Instructions

Open a new file, save it as `calc.py` or something similar that indicates a Python script. 

In the file start typing: `def add(a,b)`. With CoPilot code completions enabled, you should see a suggestion to complete the function definition. Accept the suggestion by pressing `Tab` or `Enter`.

You should now have a function definition that looks like this:

```python
def add(a, b):
    return a + b
```

What do you think about this function? How you can you improve it? 

Two things you can do to improve are type hints and a docstring.

To do that you can use the Inline Chat feature of CoPilot. Open the Inline Chat by clicking on the CoPilot icon in the searchbar or using the shortcut `Ctrl+Shift+I` (or `Cmd+Shift+I` on macOS).

Type `/edit Add type hints and docstring` and press `Enter`. 


You should get something like this: 

```python
def add(a: int, b: int) -> int:
    """Add two integers and return the result."""
    return a + b
```


Is this docstring complete? If you are unsure you could even ask CoPilot: "Is this docstring complete?" in the Inline Chat. CoPilot will suggest improvements to the docstring.

```python
def add(a: int, b: int) -> int:
    """
    Add two integers and return the result.

    Args:
        a (int): The first integer to add.
        b (int): The second integer to add.

    Returns:
        int: The sum of the two integers.
    """
    return a + b
```

---

**Test yourself**

❓ What happens if you use the Inline Chat using `/doc` without further instructions?

---

## Further exercises: 

- Add a function `subtract(a, b)` by start typing the function definition. How does the resulting function look like? 

- Use the Inline Chat function using the instruction `/generate ` and your own prompt to add additional function definitions like `multiply(a, b)` and `divide(a, b)`.

- Turn on Next Edit Suggestion by clicking on the CoPilot icon in the lower right corner of the status bar.  To test the function choose one of your functions and rename the parameters to num1 and num2. What happens?
