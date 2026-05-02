from collections.abc import Callable

from argparse import ArgumentParser

parser = ArgumentParser()
parser.add_argument(
    "-dpc",
    "--dont-print-code",
    action="store_true",
    help="Disable printing the generated code; print by default.",
)
parser.add_argument(
    "-rf",
    "--return-function",
    action="store_true",
    help="Return a callable which performs the parity check instead of printing code.",
)
parser.add_argument(
    "-n",
    "--numbers",
    nargs="+",
    type=int,
    required=True,
    help="One or more numbers to check.",
)

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

    def custom_enum(number: int):
        # Simple, readable generation of (candidate, is_even) pairs.
        if number >= 0:
            for candidate in range(0, number + 1):
                yield candidate, (candidate % 2 == 0)
        else:
            for candidate in range(number, 1):
                yield candidate, (candidate % 2 == 0)

    if not print_code and not return_func:
        raise ValueError(
            "You must either print the generated code or return a function (set `print_code` or `return_func`)."
        )

    if return_func:
        code = ["def __private_is_even_code_generator():", f"  {variable_name} = {number}"]
        for candidate, is_even_flag in custom_enum(number):
            code.append(f"  if {variable_name} == {candidate}: return {is_even_flag}")
    else:
        code = [f"{variable_name} = {number}\nis_even = False"]
        code.extend(
            f"if {variable_name} == {candidate}: is_even = {is_even_flag}"
            for candidate, is_even_flag in custom_enum(number)
        )
        code.append("print(is_even)")

    if print_code:
        print("\n".join(code))

    if return_func:
        namespace = {}
        exec("\n".join(code), namespace)
        return namespace["__private_is_even_code_generator"]


def main():
    args = parser.parse_args()

    for number in args.numbers:
        is_even(number, print_code=(not args.dont_print_code), return_func=args.return_function)


if __name__ == "__main__":
    main()
    