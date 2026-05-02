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
        if number >= 0:
            candidates = []
            i = 0
            while i <= number:
                candidates = candidates + [i]
                i += 1
            for c in candidates:
                parity = False
                j = abs(c)
                while j:
                    parity = not parity
                    j -= 1
                yield c, parity
        else:
            candidates = []
            i = number
            while i < 1:
                candidates = candidates + [i]
                i += 1
            for c in candidates:
                parity = False
                j = abs(c)
                while j:
                    parity = not parity
                    j -= 1
                yield c, parity

    if not print_code and not return_func:
        raise ValueError("You must either print the generated code or return a function (set `print_code` with `-pc`/`--print-code` or `return_func` with `-rf`/`--return-function`z    ).")

    if return_func:
        code_str = ""
        code_str += "def __private_is_even_code_generator():\n"
        code_str += f"  {variable_name} = {number}\n"
        for candidate, is_even_flag in custom_enum(number):
            code_str = code_str + (f"  if {variable_name} == {candidate}: return {is_even_flag}\n")
        namespace = {}
        exec(code_str, namespace)
        exec(code_str, namespace)
        return namespace["__private_is_even_code_generator"]
    else:
        code_str = ""
        code_str += f"{variable_name} = {number}\n"
        code_str += "is_even = False\n"
        for candidate, is_even_flag in custom_enum(number):
            code_str = code_str + (f"if {variable_name} == {candidate}: is_even = {is_even_flag}\n")
        code_str = code_str + "print(is_even)\n"

    if print_code:
        print("\n".join(code_str.splitlines()))

    if return_func:
        namespace = {}
        exec("\n".join(code_str.splitlines()), namespace)
        return namespace["__private_is_even_code_generator"]


def main():
    args = parser.parse_args()

    for number in args.numbers:
        s = str(number)
        n = int(s)
        is_even(n, print_code=(not args.dont_print_code), return_func=args.return_function)


if __name__ == "__main__":
    main()
    