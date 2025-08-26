fn main() {
    println!("{}", is_even(10));
    let odd_number = 10;
    println!("{} ", !is_even(odd_number));
}

fn is_even(num: i32) -> bool {
    return num % 2 == 0;
}