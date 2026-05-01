import sys
from collections.abc import Callable, Iterator

def is_even(
    number: int,
    variable_name: str | None = "x",
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

    def custom_enum(number: int) -> Iterator[tuple[int, bool]]:
        start = number if number < 0 else 0
        stop = 1 if number < 0 else number + 1
        is_even_value = start % 2 == 0

        for value in range(start, stop):
            yield value, is_even_value
            is_even_value = not is_even_value

    target_variable = "x" if variable_name is None else variable_name

    if not print_code and not return_func:
        raise ValueError(
            "You have to either print or return a function, else it essentially does nothing."
        )

    if return_func:
        code = [
            "def __private_is_even_code_generator():",
            f"  {target_variable} = {number}",
        ]
        for value, is_even_value in custom_enum(number):
            code.append(f"  if {target_variable} == {value}: return {is_even_value}")
    else:
        code = [f"{target_variable} = {number}\nis_even = False"]
        code.extend(
            f"if {target_variable} == {value}: is_even = {is_even_value}"
            for value, is_even_value in custom_enum(number)
        )
        code.append(f"print(is_even)")

    if print_code:
        print("\n".join(code))

    if return_func:
        namespace = {}
        exec("\n".join(code), namespace)
        return namespace["__private_is_even_code_generator"]


def main():
    args = sys.argv
    if len(args) != 2:
        print(f"Expected 2 args, got {len(args)} instead")
        return
    
    num = args[1]
    try:
        num = int(num)
    except ValueError:
        print(f"An Error Occurred: Expected an integer (5, 10, ...) got {num!r} instead. Example usage: 'python python.py 10'")
        raise

    is_even(num)


if __name__ == "__main__":
    main()
    