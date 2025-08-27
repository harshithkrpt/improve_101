//At any given time, you can have either:

// One mutable reference (&mut), OR

// Any number of immutable references (&).
// → Never both at the same time.

// Mutable references cannot coexist with immutable ones for the same variable in the same scope.

// The reference must not outlive the variable it points to (lifetime rule).

// You can re-borrow immutably from a mutable reference, but not the other way around.

pub fn borrowing() {
    let message = String::from("Hello, Harshith!");
 
    print_message(&message);

    // We can still use message after the function call
    println!("Back in main: {}", message);
}


fn print_message(msg: &String) {
    println!("Inside function: {}", msg);
}

fn mutable_reference() {
    let mut name = String::from("Harshith");

    // ✅ Create a mutable reference
    let name_ref = &mut name;
    name_ref.push_str(" Krpt");  // modify through mutable ref
    println!("After mutation: {}", name_ref);

    // ❌ Not allowed: immutable borrow while mutable borrow exists
    // let immut_ref = &name;
    // println!("{}", immut_ref);

    // ✅ After mutable ref goes out of scope, we can use immutable refs
    {
        let immut1 = &name;
        let immut2 = &name;
        println!("Immutable refs: {}, {}", immut1, immut2);
    }

    // ✅ We can create a new mutable ref after immutables are done
    let new_mut_ref = &mut name;
    new_mut_ref.push_str(" 🚀");
    println!("Final value: {}", new_mut_ref);
}