# 🧠 Java Data Types – Basic Theory

In Java, **data types** specify the kind of data a variable can hold. They are categorized into two main types:

---

### 1. Primitive Data Types

Java has **8 primitive data types** which are predefined by the language and named by a keyword.

| Type     | Description                            | Size        | Example              |
|----------|----------------------------------------|-------------|-----------------------|
| `byte`   | 8-bit signed integer                   | 1 byte      | `byte a = 100;`       |
| `short`  | 16-bit signed integer                  | 2 bytes     | `short s = 20000;`    |
| `int`    | 32-bit signed integer (default int)    | 4 bytes     | `int x = 10;`         |
| `long`   | 64-bit signed integer                  | 8 bytes     | `long l = 123456789L;`|
| `float`  | 32-bit floating point                  | 4 bytes     | `float f = 5.6f;`     |
| `double` | 64-bit floating point (default double) | 8 bytes     | `double d = 10.99;`   |
| `char`   | 16-bit Unicode character               | 2 bytes     | `char c = 'A';`       |
| `boolean`| true or false values                   | ~1 bit      | `boolean b = true;`   |

---

### 2. Non-Primitive (Reference/Object) Data Types

These refer to objects and include:

- **Strings** – e.g., `String name = "Java";`
- **Arrays** – e.g., `int[] arr = {1, 2, 3};`
- **Classes** – e.g., `Car myCar = new Car();`
- **Interfaces** and **Enums**

**Key Differences from Primitive Types:**

- Stored as references (memory address).
- Can be `null`.
- Provide built-in methods (e.g., `name.length()` for Strings).

---

### 🧾 Notes

- Java is **statically typed**, so every variable must be declared with a type.
- **Default values** exist for primitives (e.g., `int` → `0`, `boolean` → `false`).
- Use **wrapper classes** like `Integer`, `Double`, etc., to work with primitives as objects (e.g., in collections).


## 🔁 Type Casting in Java (Primitive Data Types)

**Type casting** is the process of converting one data type into another. In Java, it applies to **compatible data types only** and is of two types:

---

### 1. Implicit Type Casting (Widening Conversion)

- Automatically done by Java.
- Converts a smaller type to a larger type (no data loss).
- Example: `byte` → `short` → `int` → `long` → `float` → `double`

#### ✅ Example:
```java
int x = 100;
double y = x; // int to double (automatic)
System.out.println(y); // Output: 100.0
```


```java
double a = 9.7;
int b = (int) a; // double to int (manual)
System.out.println(b); // Output: 9 (fraction lost)


int big = 130;
byte small = (byte) big;
System.out.println(small); // Output: -126 (due to overflow)
char c = 'A';
int ascii = (int) c; // 65
char again = (char) 66; // 'B'
System.out.println(ascii); // 65
System.out.println(again); // B


```

| From Type | To Type  | Casting Type | Example                    |
| --------- | -------- | ------------ | -------------------------- |
| `int`     | `double` | Implicit     | `double d = intVal;`       |
| `double`  | `int`    | Explicit     | `int i = (int) doubleVal;` |
| `char`    | `int`    | Implicit     | `int ascii = c;`           |
| `int`     | `char`   | Explicit     | `char c = (char) i;`       |


## 📈 Type Promotion in Java

**Type promotion** is a process where smaller data types are automatically promoted to larger types during operations to prevent data loss.

---

### 🔧 When It Happens

1. In expressions with different data types.
2. During arithmetic calculations.
3. When assigning to a larger compatible type.

---

### 🔁 Promotion Rules

- `byte`, `short`, `char` → automatically promoted to `int`
- If one operand is `long` → result is `long`
- If one operand is `float` → result is `float`
- If one operand is `double` → result is `double`

---

### 🧪 Examples

#### 1. `byte` to `int`
```java
byte a = 10;
byte b = 20;
// byte c = a + b; // Compile error
int c = a + b;     // Works because of promotion to int
```

## 🔣 Java Operators: Assignment, Relational, Logical

Java provides various operators to perform operations on variables and values. Here, we'll focus on:

- Assignment Operators
- Relational (Comparison) Operators
- Logical Operators

---

### 🟢 1. Assignment Operators

Used to assign values to variables.

