class Stack:
    def __init__(self):
        self.__array = []
    
    def push(self,data):
        self.__array.append(data)

    def pop(self):
        if len(self.__array) != 0:
            x = self.__array[-1]
            del self.__array[-1]
            return x
        else:
            return None

    def is_empty(self):
        return len(self.__array) == 0

    def clear(self):
        self.__array = []

    def top(self):
        try:
            return self.__array[-1]
        except:
            return None

def tokenize_infix(ex):
    s1 = []
    low = 0
    high = 0
    while low<len(ex):
        while ex[high] not in '+-*/^':
            if high+1 < len(ex): high += 1
            else: break
        if high == len(ex) -1:
            s1.append(ex[low:])
            break
        else:
            s1.append(ex[low:high])
            s1.append(ex[high])
            high += 1
            low = high
    return s1

def get_precedence(operator,precedence):
    return precedence[operator] if operator in precedence else -1

def infix_to_postfix(ex):
    precedence = {'+': 1,'-': 1,'*': 2,'/': 2,'^': 3}
    s = Stack()
    postfix = ''
    for i in range(len(ex)):
        char = ex[i]
        if char == '(':
            s.push(char)
        elif char == ')':
            while s.top() != '(':
                postfix += s.pop()
            if s.top() == '(': s.pop()
        elif char in precedence:
            if not s.is_empty():
                while get_precedence(char,precedence) <= get_precedence(s.top(),precedence):
                    postfix += s.pop()
            s.push(char)
        else:
            postfix += char
    while not s.is_empty():
        postfix += s.pop()
    return postfix

def infix_to_prefix(ex):
    precedence = {'+': 1,'-': 1,'*': 2,'/': 2,'^': 3}
    operator_stack = Stack()
    operand_stack = Stack()
    for i in range(len(ex)):
        char = ex[i]
        if char == '(':
            operator_stack.push(char)
        elif char == ')':
            while operator_stack.top() != '(':
                b = operand_stack.pop()
                a = operand_stack.pop()
                op = operator_stack.pop()
                operand_stack.push(op+a+b)
            operator_stack.pop()
        elif char in precedence:
            while not operator_stack.is_empty() and get_precedence(char,precedence) <= get_precedence(operator_stack.top(),precedence):
                b = operand_stack.pop()
                a = operand_stack.pop()
                op = operator_stack.pop()
                operand_stack.push(op+a+b) 
            operator_stack.push(char)
        else:
            operand_stack.push(char)
    while not operator_stack.is_empty():
        b = operand_stack.pop()
        a = operand_stack.pop()
        op = operator_stack.pop()
        operand_stack.push(op+a+b)
    return operand_stack.pop()

def prefix_to_infix(ex):
    s = Stack()
    ex = ex[::-1]
    for x in ex:
        if x == '+':
            s.push('(' + s.pop() + '+' + s.pop() + ')')
        elif x == '*':
            s.push('(' + s.pop() + '*' + s.pop() + ')')
        elif x == '/':
            b = s.pop()
            a = s.pop()
            s.push('(' + f'{a}' + '/' + f'{b}' + ')')
        elif x == '%':
            b = s.pop()
            a = s.pop()
            s.push('(' + f'{a}' + '%' + f'{b}' + ')')
        elif x == '^':
            b = s.pop()
            a = s.pop()
            s.push('(' + f'{a}' + '^' + f'{b}' + ')')
        else:
            s.push(x)
    return s.pop()

def postfix_to_infix(ex):
    s = Stack()
    for x in ex:
        if x == '+':
            b = s.pop()
            a = s.pop()
            s.push('(' + f'{a}' + '+' + f'{b}' + ')')
        elif x == '*':
            b = s.pop()
            a = s.pop()
            s.push('(' + f'{a}' + '*' + f'{b}' + ')')
        elif x == '/':
            b = s.pop()
            a = s.pop()
            s.push('(' + f'{a}' + '/' + f'{b}' + ')')
        elif x == '%':
            b = s.pop()
            a = s.pop()
            s.push('(' + f'{a}' + '%' + f'{b}' + ')')
        elif x == '^':
            b = s.pop()
            a = s.pop()
            s.push('(' + f'{a}' + '^' + f'{b}' + ')')
        else:
            s.push(x)
    return s.pop()

def prefix_to_postfix(ex):
    infix_ex = prefix_to_infix(ex)
    return infix_to_postfix(infix_ex)

def postfix_to_prefix(ex):
    infix_ex = postfix_to_infix(ex)
    return infix_to_prefix(infix_ex)

def check_validity(ex):
    if ex[0] in '+-*/^': return 'prefix'
    elif ex[-1] in '+-*/^': return 'postfix'
    else: return 'infix'

def post_eval(ex):
    s = Stack()
    ex = ex.split()
    for x in ex:
        if x == '+':
            s.push((int(s.pop()))+int(s.pop()))
        elif x == '*':
            s.push(int(s.pop())*int(s.pop()))
        elif x == '/':
            b = s.pop()
            a = s.pop()
            s.push(int(a)/int(b))
        elif x == '%':
            b = s.pop()
            a = s.pop()
            s.push(int(a)%int(b))
        elif x == '^':
            b = s.pop()
            a = s.pop()
            s.push(int(a)**int(b))
        else:
            s.push(x)
    return s.pop()

def pre_eval(ex):
    s = Stack()
    ex = ex.split()
    ex = ex[::-1]
    for x in ex:
        if x == '+':
            s.push((int(s.pop()))+int(s.pop()))
        elif x == '*':
            s.push(int(s.pop())*int(s.pop()))
        elif x == '/':
            b = s.pop()
            a = s.pop()
            s.push(int(a)/int(b))
        elif x == '%':
            b = s.pop()
            a = s.pop()
            s.push(int(a)%int(b))
        elif x == '^':
            b = s.pop()
            a = s.pop()
            s.push(int(a)**int(b))
        else:
            s.push(x)
    return s.pop()

def main():
    function_list = [infix_to_postfix,
                    infix_to_prefix,
                    postfix_to_infix,
                    prefix_to_infix,
                    prefix_to_postfix,
                    postfix_to_prefix,
                    check_validity,
                    post_eval,
                    pre_eval]
    while True:
        print('1.infix to postfix\n2.infix to prefix\n3.postfix to infix\n4.prefix to infix\n5.prefix to postfix')
        print('6.postfix to prefix\n7.check validity\n10.post eval\n11.pre eval\n12.Exit')
        try:
            task = int(input("enter the number of the task: "))
            if task == 12: break
            else:
                ex = input('enter the expression: ')
                print(function_list[task-1](ex))
        except:
            print('wrong input')

main()