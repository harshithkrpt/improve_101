

# MongoDB 

- Collections & Documents

- a database has multiple collections.
- a collection has multiple documents which are kind of json objects stored as BSON -> Binary JSON.
- every document will have an _id which is a ObjectId("dsjdjds").
- document can have nested documents.


- below is the command to connect to mongodb shell 

```sh
mongosh
```

- show databases

```sh
show dbs
```

- use a specific database in mongodb shell

```sh
use bookstore
```
    - even if database does not exist it will switch

- clear screen

```sh
cls
```

- show all the collections in a database

```sh
show collections
```

- we can also write minor js code also like

```sh
var name = "my_name"
name 
name = "mario"
name # mario
```

- exit the terminal

```sh
exit
```

- to create a collection

```sh
db.books # will create a collection
```

- to insert a collection as document
    - insertOne is used to insert one document.
    - insertMany is used to insert many documents.

```sh
db.books.insertOne({
  name: "Mail System Design",
  author: "Harshith Kurapati",
  email: "harshith.krpt@gmail.com",
  tags: ["system-design", "email", "architecture"],
  publishedYear: 2024,
  rating: 4.5,
  available: true
})


db.books.insertMany([
  {
    name: "Understanding Algorithms",
    author: "Harshith Kurapati",
    email: "harshith.krpt@gmail.com",
    tags: ["algorithms", "data-structures", "interview-prep"],
    publishedYear: 2023,
    rating: 4.8,
    available: true
  },
  {
    name: "Learning MongoDB",
    author: "Kurapati Harshith",
    email: "harshithkurapati@gmail.com",
    tags: ["database", "nosql", "backend"],
    publishedYear: 2025,
    rating: 4.7,
    available: false
  },
  {
    name: "FastAPI in Action",
    author: "Harshith Kurapati",
    email: "harshith.krpt@gmail.com",
    tags: ["fastapi", "python", "api-design"],
    publishedYear: 2024,
    rating: 4.9,
    available: true
  }
])

```

- fetch the records from the collections

- find all the records

```sh
db.books.find()
```

- find a specific records

- below query matches all the queries matching rating 4.9
```sh
db.books.find({rating: 4.9})
```

- find all the records grater than 4.7 as rating

```sh
db.books.find({ rating: { $gt: 4.7  } })
```

- below are the simillar keys and its usecases

| **Operator**     | **Meaning / Use Case**                                        | **Example Query**                                                                           |
| ---------------- | ------------------------------------------------------------- | ------------------------------------------------------------------------------------------- |
| `$eq`            | Matches values equal to a specified value.                    | `{ age: { $eq: 25 } }` → finds docs where `age` is exactly 25                               |
| `$ne`            | Matches values **not equal** to a specified value.            | `{ status: { $ne: "active" } }`                                                             |
| `$gt`            | Greater than                                                  | `{ age: { $gt: 18 } }`                                                                      |
| `$gte`           | Greater than or equal to                                      | `{ age: { $gte: 18 } }`                                                                     |
| `$lt`            | Less than                                                     | `{ price: { $lt: 100 } }`                                                                   |
| `$lte`           | Less than or equal to                                         | `{ price: { $lte: 100 } }`                                                                  |
| `$in`            | Matches any value in an array                                 | `{ category: { $in: ["tech", "science"] } }`                                                |
| `$nin`           | Matches none of the values in an array                        | `{ category: { $nin: ["banned", "test"] } }`                                                |
| `$exists`        | Matches documents that have (or don’t have) a field           | `{ email: { $exists: true } }`                                                              |
| `$type`          | Matches field by BSON type                                    | `{ age: { $type: "int" } }`                                                                 |
| `$and`           | Combine multiple conditions (logical AND)                     | `{ $and: [ { age: { $gt: 20 } }, { age: { $lt: 40 } } ] }`                                  |
| `$or`            | Matches documents if **any** condition is true                | `{ $or: [ { status: "active" }, { age: { $lt: 25 } } ] }`                                   |
| `$nor`           | Opposite of `$or` (none of the conditions true)               | `{ $nor: [ { age: { $gt: 60 } }, { status: "inactive" } ] }`                                |
| `$not`           | Negates a condition                                           | `{ age: { $not: { $gt: 30 } } }` → means `age <= 30`                                        |
| `$regex`         | Pattern matching using Regular Expressions                    | `{ name: { $regex: /^H/, $options: "i" } }` → names starting with “H” (case-insensitive)    |
| `$all`           | Matches arrays containing **all** specified elements          | `{ tags: { $all: ["tech", "ai"] } }`                                                        |
| `$size`          | Matches arrays with a specific number of elements             | `{ tags: { $size: 3 } }`                                                                    |
| `$elemMatch`     | Matches array elements that satisfy multiple conditions       | `{ scores: { $elemMatch: { $gt: 80, $lt: 90 } } }`                                          |
| `$text`          | Performs a text search (requires text index)                  | `{ $text: { $search: "mongodb" } }`                                                         |
| `$mod`           | Matches numeric field divisible by a number                   | `{ age: { $mod: [5, 0] } }` → age divisible by 5                                            |
| `$where`         | Uses JavaScript expression (less recommended for performance) | `{ $where: "this.age > this.score" }`                                                       |
| `$geoWithin`     | Matches geometry within a certain shape                       | `{ location: { $geoWithin: { $centerSphere: [ [ 50, 50 ], 10 / 6378.1 ] } } }`              |
| `$geoIntersects` | Matches documents that intersect a GeoJSON geometry           | `{ location: { $geoIntersects: { $geometry: { type: "Point", coordinates: [ 1, 1 ] } } } }` |
| `$near`          | Finds points near a given coordinate (geospatial)             | `{ location: { $near: [50, 50] } }`                                                         |
| `$expr`          | Use aggregation expressions in filter                         | `{ $expr: { $gt: [ "$spent", "$budget" ] } }`                                               |



