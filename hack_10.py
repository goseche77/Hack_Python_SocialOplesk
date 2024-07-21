"""
text: "fooziman" output => ["F","0","0","Z","1","M","@","N"]
"""

def fn_hack_10():
    result = "fooziman"
    
    nombre = "fooziman"
    
    nombre = nombre.upper()
    
    substitucion = {
        'O': '0',
        'I': '1',
        'A': '@'
    }
    
    result = []
    for char in nombre:
        if char in substitucion:
            result.append(substitucion[char])
        else:
            result.append(char)
    
    return result