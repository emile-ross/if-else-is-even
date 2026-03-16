/* Rust is a blazing fast and memory safe programming language
 *
 * Compilation:
 * $ rustc rust.rs
 *
 * Usage:
 * $ ./rust 10
 *
 * It will output the code into the console.
 * Rediect it to a rust file:
 * $ ./rust 10 > is_even.rs
 *
 * Compile that newly baked is_even program:
 * $ rustc is_even.rs
 *
 * Check the result, is 10 even?:
 * $ ./is_even
 * true
 */

use std::fmt::Write;

fn main() {
    let arg = std::env::args().nth(1)
        .expect("Please enter a number");
    let number: i32 = arg.parse()
        .expect("Invalid number");

    let mut output = String::new();

    output.push_str(     "fn main() {\n"                                  );
    writeln!(output,     "    let number: i32 = {};", number              ).unwrap();
    output.push_str(     "    let mut result = false;\n"                  );

    for n in 0..=number {
        writeln!(output, "    if number == {} {{", n                      ).unwrap();
        output.push_str( "        unsafe {\n"                             );
        output.push_str( "            let ptr: *mut bool = &mut result;\n");
        writeln!(output, "            *ptr = {};", n % 2 == 0             ).unwrap();
        output.push_str( "        }\n"                                    );
        output.push_str( "    }\n"                                        );
    }

    output.push_str(     "    println!(\"{}\", result);\n"                ); 
    output.push_str(     "}\n"                                            );

    println!("{}", output);
}