| Operator | Description              | Example                |
|----------|--------------------------|----------------        |
| `=`      | Assign                   | `a = 10`               |
| `+=`     | Add and assign           | `a += 5` → `a = a + 5` |
| `-=`     | Subtract and assign      | `a -= 3` → `a = a - 3` |
| `*=`     | Multiply and assign      | `a *= 2` → `a = a * 2` |
| `/=`     | Divide and assign        | `a /= 4` → `a = a / 4` |
| `%=`     | Modulus and assign       | `a %= 3` → `a = a % 3` |

#### ✅ Example:
```java
int x = 10;
x += 5; // x becomes 15


```

### 🔵 Relational Operators

| Operator | Description           | Example  | Result     |
| -------- | --------------------- | -------- | ---------- |
| `==`     | Equal to              | `a == b` | true/false |
| `!=`     | Not equal to          | `a != b` | true/false |
| `>`      | Greater than          | `a > b`  | true/false |
| `<`      | Less than             | `a < b`  | true/false |
| `>=`     | Greater than or equal | `a >= b` | true/false |
| `<=`     | Less than or equal    | `a <= b` | true/false |

```java
int a = 10, b = 20;
System.out.println(a < b); // true
System.out.println(a == b); // false

```


### 🟠 3. Logical Operators

| Operator | Description | Example           | Result            |         |   |         |                     |
| -------- | ----------- | ----------------- | ----------------- | ------- | - | ------- | ------------------- |
| `&&`     | Logical AND | `a > 5 && a < 10` | true if both true |         |   |         |                     |
| \|\|`       |             | \`                | Logical OR        | \`a > 5 |   | a < 3\` | true if one is true |
| `!`      | Logical NOT | `!(a > 5)`        | inverts result    |         |   |         |                     |


```java
    int a = 8;
    System.out.println(a > 5 && a < 10); // true
    System.out.println(a < 5 || a > 10); // false
    System.out.println(!(a == 8));       // false

