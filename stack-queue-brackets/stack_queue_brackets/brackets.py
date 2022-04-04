from logging import exception
from stack_queue_brackets.stack import Stack

def validateBrackets(string):
    '''
    validate brackets
    Arguments: string
    Return: boolean
    representing whether or not the brackets in the string are balanced
    '''
    stack = Stack()
    if string == None:
        raise exception("you should pass valid string ")
    else:
        for chr  in string:
            if chr =="(":
                stack.push("(")
            elif chr ==")":
                if (stack.IsEmpty() or stack.pop() != "(" ):
                    return False #Invalid Expression
            elif chr =="{":
                stack.push("{")
            elif chr =="}":
                if ( stack.IsEmpty() or stack.pop() != "{"):
                    return False #Invalid Expression
            elif chr =="[":
                stack.push("[")
            elif chr =="]":
                if ( stack.IsEmpty() or stack.pop() != "["):
                    return False #Invalid Expression
        
        if stack.IsEmpty():
            return True #Valid Expression
        else:
            return False #Invalid expression


    