pub trait Summary {
    fn summarize(&self) -> String;
}

struct User {
    username: String,
    email: String,
}

struct Article {
    headline: String,
    location: String,
    content: String,
}

impl Summary for User {
    fn summarize(&self) -> String {
        format!("User: {}, Email: {}", self.username, self.email)
    }
}

impl Summary for Article {
    fn summarize(&self) -> String {
        format!("{}, located at {}, Content: {}", self.headline, self.location, self.content)
    }
}

// struct is implementing the trait which is similar to interface in other languages or abstract class in java


// traits as parameters -> under the hood, the below code is syntactic sugar for the commented code called as "trait bounds"
fn notify(item: impl Summary) {
    println!("Breaking news! {}", item.summarize());
}

// like below code which will be called as "trait bounds" using generics
pub fn notify_non_syntactic_sugar<T: Summary>(item: T) {
    println!("Breaking news! {}", item.summarize());
}