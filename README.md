# Arithmetic Formatter

This is a challenge proposed by freeCodeCamp which I present here my solution, where you had to create a function that receives a list of strings that are arithmetic problems and returns the problems arranged vertically and side-by-side. The function should optionally take a second argument. When the second argument is set to True, the answers should be displayed.

- If there are too many problems supplied to the function. **The limit is five**, anything more will return: *Error: Too many problems.*

- The appropriate operators the function will accept are addition and subtraction. Multiplication and division will return an error. Other operators not mentioned in this bullet point will not need to be tested. The error returned will be: *Error: Operator must be '+' or '-'.*

- Each number (operand) should **only contain digits**. Otherwise, the function will return: *Error: Numbers must only contain digits.*

- Each operand (aka number on each side of the operator) has a max of **four digits in width**. Otherwise, the error string returned will be: Error: *Numbers cannot be more than four digits.*