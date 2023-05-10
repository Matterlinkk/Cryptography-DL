class BigInt:

    def __init__(self, value, flag="D"):
        if flag == "D":
            self.num = value
            self.flag = flag
        if flag == "H":
            self.num = value
            self.flag = flag
        if flag == "B":
            self.num = str(int(self.num, 2))
            self.flag = flag

    def get_hex(self) -> str:
        if self.flag == "H":
            return self.num
        elif self.flag == "D":
            return hex(int(self.num))[2:]
        elif self.flag == "B":
            return hex(int(self.num, 2))[2:]

    def get_decimal(self) -> str:
        if self.flag == "D":
            return self.num
        elif self.flag == "H":
            return str(int(self.num, 16))
        elif self.flag == "B":
            return str(int(self.num, 2))

    def get_binary(self) -> str:
        if self.flag == "B":
            return self.num
        elif self.flag == "D":
            return bin(int(self.num))[2:]
        elif self.flag == "H":
            return bin(int(self.num, 16))[2:]

    def set_to_hex(self, other: int):
        self.num = hex(other)[2:]
        self.flag = "H"

    def set_to_decimal(self, other):
        self.flag = "D"
        self.num = int(other, 16)

    def set_to_binary(self, other):
        self.flag = "B"
        self.num = bin(other)[2:]

    def show_all(self):
        print(f'{self.get_binary()} - binary')
        print(f'{self.get_decimal()} - decimal')
        print(f'{self.get_hex()} - hex')

    def sum_class_type(self, other): #func SUM

        value1 = self.get_decimal()
        value2 = other.get_decimal()
        result = int(value1) + int(value2)
        result_hex = hex(result)[2:]
        result_binary = bin(result)[2:]

        print(f'{result_binary} - binary')
        print(f'{result} - decimal')
        print(f'{result_hex} - hex')

        return 'SUM'

    def sub_class_type(self, other): #func SUB

        value1 = self.get_decimal()
        value2 = other.get_decimal()
        if value1 > value2:
            result = int(value1) - int(value2)
        else:
            result = int(value2) - int(value1)
        result_hex = hex(result)[2:]
        result_binary = bin(result)[2:]

        print(f'{result_binary} - binary')
        print(f'{result} - decimal')
        print(f'{result_hex} - hex')

        return 'SUB'

    def mod_class_type(self, other):

        value1 = self.get_decimal()
        value2 = other.get_decimal()

        result = int(value1) % int(value2)
        result_hex = hex(result)[2:]
        result_binary = bin(result)[2:]

        print(f'{result_binary} - binary')
        print(f'{result} - decimal')
        print(f'{result_hex} - hex')

        return "MOD"

    def mul_class_type(self, other): #func MUL

        value1 = self.get_decimal()
        value2 = other.get_decimal()

        result = int(value1) * int(value2)
        result_hex = hex(result)[2:]
        result_binary = bin(result)[2:]

        print(f'{result_binary} - binary')
        print(f'{result} - decimal')
        print(f'{result_hex} - hex')

        return 'MUL'

    def inv_class_type(self):

        result = ~int(self.get_decimal())
        result_hex = hex(result)
        result_binary = bin(result)

        print(f'{result_binary[0] + result_binary[3:]} - binary')
        print(f'{result} - decimal')
        print(f'{result_hex[0] + result_hex[3]} - hex')

        return 'INV'

    def xor_class_type(self, other):

        value1 = self.get_decimal()
        value2 = other.get_decimal()
        result = int(value1) ^ int(value2)
        result_hex = hex(result)
        result_binary = bin(result)

        print(f'{result_binary[2:]} - binary')
        print(f'{result} - decimal')
        print(f'{result_hex[2:]} - hex')

        return 'XOR'

    def or_class_type(self, other):

        value1 = self.get_decimal()
        value2 = other.get_decimal()
        result = int(value1) | int(value2)
        result_hex = hex(result)
        result_binary = bin(result)

        print(f'{result_binary[2:]} - binary')
        print(f'{result} - decimal')
        print(f'{result_hex[2:]} - hex')

        return 'OR'

    def and_class_type(self, other):

        value1 = self.get_decimal()
        value2 = other.get_decimal()
        result = int(value1) & int(value2)
        result_hex = hex(result)
        result_binary = bin(result)

        print(f'{result_binary[2:]} - binary')
        print(f'{result} - decimal')
        print(f'{result_hex[2:]} - hex')

        return 'AND'

    def __str__(self):
        return self.num


number = BigInt("51bf608414ad5726a3c1bec098f77b1b54ffb2787f8d528a74c1d7fde6470ea4", "H")
number1 = BigInt("403db8ad88a3932a0b7e8189aed9eeffb8121dfac05c3512fdb396dd73f6331c", "H")
print("Перші тестові дані")
number.xor_class_type(number1)

number = BigInt("36f028580bb02cc8272a9a020f4200e346e276ae664e45ee80745574e2f5ab80", "H")
number1 = BigInt("70983d692f648185febe6d6fa607630ae68649f7e6fc45b94680096c06e4fadb", "H")
print("Другі тестові дані")
number.sum_class_type(number1)

number = BigInt("33ced2c76b26cae94e162c4c0d2c0ff7c13094b0185a3c122e732d5ba77efebc", "H")
number1 = BigInt("22e962951cb6cd2ce279ab0e2095825c141d48ef3ca9dabf253e38760b57fe03", "H")
print("Треті тестові дані")
number.sub_class_type(number1)

number = BigInt("7d7deab2affa38154326e96d350deee1", "H")
number1 = BigInt("97f92a75b3faf8939e8e98b96476fd22", "H")
print("Четверті тестові дані")
number.mul_class_type(number1)
