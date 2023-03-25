"""
Author: Logan Maupin
Date: 03/25/2023

The purpose of this script is to implement the fast modular exponentiation algorithm for the sake of easier modular
arithmetic with large exponent numbers.

Source to this method explained by Susan Zehra can be found here:
https://www.youtube.com/watch?v=8r4-5k-o1QE
"""


def find_largest_power_of_two(input_number: int) -> int:
    """
    The purpose of this function is to get the highest power of 2 that can be represented by the input number integer.
    If the function is given 255 for example, it will return 8, the input number of 255 is greater than 2^7.

    In which case, 8 is the smallest number of bits that could be used to represent that number.

    :param input_number:
    :returns: integer value representing the power of 2 that must be used to represent the number.
    """
    i = 0
    while (2**i - 1) < input_number:
        i += 1
    return i


def convert_number_to_binary(input_number: int) -> str:
    """
    Takes an input number and converts it to a binary string of characters of which we can iterate through using the
    fast modular exponentiation algorithm.

    :param input_number: Any integer that you wish to get the full binary representation for.
    :returns: binary string, not including the "0b" at the beginning.
    """
    return bin(input_number)[2:]


def fast_modular_exponentiation(input_number: int, exponent: int, modulus_number) -> int:
    """
    This function actually performs the algorithm in question. For more information on how the algorithm works,
    watch the linked video at the top of the file.

    :param input_number: base number. so i.e. in (240 ^ 262) % 14, 240 would be your base number.
    :param exponent: exponent number. so i.e. in (240 ^ 262) % 14, 262 would be your exponent number.
    :param modulus_number: modulus number. so i.e. in (240 ^ 262) % 14, 14 would be your modulus number.
    :returns: Modulus of the final product. The answer to your question. :)
    """

    binary_number_string = convert_number_to_binary(exponent)[1:]

    current_digit_value = input_number

    for i in range(len(binary_number_string)):

        if binary_number_string[i] == "1":
            current_digit_value = (current_digit_value * current_digit_value) % modulus_number
            current_digit_value = (current_digit_value * input_number) % modulus_number

        elif binary_number_string[i] == "0":
            current_digit_value = (current_digit_value * current_digit_value) % modulus_number

    return current_digit_value


def number_is_an_integer(input_number: str) -> bool:
    """
    This function takes a number from a string and returns True or False depending on if the given string is
    actually an integer. I.e. "1" would return true, "1.0" would return false. "a" would also return false.

    :param input_number: any string which is a digit of some kind.
    :returns: True or False depending on if the number in the string is actually an integer
    """
    #  make sure these are actually integers and not floats.
    if input_number.isdigit() and "." not in input_number:
        return True


def get_numbers_from_user():
    """
    This function gets the numbers we will use to perform this algorithm from the user via user input. Then formats
    those numbers to match the proper formatting necessary to complete the calculations.

    :returns: list of numbers in order from base number, exponent, and modulus number.
    """
    while True:
        # Since modular arithmetic is all about integers, these numbers must be an integers.
        # we will use the isdigit method to make sure the user actually gave us integers
        base_number = input("Please enter the base number of your large exponent: ")
        if number_is_an_integer(base_number):
            base_number = int(base_number)

        exponent_number = input("Please enter the exponent power of your large exponent: ")
        if number_is_an_integer(exponent_number):
            exponent_number = int(exponent_number)

        modulus_number = input("Please enter your modulus number: ")
        if number_is_an_integer(modulus_number):
            modulus_number = int(modulus_number)

        return [base_number, exponent_number, modulus_number]


def main():
    """
    This function uses all the other functions in the specified order in order to make this script work properly.
    :returns: None
    """
    number_list = get_numbers_from_user()
    base_number = number_list[0]
    exponent_number = number_list[1]
    modulus_number = number_list[2]

    print(fast_modular_exponentiation(base_number, exponent_number, modulus_number))


if __name__ == '__main__':
    main()
