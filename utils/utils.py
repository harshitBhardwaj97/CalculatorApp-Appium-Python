from random import randint
from typing import Dict, List, Tuple, Literal
from tests.locators import Locators
from math import pow, sqrt


def get_two_random_ints_and_result(operation: Literal['+', '-', '*', '/']) \
        -> Tuple[int, int, int | float, List[Tuple[str, str]]]:
    first_number = randint(10, 99)
    second_number = randint(10, 99)
    match operation:
        case '+':
            result = first_number + second_number
            print(f'first_number = {first_number}, second_number = {second_number}, '
                  f'operation = ({operation}) and result {result}')
        case '-':
            result = first_number - second_number
            print(f'first_number = {first_number}, second_number = {second_number}, '
                  f'operation = ({operation}) and result = {result}')
        case '*':
            result = first_number * second_number
            print(f'first_number = {first_number}, second_number = {second_number}, '
                  f'operation = ({operation}) and result = {result}')
        case '/':
            result = first_number / second_number
            print(f'first_number = {first_number}, second_number = {second_number}, '
                  f'operation = ({operation}) and result = {result}')
        case _:
            raise Exception("Invalid literal passed, use any of the following -> ['+', '-', '*', '/']")

    locators_list = get_locators_list_with_numbers_and_operation(first_number, second_number, operation)

    return first_number, second_number, result, locators_list


def get_power_result() -> tuple[int, int, int, list[tuple[str, str]]]:
    first_number: int = randint(1, 9)
    second_number: int = randint(1, 9)

    result: int = int(pow(first_number, second_number))

    print(f'first_number = {first_number}, second_number = {second_number}, '
          f'operation = (^) and result {result}')

    locators_list = get_locators_list_with_numbers_and_operation(first_number, second_number, '^')

    return first_number, second_number, result, locators_list


def get_square_root_result() -> Tuple[int, float|int, List[Tuple[str, str]]]:
    number: int = randint(10, 10000)
    result: float = sqrt(number)

    print(f'Square root of = {number} is = {result}')

    locators_list = get_locators_list_for_a_number(number)

    return number, result, locators_list


def get_locators_list_with_numbers_and_operation(first_number: int, second_number: int,
                                 operation: Literal['+', '-', '*', '/', '^']) -> List[Tuple[str, str]]:
    locators: List[Tuple[str, str]] = []

    locators_map: Dict[str, Tuple[str, str]] = {
        '0': Locators.number_zero,
        '1': Locators.number_one,
        '2': Locators.number_two,
        '3': Locators.number_three,
        '4': Locators.number_four,
        '5': Locators.number_five,
        '6': Locators.number_six,
        '7': Locators.number_seven,
        '8': Locators.number_eight,
        '9': Locators.number_nine,
        '+': Locators.add_operation,
        '-': Locators.subtract_operation,
        '*': Locators.multiply_operation,
        '/': Locators.divide_operation,
        '^': Locators.power_operation,
    }

    for digit in str(first_number):
        locators.append(locators_map.get(digit))

    locators.append(locators_map.get(operation))

    for digit in str(second_number):
        locators.append(locators_map.get(digit))

    return locators


def get_locators_list_for_a_number(number: int) -> List[Tuple[str, str]]:
    number_str: str = str(number)
    
    locators: List[Tuple[str, str]] = []

    locators_map: Dict[str, Tuple[str, str]] = {
        '0': Locators.number_zero,
        '1': Locators.number_one,
        '2': Locators.number_two,
        '3': Locators.number_three,
        '4': Locators.number_four,
        '5': Locators.number_five,
        '6': Locators.number_six,
        '7': Locators.number_seven,
        '8': Locators.number_eight,
        '9': Locators.number_nine,
        '+': Locators.add_operation,
        '-': Locators.subtract_operation,
        '*': Locators.multiply_operation,
        '/': Locators.divide_operation,
        '^': Locators.power_operation,
    }

    for digit in str(number_str):
        locators.append(locators_map.get(digit))

    return locators