- get specific fields after the search we can do it using the second argument
- but we will get id even if we do not specify the id

```sh
db.books.find({
    rating: {
        $gt: 4.7
    }
}, {
    name: 1,
    rating: 1
})
```

- from everything filter few attributes

```sh
db.books.find({}, {
    name: 1,
    rating: 1
})
```


- we also have findOne -> which will fetch the 1st matching record

```sh
db.books.findOne({rating: {
        $gt: 4.7
    }})
```

- findOne with single record + few arguments

```sh
db.books.findOne({rating: {
        $gt: 4.7
    }}, {
        name: 1,
        rating: 1
    })
```

- find one by ObjectId

```sh
db.books.findOne({_id: ObjectId("690b7fe7c7dd79f0184f8804") })
```

- method chaining -> perform multiple operations once after the other taking previous result as the query for next method

```sh
db.books.find().count() # count the number of records
```

- limit chaining methods we can get how many records we to get back


```sh
db.books.find().limit(2)
```

```sh
(db.books.find().limit(2).count() == 2) == true
```

- sort the records in ascending order

```sh
db.books.find().sort({
    name: 1
})
```

- sort the records in descending order

```sh
db.books.find().sort({
    name: -1
})
```

```sh
db.books.find().sort({
    name: -1
}).limit(3)
```

- we can added nested documents like below

```sh
db.books.insertOne({
  name: "Mail System Design",
  author: "Harshith Kurapati",
  email: "harshith.krpt@gmail.com",
  tags: ["system-design", "email", "architecture"],
  publishedYear: 2024,
  rating: 4.5,
  available: true,
  reviews: [
    {
      reviewer: "Ananya Reddy",
      comment: "Excellent overview of system design principles.",
      rating: 5,
      date: ISODate("2024-02-15")
    },
    {
      reviewer: "Rahul Sharma",
      comment: "Good read, but could use more examples.",
      rating: 4,
      date: ISODate("2024-03-01")
    }
  ]
})

```

- querying the nested objects is like dot notation

```sh
db.books.find({ "reviews.reviewer": "Ananya Reddy" })
```


- operators 

### 📘 MongoDB Queries & Operators — Interview Guide

A complete, leveled guide for MongoDB queries from basic to advanced, focused on practical interview-style questions.

---

### ⚡ Level 1: Simple Comparison Operators

### `$gt` — Greater Than
Find books with rating greater than 4.5:
```js
db.books.find({ rating: { $gt: 4.5 } })
```

### `$lt` — Less Than
Find books published before 2022:
```js
db.books.find({ publishedYear: { $lt: 2022 } })
```

### `$gte` / `$lte` — Greater / Less Than or Equal
Find books with rating between 4.2 and 4.8:
```js
db.books.find({ rating: { $gte: 4.2, $lte: 4.8 } })
```

---

## 🧩 Level 2: Logical Operators

### `$and`
Find books with rating > 4 and published after 2022:
```js
db.books.find({ $and: [{ rating: { $gt: 4 } }, { publishedYear: { $gt: 2022 } }] })
```

