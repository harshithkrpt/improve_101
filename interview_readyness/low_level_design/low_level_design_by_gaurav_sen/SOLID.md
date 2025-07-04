
# SOLID Principles in Java with Simple and Advanced Use Cases

## 1. **Single Responsibility Principle (SRP)**

A class should have only one reason to change.

### ✅ Simple Use Case
```java
public class Invoice {
    private double amount;

    public Invoice(double amount) {
        this.amount = amount;
    }

    public double calculateTotal() {
        return amount * 1.18; // add tax
    }
}

public class InvoicePrinter {
    public void print(Invoice invoice) {
        System.out.println("Invoice Total: " + invoice.calculateTotal());
    }
}
```

### ✅ Advanced Use Case: Logging, Validation, and Emailing an Order
```java
public class Order {
    private List<String> items;

    public Order(List<String> items) {
        this.items = items;
    }

    public double calculateTotal() {
        return items.size() * 100.0;
    }
}

public class OrderValidator {
    public boolean isValid(Order order) {
        return order != null && !order.items.isEmpty();
    }
}

public class OrderLogger {
    public void log(Order order) {
        System.out.println("Order logged: " + order);
    }
}

public class OrderMailer {
    public void sendConfirmation(Order order) {
        System.out.println("Email sent for order!");
    }
}
```

---

## 2. **Open/Closed Principle (OCP)**

Software should be open for extension but closed for modification.

### ✅ Simple Use Case: Shape Drawing
```java
public interface Shape {
    void draw();
}

public class Circle implements Shape {
    public void draw() {
        System.out.println("Drawing Circle");
    }
}

public class Rectangle implements Shape {
    public void draw() {
        System.out.println("Drawing Rectangle");
    }
}

public class Canvas {
    public void render(List<Shape> shapes) {
        for (Shape shape : shapes) {
            shape.draw();
        }
    }
}
```

### ✅ Advanced Use Case: Pluggable Payment Systems
```java
public interface PaymentMethod {
    void pay(double amount);
}

public class CreditCardPayment implements PaymentMethod {
    public void pay(double amount) {
        System.out.println("Paid " + amount + " with Credit Card");
    }
}

public class PayPalPayment implements PaymentMethod {
    public void pay(double amount) {
        System.out.println("Paid " + amount + " via PayPal");
    }
}

public class PaymentProcessor {
    private final PaymentMethod method;

    public PaymentProcessor(PaymentMethod method) {
        this.method = method;
    }

    public void execute(double amount) {
        method.pay(amount);
    }
}
```

---

## 3. **Liskov Substitution Principle (LSP)**

Derived types must be completely substitutable for their base types.

### ✅ Simple Use Case:
```java
public class Vehicle {
    public void startEngine() {}
}

public class Car extends Vehicle {}
public class Truck extends Vehicle {}

public void testEngine(Vehicle v) {
    v.startEngine();  // Substitutable
}
```

### ✅ Advanced Use Case: Proper use of inheritance and composition
```java
public interface Bird {
    void layEggs();
}

public interface FlyingBird extends Bird {
    void fly();
}

public class Sparrow implements FlyingBird {
    public void layEggs() {}
    public void fly() {}
}

public class Ostrich implements Bird {
    public void layEggs() {}
}
```

---

## 4. **Interface Segregation Principle (ISP)**

Clients should not be forced to depend on methods they don't use.

### ✅ Simple Use Case:
```java
public interface Printer {
    void print();
}

public interface Scanner {
    void scan();
}

public class MultiFunctionPrinter implements Printer, Scanner {
    public void print() {}
    public void scan() {}
}
```

### ✅ Advanced Use Case: Segregated interfaces for machine functionalities
```java
public interface Fax {
    void fax(String content);
}

public class BasicPrinter implements Printer {
    public void print() {}
}

public class OfficePrinter implements Printer, Scanner, Fax {
    public void print() {}
    public void scan() {}
    public void fax(String content) {}
}
```

---

## 5. **Dependency Inversion Principle (DIP)**

High-level modules should not depend on low-level modules; both should depend on abstractions.

### ✅ Simple Use Case:
```java
public interface MessageService {
    void sendMessage(String msg);
}

public class EmailService implements MessageService {
    public void sendMessage(String msg) {
        System.out.println("Email: " + msg);
    }
}

public class Notification {
    private final MessageService service;

    public Notification(MessageService service) {
        this.service = service;
    }

    public void alert(String msg) {
        service.sendMessage(msg);
    }
}
```

### ✅ Advanced Use Case: Repository Pattern with Dependency Injection
```java
public interface CustomerRepository {
    void save(String customerName);
}

public class MySQLCustomerRepository implements CustomerRepository {
    public void save(String customerName) {
        System.out.println("Saved " + customerName + " to MySQL DB");
    }
}

public class CustomerService {
    private final CustomerRepository repo;

    public CustomerService(CustomerRepository repo) {
        this.repo = repo;
    }

    public void register(String name) {
        repo.save(name);
    }
}
```

---

## Summary Table

| Principle | Key Idea | Simple Example | Advanced Example |
|----------|----------|----------------|------------------|
| SRP | One responsibility per class | Invoice and Printer | Order validation, logging, emailing |
| OCP | Extend without modifying | Shapes | Payment systems |
| LSP | Replaceable subtype | Vehicle engine | Bird flight handling |
| ISP | Fine-grained interfaces | Printer/Scanner | Office devices |
| DIP | Abstraction dependency | Notification via service | Repository injection |
