use std::fs;

struct User {
    active: bool,
    username: String,
    email: String,
    age: u64
}

struct ObjectRect {
    width: i32,
    height: i32
}

impl ObjectRect {
    fn area(&self) -> i32 {
        self.width * self.height
    }
    
    fn perimeter(&self) -> i32 {
        2 * (self.width + self.height)
    }

    fn static_method() -> String {
        return String::from("Hello");
    }
}

enum Direction {
    North,
    East,
    South,
    West
}
enum Shape {
    Rectange(f64, f64),
    Circle(f64)
}

enum CustomOption {
    Some(i32),
    None,
}


fn find_first_b(s: String) -> CustomOption {
    for (index, val) in s.chars().enumerate() {
        if val == 'b' {
            return CustomOption::Some(index as i32);
        }
    }

    return CustomOption::None;
}

fn main() {
    println!("{}", is_even(10));
    let odd_number = 10;
    println!("{} ", !is_even(odd_number));
    println!("fib of 10 is {}", fib(4));

    println!("Length {}", get_str_len(String::from("harshith")));

    let user1 = User {
        active: true,
        username: String::from("harshithkrpt"),
        email: String::from("harshith.kurapati@gmail.com"),
        age: 25
    }; 

    println!("{}", user1.email);
    println!("{} {}, {}", user1.active, user1.username, user1.age);

    let rect = ObjectRect {
        width: 10,
        height: 20
    };

    println!("{}", rect.area());
    println!("{}", ObjectRect::static_method());
    println!("{}", print_shape(Shape::Circle(12.2)));

    let has_b = String::from("preet");
    let ha = find_first_b(has_b);
    match ha {
        CustomOption::Some(val) => println!("{}", val),
        CustomOption::None => println!("nothing is foud")
    }
    

    let content = fs::read_to_string("./temp.txt");

    match content {
        Ok(val) => println!("{}", val),
        Err(err) => println!("{}", err)
    }
}



fn print_shape(shape: Shape) -> f64 {
    match shape {
        Shape::Rectange(a,b) => a * b,
        Shape::Circle(r) => 3.14 *  r * r,
    }
}

fn is_even(num: i32) -> bool {
    return num % 2 == 0;
}

fn fib(num: i32) -> i32 {
    let mut first = 0;
    let mut second = 1;

    if num == 0 {
        return first;
    }

    if num == 1 {
        return second;
    }

    for _ in 1..num-1 {
        let temp = second;
        second = first + second;
        first = temp;
    }

    return second;
}

fn get_str_len(str: String) -> usize {
    str.chars().count()
}