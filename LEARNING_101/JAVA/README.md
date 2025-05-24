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



# Java String Pool

The **String Pool** (also known as the **String Literal Pool**) is a special area in the Java heap memory that stores **literal** `String` instances. It helps save memory by reusing immutable `String` objects.

---

## 1. Why a String Pool?

- **Immutability**: Java `String`s are immutable. Once created, their value cannot change.
- **Memory efficiency**: Many identical string literals often appear in code. Pooling avoids multiple copies.
- **Performance**: Reusing pooled strings reduces object creation and garbage collection overhead.

---

## 2. How It Works

1. **Compile time**: When the compiler sees a string literal (e.g. `"Hello"`), it adds it to the pool.
2. **Runtime**:  
   - If code refers to a literal, JVM checks the pool:
     - **Exists** → returns reference from pool.
     - **Not exist** → creates new `String` in pool, then returns it.

---

## 3. String Creation: Literal vs `new`

```java
String s1 = "Java";          // literal → added to pool
String s2 = "Java";          // reuses pooled "Java"
String s3 = new String("Java");  
// new String(...) always creates a new object on the heap (outside pool)
```

- `s1 == s2` → `true` (same pooled reference)  
- `s1 == s3` → `false` (different heap object)

---

## 4. `intern()` Method

You can manually intern a `String` to the pool:

```java
String heapStr = new String("Hello");
String pooled = heapStr.intern(); 
// pooled now refers to the pooled "Hello" literal
```

- If `"Hello"` was already in the pool, `intern()` returns existing reference.
- Otherwise, it adds `heapStr`’s content to the pool and returns its reference.

---

## 5. Memory Layout

```
+------------------+      +--------------------+
| String Literal   | ---> | "Hello, World!"    |
| Pool (in Heap)   |      +--------------------+
+------------------+
          ^
          |   
      compile-time   
```

- **Heap**: Contains the String pool and other objects.
- **Metaspace** / **PermGen** (pre-Java 8): Stored the *class* definitions, not string data.

---

## 6. Best Practices

- **Prefer literals** when you have known, repeated `String` values.
- **Avoid** unnecessary `new String(...)` calls unless you explicitly need a distinct object.
- **Use** `intern()` sparingly for large sets of dynamic strings to avoid pool bloat.

---

## 7. Example

```java
public class StringPoolDemo {
    public static void main(String[] args) {
        String a = "foo";
        String b = "f" + "o" + "o";     // compile-time concatenation → "foo" literal
        String c = new String("foo");   // new object
        String d = c.intern();          // pooled reference

        System.out.println(a == b); // true
        System.out.println(a == c); // false
        System.out.println(a == d); // true
    }
}
```

---

**Key Takeaway:**  
The String Pool leverages Java’s immutable `String` design to reduce memory footprint and improve performance by reusing literal instances. Understanding and using it correctly can help you write more efficient Java code.


# Java StringBuffer and StringBuilder

The **StringBuffer** and **StringBuilder** classes are mutable sequence of characters in Java. They are alternatives to the immutable `String` class when you need to modify or build strings dynamically.

---

## 1. Overview

- **Mutable**: Both allow modification without creating new objects each time.
- **Thread Safety**:  
  - `StringBuffer` is **synchronized** (thread-safe).  
  - `StringBuilder` is **not synchronized** (not thread-safe), offering better performance in single-threaded contexts.

---

## 2. StringBuffer

- **Package**: `java.lang`
- **Introduced**: Java 1.0
- **Synchronization**: All public methods are synchronized.
- **Typical Use Case**: Multi-threaded applications where thread safety is required.

### Key Constructors
```java
StringBuffer sb1 = new StringBuffer();              // default capacity 16
StringBuffer sb2 = new StringBuffer("Hello");       // capacity = 16 + length of string
```

### Common Methods
- `append(...)`  
- `insert(int offset, ...)`  
- `replace(int start, int end, String str)`  
- `delete(int start, int end)`  
- `reverse()`  
- `capacity()` / `ensureCapacity(int minimumCapacity)`  

```java
StringBuffer sb = new StringBuffer("Java");
sb.append(" Buffer");
System.out.println(sb); // Java Buffer
```

---

## 3. StringBuilder

