INTEGER 
    - INT  - 4 BYTES
    - LONG - 8 BYTES
    - SHORT - 2 BYTE

    - BYTE - 1 BYTE
                    -2^7 TO 2^7
FLOAT  - 4 bytes.
DOUBLE - 8 bytes (default in JAVA).

```java
int name = 81;
double name = 723.238238232;
float numbe2 = 8.23f;
```

CHAR -> 2 Bytes
    -> Support Uniqcode 
    -> Has bigger range
    -> for character's we have to add single quotes
    
```java
    char c = 'k';
```

BOOLEAN -> true or false 
    -> In Java Boolean can only be assigned true or false , 


```java
    boolean b = true;
```



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
