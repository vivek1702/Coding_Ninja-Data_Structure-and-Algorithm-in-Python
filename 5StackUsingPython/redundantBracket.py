from sys import stdin

def checkRedundantBrackets(expression) :
	# Your code goes here
    st = []
    for ch in expression:
 
        # if current character is close
        # parenthesis ')'
        if (ch == ')'):
            top = st[-1]
            st.pop()
 
            # If immediate pop have open parenthesis
            # '(' duplicate brackets found
            flag = True
 
            while (top != '('):
 
                # Check for operators in expression
                if (top == '+' or top == '-' or
                    top == '*' or top == '/'):
                    flag = False
 
                # Fetch top element of stack
                top = st[-1]
                st.pop()
 
            # If operators not found
            if (flag == True):
                return True
 
        else:
            st.append(ch) # append open parenthesis '(',
                          # operators and operands to stack
    return False



#main
expression = stdin.readline().strip()

if checkRedundantBrackets(expression) :
	print("true")

else :
	print("false")

#(a+b)