- **Package**: `java.lang`
- **Introduced**: Java 5
- **Synchronization**: Not synchronized.
- **Typical Use Case**: Single-threaded applications or local string manipulations where performance matters.

### Key Constructors
```java
StringBuilder sb1 = new StringBuilder();            // default capacity 16
StringBuilder sb2 = new StringBuilder("Hello");     // capacity = 16 + length of string
```

### Common Methods
- `append(...)`  
- `insert(int offset, ...)`  
- `replace(int start, int end, String str)`  
- `delete(int start, int end)`  
- `reverse()`  
- `capacity()` / `ensureCapacity(int minimumCapacity)`  

```java
StringBuilder sb = new StringBuilder("Java");
sb.append(" Builder");
System.out.println(sb); // Java Builder
```

---

## 4. Key Differences

| Feature             | StringBuffer           | StringBuilder         |
|---------------------|------------------------|-----------------------|
| Thread Safety       | Synchronized (safe)    | Not synchronized      |
| Performance         | Slower due to locking  | Faster in single-threaded code |
| Introduced Version  | Java 1.0               | Java 5                |

---

## 5. Example: When to Use Which

```java
// Thread-safe usage
public class SafeString {
    private StringBuffer buffer = new StringBuffer();

    public void add(String s) {
        buffer.append(s);
    }
}

// High-performance single-threaded usage
public class FastString {
    public static void main(String[] args) {
        StringBuilder builder = new StringBuilder();
        for (int i = 0; i < 1000; i++) {
            builder.append(i);
        }
        System.out.println(builder);
    }
}
```

---

## 6. Best Practices

- Use **StringBuilder** by default for better performance.
- Switch to **StringBuffer** only when you need thread-safe mutable strings.
- Avoid mixing `String`, `StringBuilder`, and `StringBuffer` conversions unnecessarily.

---

**Key Takeaway:**  
Choose `StringBuilder` for most mutable string operations in single-threaded contexts and prefer `StringBuffer` when thread safety is a requirement.


# Thread Safety

In concurrent programming, **thread safety** means that a piece of code (method, class, or data structure) functions correctly when accessed by multiple threads simultaneously, without causing data corruption, unexpected behavior, or race conditions.

---

## 1. Why Thread Safety Matters

- **Concurrency**: Modern applications often perform many tasks in parallel to improve performance.  
- **Shared Resources**: When threads share mutable data (e.g., collections, counters, buffers), unsynchronized access can lead to inconsistent state.  
- **Reliability**: Thread-safe code guarantees predictable results regardless of thread scheduling.

---

## 2. Common Concurrency Hazards

1. **Race Conditions**  
   Two or more threads read and write shared data in an interleaved way, producing incorrect results.
2. **Visibility Issues**  
   Changes made by one thread may not be immediately visible to others due to CPU caching and memory reordering.
3. **Deadlocks**  
   Two or more threads wait indefinitely for locks held by each other.
4. **Livelocks and Starvation**  
   Threads remain active but fail to make progress due to repeated contention.

---

## 3. Techniques for Achieving Thread Safety

| Technique                  | Description                                                                 |
|----------------------------|-----------------------------------------------------------------------------|
| **`synchronized` blocks**  | Java keyword that acquires an object’s monitor for exclusive access.        |
| **Locks (java.util.concurrent.locks)** | More flexible lock implementations (e.g., `ReentrantLock`).       |
| **Immutable Objects**      | Objects whose state cannot change after creation (e.g., `String`).          |
| **Atomic Variables**       | Lock-free thread-safe single variables (e.g., `AtomicInteger`, `AtomicReference`). |
| **Thread-safe Collections**| Collections designed for concurrency (e.g., `ConcurrentHashMap`, `CopyOnWriteArrayList`). |
| **Volatile Fields**        | Ensures visibility of changes across threads without full locking.          |

---

## 4. Example: Synchronized Counter

```java
public class SafeCounter {
    private int count = 0;

    public synchronized void increment() {
        count++;
    }

    public synchronized int getCount() {
        return count;
    }
}
```


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


## Method Overloading

**Definition:**  
Method overloading is a feature of Java that allows a class to have more than one method with the same name, but different parameter lists. It is a form of compile-time (static) polymorphism.

