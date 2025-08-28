use std::collections::HashMap;


pub fn vec() {
    let mut vector = Vec::new();
    vector.push(1);
    vector.push(10);
    println!("{:?}", vec);
}

fn vec2() {
    // 1️⃣ Create and add elements
    let mut numbers: Vec<i32> = Vec::new(); // empty vector of i32
    numbers.push(10); // add
    numbers.push(20);
    numbers.push(30);
    println!("After adding: {:?}", numbers);

    // 2️⃣ Removing elements
    numbers.pop(); // removes last element (30)
    println!("After pop: {:?}", numbers);

    numbers.remove(0); // removes element at index 0
    println!("After remove at index 0: {:?}", numbers);

    // 3️⃣ Get length
    println!("Length: {}", numbers.len());

    // 4️⃣ Type of vector
    let words = vec!["hello", "rust", "vector"]; // inferred as Vec<&str>
    println!("Words: {:?}, Type: Vec<&str>", words);

    // 5️⃣ Mutable reference using vector
    let mut values = vec![1, 2, 3];
    {
        let val_ref = &mut values[1]; // mutable borrow of index 1
        *val_ref = 42; // modify through mutable ref
    }
    println!("Modified vector: {:?}", values);

    // Accessing safely
    match values.get(2) {
        Some(val) => println!("Third element: {}", val),
        None => println!("No value at index 2"),
    }
}


fun hashmap_example() {
    // 1️⃣ Create and add elements
    let mut scores: HashMap<String, i32> = HashMap::new();
    scores.insert(String::from("Alice"), 50);
    scores.insert(String::from("Bob"), 70);
    scores.insert(String::from("Charlie"), 90);

    println!("After inserting: {:?}", scores);

    // 2️⃣ Removing elements
    scores.remove("Bob"); // remove key
    println!("After removing Bob: {:?}", scores);

    // 3️⃣ Get length
    println!("Length: {}", scores.len());

    // 4️⃣ Type of hashmap
    let mut fruit_stock = HashMap::from([
        ("Apple", 10),
        ("Banana", 20),
        ("Orange", 15),
    ]);
    println!("Fruit stock: {:?}, Type: HashMap<&str, i32>", fruit_stock);

    // 5️⃣ Mutable reference using hashmap
    if let Some(val) = fruit_stock.get_mut("Banana") {
        *val += 5; // increase stock
    }
    println!("Updated fruit stock: {:?}", fruit_stock);

    // Safe access
    match fruit_stock.get("Apple") {
        Some(val) => println!("Apple stock: {}", val),
        None => println!("No Apple found"),
    }

    // Iterating (key, value)
    for (key, val) in &fruit_stock {
        println!("{} -> {}", key, val);
    }
}