```


## 🔀 Conditional Statements in Java

Conditional statements in Java are used to execute blocks of code based on specific conditions. They control the **flow of execution** in your program.

---

### 🧱 Types of Conditional Statements

1. `if` statement  
2. `if-else` statement  
3. `if-else-if` ladder  
4. `switch` statement  
5. Ternary operator `? :`

---

### ✅ 1. `if` Statement

Executes a block of code if the condition is `true`.

#### Syntax:
```java
if (condition) {
    // code to execute
}
```

#### Example:
```java
int age = 20;
if (age >= 18) {
    System.out.println("You are eligible to vote.");
}
```

---

### ✅ 2. `if-else` Statement

Executes one block if condition is `true`, another if `false`.

#### Syntax:
```java
if (condition) {
    // true block
} else {
    // false block
}
```

#### Example:
```java
int number = 5;
if (number % 2 == 0) {
    System.out.println("Even");
} else {
    System.out.println("Odd");
}
```

---

### ✅ 3. `if-else-if` Ladder

Multiple conditions can be checked sequentially.

#### Syntax:
```java
if (condition1) {
    // block 1
} else if (condition2) {
    // block 2
} else {
    // default block
}
```

#### Example:
```java
int marks = 75;
if (marks >= 90) {
    System.out.println("Grade A");
} else if (marks >= 75) {
    System.out.println("Grade B");
} else {
    System.out.println("Grade C");
}
```

---

### ✅ 4. `switch` Statement

Best for multiple constant value checks.

#### Syntax:
```java
switch (expression) {
    case value1:
        // block
        break;
    case value2:
        // block
        break;
    default:
        // default block
}
```

#### Example:
```java
int day = 3;
switch (day) {
    case 1:
        System.out.println("Monday");
        break;
    case 2:
        System.out.println("Tuesday");
        break;
    case 3:
        System.out.println("Wednesday");
        break;
    default:
        System.out.println("Invalid day");
}
```

---

### ✅ 5. Ternary Operator (`? :`)

Shortcut for `if-else` that returns a value.

#### Syntax:
```java
variable = (condition) ? value_if_true : value_if_false;
```

#### Example:
```java
int a = 10, b = 20;
int max = (a > b) ? a : b;
System.out.println("Max: " + max);
```

---

### 📌 Use Cases

- Making decisions based on user input.
- Validating conditions before executing logic.
- Replacing complex `if-else` ladders with `switch` or ternary when applicable.



## 🔁 Loops in Java

Loops in Java are used to execute a block of code repeatedly until a specified condition is met.

---

### 🧱 Types of Loops

1. `for` loop  
2. `while` loop  
3. `do-while` loop  
4. Enhanced `for` loop (for arrays/collections)

---

### ✅ 1. `for` Loop

Used when the number of iterations is known.

#### Syntax:
```java
for (initialization; condition; update) {
    // code block
}
```

#### Example:
```java
for (int i = 1; i <= 5; i++) {
    System.out.println(i);
}
```

---

### ✅ 2. `while` Loop

Used when the number of iterations is unknown and depends on a condition.

#### Syntax:
```java
while (condition) {
    // code block
}
```

#### Example:
```java
int i = 1;
while (i <= 5) {
    System.out.println(i);
    i++;
}
```

---

### ✅ 3. `do-while` Loop

Similar to `while`, but ensures the loop runs **at least once**.

#### Syntax:
```java
do {
    // code block
} while (condition);
```

#### Example:
```java
int i = 1;
do {
    System.out.println(i);
    i++;
} while (i <= 5);
```

---

### ✅ 4. Enhanced `for` Loop (For-Each)

Used for iterating over arrays or collections.

#### Syntax:
```java
for (type var : array) {
    // code block
}
```

#### Example:
```java
int[] numbers = {1, 2, 3, 4, 5};
for (int num : numbers) {
    System.out.println(num);
}
```

---

### 🔄 Loop Control Statements

| Keyword   | Description                                     |
|-----------|-------------------------------------------------|
| `break`   | Exits the loop immediately                      |
| `continue`| Skips the current iteration and continues       |

#### Example:
```java
for (int i = 1; i <= 5; i++) {
    if (i == 3) continue;
    System.out.println(i);
}
```

---

### 📌 Use Cases

- Automating repetitive tasks
- Iterating over data structures
- Validating input until correct



## Java: `super`, Constructors, and Inheritance

### 🧠 What is `super` in Java?

The `super` keyword in Java is used to:

1. Access **parent class methods** (even if overridden).
2. Access **parent class constructors**.
3. Access **parent class variables** (if shadowed by child class variables).

---

### 🧱 Constructors in Java

#### Constructor Basics

- A constructor is a special method used to **initialize objects**.
- It has the **same name as the class**.
- It has **no return type** (not even `void`).
- If no constructor is defined, Java provides a **default constructor**.

#### Types of Constructors

1. **Default Constructor**
   ```java
   class Animal {
       Animal() {
           System.out.println("Animal created");
       }
   }
   ```

2. **Parameterized Constructor**
   ```java
   class Animal {
       Animal(String name) {
           System.out.println("Animal name: " + name);
       }
   }
   ```

---

### 🧬 Using `super()` in Constructors

#### Why use `super()`?

- To explicitly **call the parent class constructor**.
- Must be the **first line** in the child class constructor.

#### Example

```java
class Animal {
    Animal() {
        System.out.println("Animal constructor called");
    }
}

class Dog extends Animal {
    Dog() {
        super(); // Calls Animal()
        System.out.println("Dog constructor called");
    }
}
```

**Output:**
```
Animal constructor called
Dog constructor called
```

#### With Parameters

```java
class Animal {
    Animal(String name) {
        System.out.println("Animal name: " + name);
    }
}

class Dog extends Animal {
    Dog() {
        super("Buddy"); // Call parent class constructor with parameter
        System.out.println("Dog is ready");
    }
}
```

---

### 💡 Notes

- If you **don't call `super()`**, Java **implicitly calls the no-arg constructor** of the parent.
- If the **parent does not have a no-arg constructor**, you **must** explicitly call a parameterized constructor using `super(...)`.

---

### 📌 Accessing Parent Members

```java
class Animal {
    int age = 10;

    void show() {
        System.out.println("Animal age: " + age);
    }
}

class Dog extends Animal {
    int age = 5;

