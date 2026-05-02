from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from collections.abc import Callable

from argparse import ArgumentParser

def is_even(
    number: int,
    variable_name: str = "x",
    *,
    print_code: bool = True,
    return_func: bool = False,
) -> Callable[[], bool] | None:
    """
    Generates python if-else code that allows you to check if a number is even.

    Parameters
    ----------
    number: :class:`int`
        The number to check.
    variable_name: :class:`str` | `None`
        The variable used for the code generator when comparing. If `None`, the variable name `x` is used.
    print_code: :class:`bool`
        Whether to print the generated code. Defaults to `True`.
    return_func: :class:`bool`
        Whether to return a :class:`Callable` of the generated code. Defaults to `False`.

    Raises
    -------
    ValueError
        When both `print_code` and `return_func` are set to `False` as the function would essentially do nothing.

    Returns
    --------
        The :class:`Callable` which you can call and returns a :class:`bool` if `return_func` is set to `True`, else `None`
    """

    def _enumerate_odd_even(number: int):
        start = 0
        if number < 0:
            stop = number - 1
            step = -1
        else:
            stop = number + 1
            step = 1

        is_even_value: bool = True

        for value in range(start, stop, step):
            yield value, is_even_value
            is_even_value = not is_even_value

    if not print_code and not return_func:
        raise ValueError("You must either print the generated code or return a function.")

    if return_func:
        code = [
            "def __private_is_even_code_generator():",
            f"  {variable_name} = {number}",
        ]
        for i, value in _enumerate_odd_even(number):
            code.append(f"  if {variable_name} == {i}: return {value}")
    else:
        code = [f"{variable_name} = {number}\nis_even = False"]
        code.extend(f"if {variable_name} == {i}: is_even = {value}" for i, value in _enumerate_odd_even(number))
        code.append(f"print(is_even)\n\n")

    if print_code:
        print("\n".join(code))

    if return_func:
        namespace = {}
        exec("\n".join(code), namespace)
        return namespace["__private_is_even_code_generator"]


def main():
    parser = ArgumentParser()
    parser.add_argument(
        "numbers",
        nargs="+",
        type=int,
        help="One or more numbers to check.",
    )
    args = parser.parse_args()
    for number in args.numbers:
        is_even(number)


if __name__ == "__main__":
    main()
