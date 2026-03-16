# About
This is just a silly repo that consists of code generators in different languages to see if a number is even.

## Table of contents

### Interpreted languages:

1. [Python](#python-version)
2. [Perl](#perl-version)

### Compiled languages:
1. [C](#c-version)
2. [Rust](#rust-version)
3. [Pascal](#pascal-version)

## Python Version

### Generating the code

```sh
python python.py 10
```
If you want to run the generated script, run these commands instead:
- ```sh
  python python.py 10 > is_even.py
  ```
- ```sh
  python is_even.py
  ```

### Running the function directly

```py
x = 10
func = is_even(x, return_func=True) # This will return a callable than you can call
print(func()) # Call the function which prints 'True'
```

[(GO TO HOME)](#table-of-contents)

## Perl Version

> Make sure you have `perl` installed.

1. Run the script generator:

```sh
perl perl.pl - 5 > is_even.pl
```

> [!NOTE]
> The `-` symbol after the script is to pass the argument to the script.
> If you want to pass negative number. You can do something like this:
>
> ```sh
> perl perl.pl - -10 > is_even.pl
> ```

2. Run the generated script:

```sh
perl is_even.pl
# 0
```

[(GO TO HOME)](#table-of-contents)

---

## C Version


1. Compile:

```sh
gcc c_code.c -o c_code
```

2. Usage:

```sh
# Unix
./c_code 10 > is_even.c

# Windows
.\c_code.exe 10 > is_even.c
```

3. Compile that newly baked program:

```sh 
gcc is_even.c -o is_even
```

4. Check the result, is 10 even?:

```sh
# Unix
./is_even

# Windows
.\is_even.exe

# true
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
# Unix
./rust 10 > is_even.rs

# Windows
.\rust.exe 10 > is_even.rs
```

3. Compile that newly baked program:

```sh 
rustc is_even.rs
```

4. Check the result, is 10 even?:

```sh
# Unix
./is_even

# Windows
.\is_even.exe

# true
```

[(GO TO HOME)](#table-of-contents)

## Pascal Version

> I use fpc to compile. Use whatever free pascal compiler you have.

1. Compile:

```sh
fpc pascal.pp
```

2. Usage:

```sh
# Unix:
./pascal 9 > isEven.pp

# Windows:
.\pascal.exe 9 > isEven.pp
```

3. Compile the new isEven program:

```sh
fpc isEven.pp
```

4. Run it:

```sh
# Unix:
./isEven

# Windows:
.\isEven.exe

# FALSE
```

[(GO TO HOME)](#table-of-contents)

