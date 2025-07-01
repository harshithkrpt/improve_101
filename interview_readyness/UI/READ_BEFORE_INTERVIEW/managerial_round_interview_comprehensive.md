# Managerial Round Interview Questions and Answers

Each entry includes a concise theory explanation and an illustrative example or approach.

---

## 1. How do you ensure your team delivers high-quality code within deadlines?
**Theory:** Implement coding standards, code reviews, CI pipelines, and clear timelines.  
**Example:**  
- Set up GitHub Actions to run linting and tests on every PR.  
- Daily stand-ups to track progress and flag blockers.

---

## 2. Describe a situation where you had to mentor a junior developer. How did you handle it?
**Theory:** Pair programming, constructive feedback, and setting growth goals.  
**Example:**  
- Scheduled weekly one-on-ones to review code and set learning objectives.  
- Provided resources (articles, courses) aligned with their interests.

---

## 3. Explain the SOLID principles and how you apply them in your designs?
**Theory:**  
- **S**ingle Responsibility  
- **O**pen/Closed  
- **L**iskov Substitution  
- **I**nterface Segregation  
- **D**ependency Inversion  
**Example:**  
- Use small, focused modules (SRP).  
- Depend on abstractions (interfaces) not concrete classes (DIP).

---

## 4. Explain design patterns in JavaScript
**Theory:** Reusable solutions to common problems (Module, Singleton, Observer).  
**Example (Module Pattern):**  
```js
const Logger = (function() {
  let instance;
  function create() {
    return {
      log: msg => console.log(msg)
    };
  }
  return {
    getInstance: function() {
      if (!instance) instance = create();
      return instance;
    }
  };
})();
```

---

## 5. How do you decide which tech stack is suitable for a specific project?
**Theory:** Evaluate project requirements, team expertise, scalability, and ecosystem.  
**Approach:**  
- List functional/non-functional requirements.  
- Rate stack options on criteria (performance, community support).  
- Prototype critical path features.

---

## 6. Difference between development, FT, UAT, pre-prod, and production environments
**Theory:**  
- **Dev:** Local development.  
- **FT (Functional Testing):** QA environment for feature tests.  
- **UAT:** User Acceptance Testing by stakeholders.  
- **Pre-Prod:** Mirror of production for final verification.  
- **Prod:** Live environment.

---

## 7. How do you ensure 100% code coverage in your projects?
**Theory:** Write unit and integration tests to cover all code paths.  
**Approach:**  
- Use coverage tools (Istanbul).  
- Enforce coverage thresholds in CI.  
- Review missing coverage badges on PRs.

---

## 8. Difference between unit, integration, and functional testing?
**Theory:**  
- **Unit:** Tests individual functions/modules.  
- **Integration:** Tests interactions between modules/services.  
- **Functional:** Tests end-to-end user flows.  
**Example:**  
- Unit: Jest test for a pure function.  
- Integration: Express route tested with Supertest.  
- Functional: Cypress E2E for UI flows.

---

## 9. How do you secure sensitive data in a MERN stack application?
**Theory:** Encryption at rest/in transit, environment variables, RBAC.  
**Approach:**  
- Store secrets in Vault or AWS Secrets Manager.  
- Use HTTPS/TLS and encrypt database fields (e.g., AES).

---

## 10. Describe your experience working in an Agile/Scrum environment
**Theory:** Iterative development, sprints, ceremonies (planning, stand-up, review, retro).  
**Example:**  
- Two-week sprints with sprint goals.  
- Regular backlog grooming sessions.

---

## 11. Explain sprint planning, daily standup, backlog, sprint review, sprint retrospective
**Theory & Process:**  
- **Planning:** Define sprint scope and tasks.  
- **Standup:** 15-min sync (What did I do? What's next? Blockers?).  
- **Backlog:** Prioritized feature list.  
- **Review:** Demo completed work.  
- **Retro:** Identify improvements for next sprint.

---

## 12. How do you document your code and project architecture?
**Theory:** Use inline comments, markdown docs, diagrams (C4/Ca).  
**Approach:**  
- Maintain `README.md` for project overview.  
- Use tools like PlantUML for architecture diagrams.

---

## 13. How do you onboard new developers to your team?
**Theory:** Provide clear documentation, mentorship, and starter tasks.  
**Example:**  
- Create a “Getting Started” doc with environment setup.  
- Pair them with a buddy for the first week.

---

## 14. What tools do you use to track project progress and manage tasks?
**Theory:** Use Jira, Trello, or Asana for issue tracking; Slack for communication.  
**Example:**  
- Jira epics, stories, and sub-tasks with clear acceptance criteria.

---

## 15. Key considerations when designing RESTful APIs
**Theory:**  
- Use proper HTTP verbs and status codes.  
- Versioning, pagination, filtering.  
**Example:**  
```
GET /api/v1/users?page=2&limit=20
```

---

## 16. Approach to deploying and scaling a MERN stack application
**Theory:** Use containerization, orchestration, and auto-scaling.  
**Example:**  
- Dockerize services, deploy on Kubernetes with HPA (Horizontal Pod Autoscaler).

---

## 17. Handling memory leaks in an application
**Theory:** Identify and fix via profiling and code reviews.  
**Approach:**  
- Use Chrome DevTools heap snapshots.  
- Ensure proper cleanup of event listeners and intervals.

---

## 18. Debugging React performance issues
**Theory:** Use React Profiler and DevTools to identify expensive renders.  
**Approach:**  
- Wrap components with `React.memo`.  
- Optimize state updates and avoid unnecessary renders.

---

## 19. Database bottleneck handling
**Theory:** Use indexing, caching, and query optimization.  
**Approach:**  
- Enable slow query logs.  
- Introduce Redis caching for frequent reads.

---

## 20. Guiding team through critical bugs
**Theory:** Triage systematically, reproduce, isolate root cause, test fix.  
**Approach:**  
- Host a debug session, assign roles (reader, driver, tester).

---

## 21. Code review approach
**Theory:** Focus on correctness, readability, and maintainability.  
**Checklist:**  
- Follow style guides.  
- Check edge cases and error handling.  
- Verify tests are updated.

---

## 22. Optimizing MongoDB queries for performance
**Theory:** Use indexes, projection, and aggregation with `$match` early.  
**Example:**  
```js
db.users.find({ active: true }, { projection: { password: 0 } });
```

---

## 23. Error handling in Express.js
**Theory:** Centralized error middleware, use try/catch in async handlers.  
```js
app.use(async (req, res, next) => {
  try {
    await someAsync();
    next();
  } catch (err) {
    next(err);
  }
});
```

---

## 24. Securing an Express.js API
**Theory:** Input validation, rate limiting, helmet for headers, CORS config.  
**Example:**  
```js
const helmet = require('helmet');
app.use(helmet());
```

---

## 25. Optimizing React applications for performance
**Theory:** Code-splitting, lazy loading, memoization, virtualization.  
**Approach:**  
- Use `React.lazy` for route-based chunks.  
- Optimize bundle size with Webpack.

---

## 26. Securing a Node.js application
**Theory:** Sanitize inputs, use Helmet, avoid eval, secure dependencies.  
**Approach:**  
- Run `npm audit` regularly.  
- Use CSP and secure cookies.

---

## 27. Database sharding and replication in MongoDB
**Theory:** Sharding distributes data across shards; replication provides fault tolerance.  
**Example:**  
```
sh.enableSharding("mydb");
db.users.createIndex({ _id: "hashed" });
```

---

