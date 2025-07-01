# 🧱 Low-Level Design (LLD) Principles

Low-Level Design focuses on designing class structures, interactions, and detailed architecture that is **readable**, **extensible**, and **correct**. These principles are crucial in interviews and real-world software engineering.

---

## 📖 1. Readability

> _"Code is read much more often than it is written." – Robert C. Martin_

### Why It Matters:
- Readable code reduces onboarding time for new developers.
- Easier to debug, maintain, and refactor.
- Clean code improves collaboration and code review efficiency.

### Best Practices:
- Use meaningful class and method names.
- Follow consistent indentation and formatting.
- Keep methods short and focused (Single Responsibility Principle).
- Avoid deep nesting; use guard clauses where possible.
- Add minimal but clear comments only where necessary.

🔺 **Note:** In interviews, unreadable code—even if functionally correct—can negatively impact your evaluation.

---

## 🔧 2. Extensibility

> _"Design for change. Your code should welcome new features, not break under them."_

### Why It Matters:
- Software requirements evolve frequently.
- Engineering standards and business rules change over time.

### Best Practices:
- Apply **Open/Closed Principle**: code should be open for extension, closed for modification.
- Use **interfaces** or **abstract classes** for polymorphism.
- Prefer **composition** over inheritance for flexibility.
- Apply **design patterns** where appropriate (e.g., Strategy, Factory).
- Avoid hardcoding logic that may need to evolve.

💡 **Example:** Instead of using `if-else` for every payment method, use a `PaymentStrategy` interface.

---

## ✅ 3. Correctness

> _"Correctness is non-negotiable. Bugs in production can cost real money—or worse, trust."_

### Why It Matters:
- Production bugs are expensive and harmful to reputation.
- System reliability is critical in user-facing and backend systems.

### Best Practices:
- Follow **Test-Driven Development (TDD)** when feasible.
- Write **unit tests**, **integration tests**, and **failover handling**.
- Validate inputs and handle edge cases explicitly.
- Log meaningful errors, not stack traces alone.
- Maintain **backups**, **circuit breakers**, and **retry mechanisms** in critical flows.

⚠️ **Tip:** Prioritize correctness over cleverness. Simpler, well-tested code is better than complex logic that’s hard to verify.

---

## ✅ Summary Table

| Principle     | Goal                               | Key Practices                                                  |
|---------------|------------------------------------|----------------------------------------------------------------|
| Readability   | Easy to read, maintain, and review | Clean code, naming, SRP, minimal comments                     |
| Extensibility | Easy to adapt to future changes    | OCP, design patterns, composition, interface-based design     |
| Correctness   | Bug-free, reliable production code | TDD, validations, testing layers, error handling, observability |