    void display() {
        System.out.println("Dog age: " + age);
        System.out.println("Animal age: " + super.age); // Access parent class variable
        super.show(); // Call parent class method
    }
}
```

---

### ✅ Best Practices

- Use `super()` for **constructor chaining**.
- Use `super.method()` to **reuse parent class logic**.
- Avoid overusing `super` in deeply nested inheritance to maintain readability.


## Java: `this` Keyword

### 📌 What is `this` in Java?

The `this` keyword is a reference variable in Java that refers to the **current object**.

---

### 🔑 Uses of `this` Keyword

#### 1. To refer current class instance variable

Used when **instance variables** and **parameters** have the same name.

```java
class Student {
    int id;
    String name;

    Student(int id, String name) {
        this.id = id;
        this.name = name;
    }
}
```

---

#### 2. To invoke current class method

```java
class Test {
    void show() {
        System.out.println("Show called");
    }

    void display() {
        this.show();  // same as calling show()
    }
}
```

---

#### 3. To invoke current class constructor

Used for **constructor chaining**.

```java
class Book {
    int pages;
    String title;

    Book() {
        this("Unknown", 100);  // Calls parameterized constructor
    }

    Book(String title, int pages) {
        this.title = title;
        this.pages = pages;
    }
}
```

---

#### 4. To pass as argument in method call

```java
class A {
    void methodA(A obj) {
        System.out.println("Method called");
    }

    void call() {
        methodA(this); // Passing current object
    }
}
```

---

#### 5. To return current class instance

```java
class Demo {
    Demo getDemo() {
        return this;
    }
}
```

---

### 💡 Notes

- `this` is **not static** — it cannot be used inside static methods.
- Mostly used to avoid ambiguity or enable fluent/chained method calls.

---

### ✅ Best Practices

- Use `this` to make code **more readable and maintainable**.
- Use it **only when necessary** to resolve ambiguity or for chaining.


## 🔍 Core OOPs Concepts in Java

Object-Oriented Programming (OOPs) is a programming paradigm based on the concept of "objects". Java is inherently an object-oriented language.

---

## 1. ✅ **Class and Object**

- **Class**: Blueprint for creating objects.
- **Object**: Instance of a class.

```java
class Car {
    String color;
    void drive() {
        System.out.println("Driving...");
    }
}

public class Main {
    public static void main(String[] args) {
        Car c1 = new Car();
        c1.drive();
    }
}
```

---

## 2. 🔒 **Encapsulation**

- Wrapping data (variables) and code (methods) together as a single unit.
- Achieved using **private variables** and **public getters/setters**.

```java
class Student {
    private int age;

    public void setAge(int a) {
        age = a;
    }

    public int getAge() {
        return age;
    }
}
```

---

## 3. 🧬 **Inheritance**

- Mechanism where one class acquires properties of another.
- Uses `extends` keyword.

```java
class Animal {
    void eat() {
        System.out.println("Eating...");
    }
}

class Dog extends Animal {
    void bark() {
        System.out.println("Barking...");
    }
}
```

---

## 4. 🎭 **Polymorphism**

Means many forms. Two types:

### a. Compile-Time (Method Overloading)

```java
class MathUtil {
    int add(int a, int b) {
        return a + b;
    }

    double add(double a, double b) {
        return a + b;
    }
}
```

### b. Run-Time (Method Overriding)

```java
class Animal {
    void sound() {
        System.out.println("Animal sound");
    }
}

class Dog extends Animal {
    void sound() {
        System.out.println("Dog barks");
    }
}
```

---

## 5. 🧩 **Abstraction**

- Hiding internal details and showing only essential features.
- Achieved using **abstract classes** or **interfaces**.

```java
abstract class Shape {
    abstract void draw();
}

class Circle extends Shape {
    void draw() {
        System.out.println("Drawing Circle");
    }
}
```

---

## 6. 🧱 **Interface**

- Used to achieve **100% abstraction**.
- All methods in interface are abstract by default.

```java
interface Drawable {
    void draw();
}

class Rectangle implements Drawable {
    public void draw() {
        System.out.println("Drawing Rectangle");
    }
}
```

---

## 💡 Summary Table

| Concept        | Description                                  |
|----------------|----------------------------------------------|
| Class          | Blueprint for creating objects               |
| Object         | Instance of a class                          |
| Encapsulation  | Binding data & code using access modifiers   |
| Inheritance    | Acquiring features from parent class         |
| Polymorphism   | One interface, many implementations          |
| Abstraction    | Hiding internal details                      |
| Interface      | Full abstraction using `interface` keyword   |