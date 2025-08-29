pub fn string_ex() {
    // store "Harshith"
    // add "Kurapati"  to it
    // print "Harshith Kurapati"
    let mut s1 = String::from("Harshith");
    s1.push_str(" Kurapati");
    println!("{}", s1);
    // now remove "Kurapati"
    s1.remove(8..s1.len());
    println!("{}", s1);
}

// slice
pub fn string_slice() {
    let s1 = String::from("Hello, world!");
    let hello = &s1[0..5]; // slice for "Hello"
    let world = &s1[7..12]; // slice for "world"
    println!("{} {}", hello, world);
    let first_word = find_first_word(&s1);
    println!("First word: {}", first_word);
}


fn find_first_word(s: &str) -> &str {
    let mut index = 0;
    for (_, &item) in s.chars().enumerate() {
        if item == ' ' {
            return &s[0..index];
        }
        index = index + 1;
    }
}

// string literal
pub fn string_literal() {
    let s = "Hello, world!"; // string literal
    println!("{}", s);
}