### `$or`
Find books that are either about `frontend` or have rating above 4.8:
```js
db.books.find({ $or: [{ tags: "frontend" }, { rating: { $gt: 4.8 } }] })
```

### `$nor`
Find books that are *not* about frontend *and* have rating *not above* 4.5:
```js
db.books.find({ $nor: [{ tags: "frontend" }, { rating: { $gt: 4.5 } }] })
```

---

## 🧠 Level 3: Array Operators

### `$in` / `$nin`
Find books whose tags include *either* “frontend” or “system-design”:
```js
db.books.find({ tags: { $in: ["frontend", "system-design"] } })
```

Find books that don’t have those tags:
```js
db.books.find({ tags: { $nin: ["frontend", "system-design"] } })
```

### `$all`
Find books that include *both* “system-design” and “architecture”:
```js
db.books.find({ tags: { $all: ["system-design", "architecture"] } })
```

### `$size`
Find books that have exactly 3 tags:
```js
db.books.find({ tags: { $size: 3 } })
```

---

## 🧩 Level 4: Nested Documents & `$elemMatch`

Find books where any review has rating ≥ 5 and comment containing “Excellent”:
```js
db.books.find({
  reviews: {
    $elemMatch: {
      rating: { $gte: 5 },
      comment: /Excellent/i
    }
  }
})
```

---

## 🧭 Level 5: Pattern Matching & Existence

### `$regex`
Find books whose name starts with “Web” (case-insensitive):
```js
db.books.find({ name: { $regex: /^Web/i } })
```

### `$exists`
Find books that contain the `reviews` field:
```js
db.books.find({ reviews: { $exists: true } })
```

### `$type`
Find books where `rating` is of type number:
```js
db.books.find({ rating: { $type: "number" } })
```

---

## 🧩 Level 6: Updating and Array Modifiers

### `$push`
Add a new review to an existing book:
```js
db.books.updateOne(
  { name: "Web Performance Handbook" },
  { $push: { reviews: { reviewer: "Amit", rating: 4.5, comment: "Very practical" } } }
)
```

### `$inc`
Increase the rating of a book by 0.1:
```js
db.books.updateOne({ name: "Mail System Design" }, { $inc: { rating: 0.1 } })
```

### `$set` with Positional Operator `$`
Update the rating of a review by reviewer name:
```js
db.books.updateOne(
  { "reviews.reviewer": "Rahul Sharma" },
  { $set: { "reviews.$.rating": 4.3 } }
)
```

---

## 💣 Level 7: Advanced Filtering

### Combine `$and` with `$elemMatch`
Find books that have rating above 4.2 and a review rating ≥ 5:
```js
db.books.find({
  $and: [
    { rating: { $gt: 4.2 } },
    { reviews: { $elemMatch: { rating: { $gte: 5 } } } }
  ]
})
```

### `$regex` with Arrays
Find all books with tag matching regex “design”:
```js
db.books.find({ tags: { $regex: /design/i } })
```

### `$expr`
Compare one field to another (e.g., `rating` > `expectedRating`):
```js
db.books.find({ $expr: { $gt: ["$rating", "$expectedRating"] } })
```

---

## 🧮 Level 8: Aggregation Starters (Interview Favorites)

### Average review rating per book:
```js
db.books.aggregate([
  { $unwind: "$reviews" },
  { $group: { _id: "$name", avgReviewRating: { $avg: "$reviews.rating" } } }
])
```

### Books with average review rating > 4.5:
```js
db.books.aggregate([
  { $unwind: "$reviews" },
  { $group: { _id: "$name", avgReview: { $avg: "$reviews.rating" } } },
  { $match: { avgReview: { $gt: 4.5 } } }
])
```

---

## ⚖️ Embedded vs. Referenced Documents — Interview Tip

| Embedded Documents | Referenced Collections |
|--------------------|------------------------|
| 1-to-few relationships | 1-to-many or many-to-many |
| Faster reads, single fetch | Separate reads needed |
| Simpler structure | More scalable |
| 16MB document limit | No size restriction |

---

## 🧭 Bonus: Practice Collection