**Rules:**
- Same method name  
- Different parameter type, number, or both  
- Return type can be same or different  
- Access modifiers can vary  
- Can throw different exceptions  

**Example:**
```java
public class MathUtils {
    public int add(int a, int b) {
        return a + b;
    }

    public double add(double a, double b) {
        return a + b;
    }

    public int add(int a, int b, int c) {
        return a + b + c;
    }
}
```

---

## Method Overriding

**Definition:**  
Method overriding occurs when a subclass provides a specific implementation for a method that is already defined in its superclass. It is a form of runtime (dynamic) polymorphism.

**Rules:**
- Same method name, return type, and parameter list  
- Subclass method must have same or more accessible visibility  
- Cannot override methods marked as `final`  
- Can throw same, narrower, or no exceptions, but not broader ones  
- `@Override` annotation is recommended  

**Example:**
```java
class Animal {
    public void makeSound() {
        System.out.println("Some sound");
    }
}

class Dog extends Animal {
    @Override
    public void makeSound() {
        System.out.println("Bark");
    }
}
```

---

## Dynamic Method Dispatch

**Definition:**  
Dynamic Method Dispatch is the mechanism by which a call to an overridden method is resolved at runtime rather than compile-time. It enables calling the subclass's method implementation through a superclass reference.

**How it works:**
- A superclass reference variable points to a subclass object.  
- At runtime, the JVM determines the actual object's type and invokes the appropriate overridden method.  

**Example:**
```java
class Animal {
    public void makeSound() {
        System.out.println("Some sound");
    }
}

class Dog extends Animal {
    @Override
    public void makeSound() {
        System.out.println("Bark");
    }
}

public class TestPolymorphism {
    public static void main(String[] args) {
        Animal myAnimal = new Dog(); // Superclass reference, subclass object
        myAnimal.makeSound();        // Prints "Bark"
    }
}
```

## The `final` Keyword in Java

The `final` keyword in Java is used to restrict the user. It can be applied to variables, methods, and classes.

---

## 1. Final Variables

- A **final variable** can be initialized only once.
- Must be initialized at the time of declaration or inside a constructor (for instance variables).
- After initialization, its value cannot change.

```java
public class Constants {
    public static final double PI = 3.1415926535; // Initialized at declaration

    private final int id; // Blank final instance variable

    public Constants(int id) {
        this.id = id; // Initialized in constructor
    }

    public void changeId() {
        // this.id = 10; // Compilation error: cannot assign a value to final variable id
    }
}
```

---

## 2. Blank Final Variables

- A **blank final variable** is a final variable not initialized at the point of declaration.
- Must be initialized in every constructor of the class.

```java
public class Employee {
    private final String name; // Blank final

    public Employee(String name) {
        this.name = name; // Mandatory initialization
    }
}
```

---

## 3. Final Methods

- A **final method** cannot be overridden by subclasses.
- Used to prevent altering method behavior in subclasses.

```java
class Animal {
    public final void eat() {
        System.out.println("Animal eats");
    }
}

class Dog extends Animal {
    // @Override
    // public void eat() {} // Compilation error: cannot override final method
}
```

---

## 4. Final Classes

- A **final class** cannot be subclassed.
- Often used for utility or immutable classes.

```java
public final class MathUtils {
    public static int add(int a, int b) {
        return a + b;
    }
}

// class AdvancedMath extends MathUtils {} // Compilation error: cannot subclass final class
```

---

## 5. Final Parameters

- A **final parameter** cannot be reassigned within the method body.
- Useful to prevent accidental modification.

```java
public void printMessage(final String message) {
    // message = "Hello"; // Compilation error: cannot assign a value to final parameter
    System.out.println(message);
}
```

---

## 6. Benefits of Using `final`

- **Immutability:** Helps create immutable classes.
- **Thread-safety:** Final fields are safely published after construction.
- **Clarity:** Indicates that values or behaviors should not change.
- **Security:** Prevents misuse by subclasses.

---

## 7. Summary

| Use Case                 | Effect                                    |
|--------------------------|-------------------------------------------|
| `final` variable         | Single assignment, constant behavior      |
| Blank final variable     | Assignment in constructor required        |
| `final` method           | Cannot be overridden                      |
| `final` class            | Cannot be subclassed                      |
| `final` parameter        | Parameter reassignment prohibited         |


