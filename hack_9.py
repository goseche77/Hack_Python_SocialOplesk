"""
loop: while [1,2,3] ouput => [1,'@',2,'@',3,'@']
"""

def fn_hack_9():
    result = [1,2,3]
    num = 0
    while num < len(result):
        result.insert(num+1,'@')
        num += 2
    return result  