```js
db.books.insertMany([
  {
    name: "Mail System Design",
    author: "Harshith Kurapati",
    rating: 4.5,
    publishedYear: 2024,
    tags: ["system-design", "email", "architecture"],
    reviews: [
      { reviewer: "Ananya Reddy", rating: 5, comment: "Excellent" },
      { reviewer: "Rahul Sharma", rating: 4, comment: "Good read" }
    ]
  },
  {
    name: "Distributed Systems",
    author: "Martin Kleppmann",
    rating: 4.9,
    publishedYear: 2022,
    tags: ["system-design", "distributed", "database"],
    reviews: [
      { reviewer: "Harshith Kurapati", rating: 5, comment: "Must read" }
    ]
  },
  {
    name: "Web Performance Handbook",
    author: "Addy Osmani",
    rating: 4.2,
    publishedYear: 2021,
    tags: ["frontend", "performance", "optimization"],
    reviews: [
      { reviewer: "Sita Ram", rating: 3.8, comment: "Bit advanced" }
    ]
  }
])
```

---

### 🏁 Quick Summary

Mastering operators like `$gt`, `$lt`, `$in`, `$or`, `$elemMatch`, `$regex`, and `$expr` prepares you for most MongoDB interview scenarios — from simple filters to real-world nested queries.

---


- array query matching

```sh
db.books.insertMany([
  { name: "Book A", tags: ["system", "design", "architecture"] },
  { name: "Book B", tags: ["frontend", "css", "html"] },
  { name: "Book C", tags: ["system", "email"] },
  { name: "Book D", tags: ["architecture", "database"] }
])

```

- 1️⃣ Exact Array Match

If you want the array to match exactly (same elements, same order):

```sh
db.books.find({ tags: ["system", "design", "architecture"] })
```

✅ Matches only:

{ name: "Book A", tags: ["system", "design", "architecture"] }

❌ Does not match:

["architecture", "design", "system"] (different order)

["system", "design"] (different size)

2️⃣ One-of Match (any element matches)
This is the most common case.
You want documents where any element of the array matches a given value.

```sh
db.books.find({ tags: "system" })
```

Matches:

Book A (because tags has “system”)

Book C (also has “system”)

### delete one

```sh
db.books.deleteOne({ name: "Book B" })
```
[]
- delete one record deleteOne({filter})

### deleteMany

```sh
db.books.deleteMany({
    reviews: {
        $size: 2
    }
})
```

### update one & update many

```js
db.collection.updateOne(
   { filter_condition },
   { update_operation },
   { options }
)

db.collection.updateMany(
   { filter_condition },
   { update_operation },
   { options }
)

```

```js
db.users.updateOne(
  { city: "Hyderabad" },
  { $set: { age: 28 } }
)
```

| Operator    | Meaning                   | Example                             |
| ----------- | ------------------------- | ----------------------------------- |
| `$set`      | Set a field to a value    | `{ $set: { age: 30 } }`             |
| `$inc`      | Increment a numeric field | `{ $inc: { age: 1 } }`              |
| `$unset`    | Remove a field            | `{ $unset: { city: "" } }`          |
| `$push`     | Add item to array         | `{ $push: { tags: "new" } }`        |
| `$addToSet` | Add item if not present   | `{ $addToSet: { tags: "unique" } }` |


- creating indexing 

```js
// single-field ascending index
db.books.createIndex({ rating: 1 }, { name: "rating_idx", background: true })

// descending if you usually sort desc
db.books.createIndex({ rating: -1 }, { name: "rating_idx_desc", background: true })

// partial index: only index documents with rating field >= 1 (saves space if many docs have no rating)
db.books.createIndex(
  { rating: 1 },
  { name: "rating_partial_idx", partialFilterExpression: { rating: { $exists: true } } }
)

```

- drop indexing

```js
db.books.dropIndex({ rating: 1 }, { name: "rating_idx" })
```

- get all indexes

```js
db.books.getIndexes();
```


- indexes

```js
// single-field ascending index
db.collection.createIndex({ field: 1 })

// descending
db.collection.createIndex({ field: -1 })

// compound: index on fieldA asc then fieldB desc
db.collection.createIndex({ fieldA: 1, fieldB: -1 })

```

## Types of indexes (MongoDB)

- single field index - index on single field good for range , simple equality
- Compound index — index on multiple fields in specified order. Supports queries that filter on a prefix of the index keys.
- Multikey index — created implicitly when a field holds an array; index has one entry per array element. Enables queries that match array elements.
- Text index — supports text search ($text) across string content. Only one text index per collection (but can include multiple fields in it).
- unique index -> enforces unique values in indexes fields
- Partial index — index only documents that match a filter expression. Useful to reduce index size when only a subset of docs are queried.

### Compound indexes — order matters (very important)

- Compound indices are ordered. The index can be used for queries that filter on the left-most prefix of the index fields.

- Example: createIndex({ a: 1, b: 1, c: 1 })

