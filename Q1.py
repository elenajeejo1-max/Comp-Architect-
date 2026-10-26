
def to_8bit(n):
    return format(n & 0xFF, '08b')

def signed_value(binary):
    value = int(binary, 2)
    return value - 256 if value >= 128 else value

def calculate(a, b, operation):
    if operation == '+':
        result = a + b
    else:
        result = a - b

    print(f"\nExpression: ({a}) {operation} ({b})")
    print("First operand :", to_8bit(a))
    print("Second operand:", to_8bit(b))

    if operation == '-':
        print("2's complement of second operand:", to_8bit(-b))

    binary = to_8bit(result)
    overflow = result < -128 or result > 127

    print("Result binary :", binary)
    print("Result decimal:", signed_value(binary))
    print("Overflow:", "Yes" if overflow else "No")

calculate(25, 18, '+')
calculate(-25, -18, '+')
