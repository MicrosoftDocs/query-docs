---
title: "Table.Join | Microsoft Docs"
ms.date: 4/16/2018
ms.prod: power-query
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# Table.Join
`Table.Join(<b>table1</b> as table, <b>key1</b> as any, <b>table2</b> as table, <b>key2</b> as any, optional <b>joinKind</b> as nullable number, optional <b>joinAlgorithm</b> as nullable number, optional <b>keyEqualityComparers</b> as nullable list) as table`

## About
Joins the rows of `table1` with the rows of `table2` based on the equality of the values of the key columns selected by `key1` (for `table1`) and `key2` (for `table2`).

By default, an inner join is performed, however an optional `joinKind` may be included to specify the type of join. Options include: <ul> <li>`JoinKind.Inner`</li> <li>`JoinKind.LeftOuter`</li> <li>`JoinKind.RightOuter`</li> <li>`JoinKind.FullOuter`</li> <li>`JoinKind.LeftAnti`</li> <li>`JoinKind.RightAnti`</li> </ul> </p> <p>An optional set of `keyEqualityComparers` may be included to specify how to compare the key columns.

## Example 1
Inner join the two tables on [CustomerID]

```
Table.Join
(Table.FromRecords({
[CustomerID = 1, Name = "Bob", Phone = "123-4567"],
[CustomerID = 2, Name = "Jim", Phone = "987-6543"], 
[CustomerID = 3, Name = "Paul", Phone = "543-7890"],
[CustomerID = 4, Name = "Ringo", Phone = "232-1550"]}), 
"CustomerID", Table.FromRecords({ [OrderID = 1, CustomerID = 1, Item = "Fishing rod", Price = 100.0], 
[OrderID = 2, CustomerID = 1, Item = "1 lb. worms", Price = 5.0],
[OrderID = 3, CustomerID = 2, Item = "Fishing net", Price = 25.0], 
[OrderID = 4, CustomerID = 3, Item = "Fish tazer", Price = 200.0], 
[OrderID = 5, CustomerID = 3, Item = "Bandaids", Price = 2.0], 
[OrderID = 6, CustomerID = 1, Item = "Tackle box", Price = 20.0],
[OrderID = 7, CustomerID = 5, Item = "Bait", Price = 3.25], 
[OrderID = 8, CustomerID = 5, Item = "Fishing Rod", Price = 100.0], 
[OrderID = 9, CustomerID = 6, Item = "Bait", Price = 3.25]}), "CustomerID")
```

<table> <tr> <th>CustomerID</th> <th>Name</th> <th>Phone</th> <th>OrderID</th> <th>Item</th> <th>Price</th> </tr> <tr> <td>1</td> <td>Bob</td> <td>123-4567</td> <td>1</td> <td>Fishing rod</td> <td>100</td> </tr> <tr> <td>1</td> <td>Bob</td> <td>123-4567</td> <td>2</td> <td>1 lb. worms</td> <td>5</td> </tr> <tr> <td>2</td> <td>Jim</td> <td>987-6543</td> <td>3</td> <td>Fishing net</td> <td>25</td> </tr> <tr> <td>3</td> <td>Paul</td> <td>543-7890</td> <td>4</td> <td>Fish tazer</td> <td>200</td> </tr> <tr> <td>3</td> <td>Paul</td> <td>543-7890</td> <td>5</td> <td>Bandaids</td> <td>2</td> </tr> <tr> <td>1</td> <td>Bob</td> <td>123-4567</td> <td>6</td> <td>Tackle box</td> <td>20</td> </tr> </table>

  