- Queries on {a}, {a,b}, or {a,b,c} can use the index.

- Query on {b} alone cannot use it for lookup.

F- or sorting: an index can also satisfy sort requests if the sort order matches the index order (or is the reverse if single field). A compound index can satisfy sort on a prefix too.

- Interview tip: explain with prefix rule and show a failing example: compound index {a:1, b:1} does not help db.col.find({b:1}).

### Multikey indexes (arrays)

If you index a field that contains an array, MongoDB creates a multikey index and stores one index entry per array element.


```js
db.posts.insertOne({ tags: ["js","db","backend"], title: "..." });
db.posts.createIndex({ tags: 1 });
// index has entries for "js","db","backend"
```

### Using explain() to check index usage

- explain("executionStats") is interview gold because it shows what the server did and performance stats. 

```js
const res = db.users.find({ age: { $gt: 30 }, status: "active" }).explain("executionStats")
printjson(res.queryPlanner.winningPlan)
printjson(res.executionStats)

```


- common interview indexes

```js
// common: support lookup by userId and date range, and sort by date desc
db.events.createIndex({ userId: 1, createdAt: -1 })

// unique email
db.users.createIndex({ email: 1 }, { unique: true })

// partial index for active users only
db.users.createIndex({ lastLogin: 1 }, { partialFilterExpression: { active: true } })

// TTL index for sessions
db.sessions.createIndex({ lastAccess: 1 }, { expireAfterSeconds: 3600 })

// wildcard (handy for dynamic fields)
db.logs.createIndex({ "$**": 1 })

```

### Aggregations 

- array of pipeline operations which run one after the other to filter out the data and compute some thins like min, max, avg, sum


- below example will be grouped based on the sum of all ratings

- operator is $group 

```js
db.books.aggregate( [ { $group: { _id: "randomID", allRatings: { $sum: "$rating" } } } ])
db.books.aggregate( [ { $group: { _id: "randomID", allRatings: { $min: "$rating" } } } ])
db.books.aggregate( [ { $group: { _id: "randomID", allRatings: { $max: "$rating" } } } ])
db.books.aggregate( [ { $group: { _id: "randomID", allRatings: { $avg: "$rating" } } } ])
```

- operator is $match

```js
db.books.aggregate([
  { $match: { rating: { $gt: 4 } } }
])
```

```js
db.sales.aggregate([
  { $match: { region: "APAC" } },
  { $group: { _id: "$salesperson", total: { $sum: "$amount" } } }
])
```

- $limit Does

$limit restricts the number of documents that continue through the pipeline.

It takes a single numeric argument — the number of documents you want.

```js
db.collection.aggregate([
  { $limit: 5 }
])
```

- sort with limit

```js
db.movies.aggregate([
  { $sort: { rating: -1 } },
  { $limit: 5 }
])
```

- limit after group

```js
db.sales.aggregate([
  { $group: { _id: "$region", totalSales: { $sum: "$amount" } } },
  { $sort: { totalSales: -1 } },
  { $limit: 3 }
])

```

- use with skip 

```js
db.users.aggregate([
  { $skip: 10 },
  { $limit: 5 }
])

```

- $unwind Does

$unwind deconstructs an array field in each document into multiple documents, one for each element in the array.

```js
db.students.insertMany([
  { name: "Harshith", subjects: ["Math", "Science", "English"] },
  { name: "Aarav", subjects: ["History", "Geography"] }
])

db.students.aggregate([
  { $unwind: "$subjects" }
])

<!-- 
[
  { name: "Harshith", subjects: "Math" },
  { name: "Harshith", subjects: "Science" },
  { name: "Harshith", subjects: "English" },
  { name: "Aarav", subjects: "History" },
  { name: "Aarav", subjects: "Geography" }
] -->

db.students.aggregate([
  { $unwind: "$subjects" },
  { $group: { _id: "$subjects", studentCount: { $sum: 1 } } }
])


```

- preserve the empty field for unwind 

```sh
db.students.aggregate([
  {
    $unwind: {
      path: "$subjects",
      preserveNullAndEmptyArrays: true
    }
  }
])

```

- project operator

What $project Does

$project controls:

Which fields are included or excluded in the output.

Defines new fields using expressions.

Can rename or reshape existing fields.

```js
db.students.aggregate([
  { $project: { name: 1, age: 1, _id: 0 } }
])
<!-- # Only returns name and age, excluding _id. -->
```

<!-- Rename a field -->
```js
db.students.aggregate([
  { $project: { studentName: "$name", score: "$marks" } }
])
```