pub fn iterators() {
    let v1 = vec![1, 2, 3];

    let mut v1_iter = v1.iter();

    for val in v1_iter {
        println!("Got: {}", val);
    }

    v1_iter = v1.iter();

    while let Some(x) = v1_iter.next() {
        println!("Next: {}", x);
    }
}


// Iterating using a for loop
fn basic_iterator() {
    let v1 = vec![1, 2, 3];
    for val in v1 {
        println!("Got: {}", val);
    }

    // println!("{:?}", v1); // This would cause a compile-time error because v1 has been moved as for loop takes ownership as it internally uses into_iter()
}

// Using a iter() + for loop

fn using_for_loop() {
    let v1 = vec![1, 2, 3];
    for val in v1.iter() {
        println!("Got: {}", val);
    }
}


// Using next() + while let by borrowing an iterator with iter() 
fn using_while_let() {
    let v1 = vec![1, 2, 3];
    let mut v1_iter = v1.iter();
    while let Some(x) = v1_iter.next() {
        println!("Next: {}", x);
    }
}

// using mutable iterator
fn using_mutable_iterator() {
    let mut v1 = vec![1, 2, 3];
    let mut v1_iter = v1.iter_mut();
    while let Some(x) = v1_iter.next() {
        *x += 1;
        println!("Next: {}", x);
    }
}   

// using into_iter() to take ownership of the vector
fn using_into_iter() {
    let v1 = vec![1, 2, 3];
    let mut v1_iter = v1.into_iter();
    while let Some(x) = v1_iter.next() {
        println!("Next: {}", x);
    }

    println!("{:?}", v1); // This would cause a compile-time error because v1 has been moved
}

// Using iterator adaptors
// consumer iterators
fn using_iterator_adaptors() {
    let v1 = vec![1, 2, 3];
    let v1_iter = v1.iter();
    let sum = v1_iter.sum::<i32>();

    println!("Sum: {}", sum);

    // println!("{:?}", v1_iter); // This would cause a compile-time error because v1_iter has been moved
    println!("{:?}", v1); // This is fine because v1 was not moved
}

// defination of iterator adaptors
/*
An iterator adaptor is a method that takes an iterator as input and returns a new iterator as output, usually with some transformation applied to the elements of the original iterator. Iterator adaptors are lazy, meaning they do not perform any computation until the resulting iterator is consumed.

An Consumer adaptor is a method that takes an iterator as input and produces a final value or collection, consuming the iterator in the process. Consumer adaptors are eager, meaning they perform their computation immediately when called.
*/

// list of consumer adaptors
// sum, product, collect, fold, any, all, find, position, max, min, count  
// list of iterator adaptors
// map, filter, take, skip, enumerate, peekable, inspect, chain, zip


// Using map() iterator adaptor
fn using_map_iterator_adaptor() {
    let v1 = vec![1, 2, 3];
    let v1_iter = v1.iter();
    let v1_iter2: Vec<_> = v1_iter.map(|x| x + 1);
    println!("{:?}", v1_iter2);
}

// Using filter() iterator adaptor
fn using_filter_iterator_adaptor() {
    let v1 = vec![1, 2, 3, 4, 5, 6];
    let v1_iter = v1.iter();
    let v1_iter2 = v1_iter.filter(|x| *x % 2 == 0);
    println!("{:?}", v1_iter2);
}

// iterate odd values + double them + collect into a vector
fn using_chain_iterator_adaptor() {
    let v1 = vec![1, 2, 3, 4, 5, 6];
    let v1_iter = v1.iter();
    let new+vector: Vec<_> = v1_iter
        .filter(|x| *x % 2 != 0)
        .map(|x| x * 2)
        .collect();
    println!("{:?}", v1_iter2);
}

// iterators in hashmaps
use std::collections::HashMap;
fn using_iterators_in_hashmaps() {
    let mut scores = HashMap::new();
    scores.insert(String::from("Blue"), 10);
    scores.insert(String::from("Yellow"), 50);

    for (key, value) in &scores {
        println!("{}: {}", key, value);
    }

    let team_name = String::from("Blue");
    let score = scores.get(&team_name);
    match score {
        Some(s) => println!("Score for {}: {}", team_name, s),
        None => println!("No score for {}", team_name),
    }

    for (key, value) in scores.iter() {
        println!("{}: {}", key, value);
    }
}