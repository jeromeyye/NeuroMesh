def check_parentheses(input_str):
    stack = []
    result = [" "] * len(input_str) 
    for i, char in enumerate(input_str):
        if char == '(':
            stack.append(i)
        elif char == ')':
            if stack:
                stack.pop()
            else:
                result[i] = '?'
        
    while stack:
        result[stack.pop()] = 'x'

    ans = input_str + "\n" + "".join(result)
    return ans

print(check_parentheses("bge)))))))))")) 
print(check_parentheses("((IIII))))))"))  
print(check_parentheses("()()()()(uuu")) 
print(check_parentheses("))))UUUU((()"))  
