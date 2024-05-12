# addition.py

def add(a, b):
    result = a + b
    with open("output.txt", "w") as f:
        f.write(str(result))

    return result 
    return result

print(add(4, 5))


