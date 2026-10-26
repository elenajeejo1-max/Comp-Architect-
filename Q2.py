
def ror(binary, positions):
    print("\nRotate Right Without Carry (ROR)")
    print("Original:", binary)

    for i in range(positions):
        binary = binary[-1] + binary[:-1]
        print(f"After rotation {i + 1}:", binary)

    print("Final result:", binary)

def rcr(binary, carry, positions):
    print("\nRotate Right Through Carry (RCR)")
    print("Original:", binary)
    print("Initial carry:", carry)

    for i in range(positions):
        new_carry = int(binary[-1])
        binary = str(carry) + binary[:-1]
        carry = new_carry
        print(f"After rotation {i + 1}: "
              f"Carry={carry}, Binary={binary}")

    print("Final result:", binary)
    print("Final carry:", carry)

ror("11010101", 3)
rcr("11010101", 0, 3)
