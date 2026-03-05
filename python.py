import sys
from typing import Callable


# Simple helper function
def _dprint(msg: str, colour: str) -> None:
    RESET = "\033[0m"
    colour = colour.casefold()
    colour_mapping = {
        "red": "\033[31m",
        "green": "\033[32m"
    }
    try:
        print(f"{colour_mapping[colour]}{msg}{RESET}")
    except KeyError:
        print(msg)


def is_even(
    number: int,
    variable_name: str = "x",
    *,
    print_code: bool = True,
    return_func: bool = False,
) -> Callable | None:
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
        When both `print_code` and `return_func` is set to `False` as the function would esentially do nothing.

    Returns
    --------
        The :class:`Callable` which you can call and returns a :class:`bool` if `return_func` is set to `True`, else `None`
    """

    def custom_enum(iterable):
        odd = True
        for _ in iterable:
            yield _, odd
            if not odd:
                odd = True
            else:
                odd = False

    if not print_code and not return_func:
        raise ValueError(
            "You have to either print or return a function, else it esentially does nothing."
        )

    if return_func:
        code = [
            "def __private_is_even_code_generator():",
            f"  {variable_name} = {number}",
        ]
        for i, value in custom_enum(range(number + 1)):
            ret = f"if {variable_name} == {i}: return {value}"
            code.append(f"  {ret}")
    else:
        code = [f"if {variable_name} == {i}: return {value}" for i, value in custom_enum(range(number + 1))]

    if print_code:
        print("\n".join(code))

    if return_func:
        namespace = {}
        exec("\n".join(code), namespace)
        return namespace["__private_is_even_code_generator"]


def main():
    args = sys.argv
    if len(args) < 2 or len(args) > 2:
        _dprint(f"Expected 2 args, got {len(args)} instead", "red")
        return
    
    num = args[1]
    try:
        num = int(num)
    except ValueError:
        _dprint(f"An Error Occurred: Expected an integer (5, 10, ...) got {num!r} instead. Example usage: 'python python.py 10'", "red")
        raise

    is_even(num)
    _dprint(f"\nSuccessfully generated is-even if-else code for the number: {num}", "green")


if __name__ == "__main__":
    main()
    