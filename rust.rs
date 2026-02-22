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

fn main() {
    let arg = std::env::args().nth(1)
        .expect("Please enter a number");
    let number: i32 = arg.parse()
        .expect("Invalid number");

    println!("fn main() {{");
    println!("    let number: i32 = {};", number);
    println!("    let mut result = false;");

    for n in 0..=number {
        println!("    if number == {} {{", n);
        println!("        unsafe {{");
        println!("            let ptr: *mut bool = &mut result;");
        println!("            *ptr = {};", if n % 2 == 0 { "true" } else { "false" });
        println!("        }}");
        println!("    }}");
    }

    println!("    println!(\"{{}}\", result);"); 
    println!("}}");
}