## `java.lang.Object` Class in Java

The `Object` class is the root of the Java class hierarchy. Every class in Java implicitly inherits from `Object` if no other superclass is specified.

---

## 1. Declaration and Constructor

- **Declaration:**
  ```java
  public class Object {
      // ...
  }
  ```
- **Constructor:**
  ```java
  protected Object() { }
  ```
  - The constructor is `protected` to prevent direct instantiation except by subclasses.

---

## 2. Core Methods

### 2.1 `equals(Object obj)`
- **Signature:**  
  ```java
  public boolean equals(Object obj)
  ```
- **Default Behavior:**  
  Compares object references (i.e., `this == obj`).
- **Override Recommendation:**  
  When overriding, ensure consistency with `hashCode()`.

### 2.2 `hashCode()`
- **Signature:**  
  ```java
  public int hashCode()
  ```
- **Default Behavior:**  
  Returns a hash code based on the object’s memory address.
- **Contract:**  
  - If `a.equals(b)`, then `a.hashCode() == b.hashCode()`.  
  - Overriding `equals` should also override `hashCode`.

### 2.3 `toString()`
- **Signature:**  
  ```java
  public String toString()
  ```
- **Default Behavior:**  
  Returns a string in the format `ClassName@HashCodeInHex`.  
- **Override Recommendation:**  
  Provide a meaningful string representation of the object.

### 2.4 `getClass()`
- **Signature:**  
  ```java
  public final Class<?> getClass()
  ```
- **Behavior:**  
  Returns the runtime class of the object. The method is `final` and cannot be overridden.

---

## 3. Cloning and Finalization

### 3.1 `clone()`
- **Signature:**  
  ```java
  protected Object clone() throws CloneNotSupportedException
  ```
- **Behavior:**  
  Performs a field-by-field copy of the object.  
- **Usage:**  
  - Class must implement `Cloneable` interface.  
  - Often overridden with public visibility and deeper cloning logic.

### 3.2 `finalize()`
- **Signature:**  
  ```java
  protected void finalize() throws Throwable
  ```
- **Behavior:**  
  Called by the garbage collector before object reclamation.  
- **Deprecated:**  
  As of Java 9, `finalize()` is deprecated; use try-with-resources or cleaners instead.

---

## 4. Thread Coordination Methods

### 4.1 `wait()`, `wait(long timeout)`, `wait(long timeout, int nanos)`
- **Behavior:**  
  Causes the current thread to wait until notified or timeout expires.  
- **Usage:**  
  Must be called within a `synchronized` context on the object.

### 4.2 `notify()` and `notifyAll()`
- **Behavior:**  
  Wakes up one (`notify()`) or all (`notifyAll()`) threads waiting on the object’s monitor.  
- **Usage:**  
  Must be called within a `synchronized` context on the object.

---

## 5. Native Method Registration

- **`private static native void registerNatives()`**  
  Used internally to link native methods to JVM implementations.

---

## 6. Summary of Key Methods

| Method Signature                                   | Purpose                                        |
|----------------------------------------------------|------------------------------------------------|
| `protected Object()`                               | Constructor for subclasses                     |
| `public boolean equals(Object obj)`                | Reference equality (can be overridden)          |
| `public int hashCode()`                            | Hash code for hash-based collections            |
| `public String toString()`                         | String representation of the object             |
| `public final Class<?> getClass()`                 | Runtime class information (cannot override)     |
| `protected Object clone() throws CloneNotSupportedException` | Object cloning (requires `Cloneable`) |
| `protected void finalize() throws Throwable`        | Cleanup before GC (deprecated)                 |
| `public final void wait()` / overloads             | Thread waits for notification                   |
| `public final void notify()` / `notifyAll()`       | Thread notification                             |

---

## 7. Example Usage

```java
public class Person {
    private String name;

    public Person(String name) {
        this.name = name;
    }

    @Override
    public boolean equals(Object obj) {
        if (this == obj) return true;
        if (!(obj instanceof Person)) return false;
        Person other = (Person) obj;
        return name.equals(other.name);
    }

    @Override
    public int hashCode() {
        return name.hashCode();
    }

    @Override
    public String toString() {
        return "Person{name='" + name + "'}";
    }
}
```
