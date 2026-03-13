# About
This is just a silly repo that consists of code generators in different languages to see if a number is even.

## Table of contents

1. [Python](#python-version)
2. [C](#c-version)
3. [Rust](#rust-version)

## Python Version

```python
# Through the command line
python python.py 10

# Calling the 'is_even' function directly
x = 10
func = is_even(x, return_func=True) # This will return a callable than you can call
print(func()) # Call the function which prints 'True'
```

[(GO TO HOME)](#table-of-contents)

## C Version

```c
// compile the code
gcc c_code.c -o is_even

// run the compiled code
.\is_even 10
```

[(GO TO HOME)](#table-of-contents)

## Rust Version

> Make sure you have `rustup` installed.

1. Compile:

```sh
rustc rust.rs
```

2. Usage:

```sh
./rust 10
```

It will output the code into the console.

Rediect it to a rust file:

```sh
./rust 10 > is_even.rs
```

3. Compile that newly baked program:

```sh 
rustc is_even.rs
```

4. Check the result, is 10 even?:

```sh
./is_even
# true
```

[(GO TO HOME)](#table-of-contents)

