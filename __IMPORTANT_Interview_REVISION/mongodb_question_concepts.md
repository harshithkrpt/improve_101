

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