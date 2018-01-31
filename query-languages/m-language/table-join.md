---
title: "Table.Join | Microsoft Docs"
ms.custom: ""
ms.date: "01/19/2018"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: b51c8463-f989-490d-aed4-a00aaed87d85
caps.latest.revision: 9
author: "Minewiskan"
ms.author: "owend"
manager: "kfile"
---
# Table.Join
<code>Table.Join(<b>table1</b> as table, <b>key1</b> as any, <b>table2</b> as table, <b>key2</b> as any, optional <b>joinKind</b> as nullable number, optional <b>joinAlgorithm</b> as nullable number, optional <b>keyEqualityComparers</b> as nullable list) as table</code>

## About
Joins the rows of <code>table1</code> with the rows of <code>table2</code> based on the equality of the values of the key columns selected by <code>key1</code> (for <code>table1</code>) and <code>key2</code> (for <code>table2</code>).

By default, an inner join is performed, however an optional <code>joinKind</code> may be included to specify the type of join. Options include: <ul> <li><code>JoinKind.Inner</code></li> <li><code>JoinKind.LeftOuter</code></li> <li><code>JoinKind.RightOuter</code></li> <li><code>JoinKind.FullOuter</code></li> <li><code>JoinKind.LeftAnti</code></li> <li><code>JoinKind.RightAnti</code></li> </ul> </p> <p>An optional set of <code>keyEqualityComparers</code> may be included to specify how to compare the key columns.

## Example 1
Inner join the two tables on [CustomerID]



```
Table.Join(Table.FromRecords({[CustomerID = 1, Name = "Bob", Phone = "123-4567"], [CustomerID = 2, Name = "Jim", Phone = "987-6543"], [CustomerID = 3, Name = "Paul", Phone = "543-7890"], [CustomerID = 4, Name = "Ringo", Phone = "232-1550"]}), "CustomerID", Table.FromRecords({ [OrderID = 1, CustomerID = 1, Item = "Fishing rod", Price = 100.0], [OrderID = 2, CustomerID = 1, Item = "1 lb. worms", Price = 5.0], [OrderID = 3, CustomerID = 2, Item = "Fishing net", Price = 25.0], [OrderID = 4, CustomerID = 3, Item = "Fish tazer", Price = 200.0], [OrderID = 5, CustomerID = 3, Item = "Bandaids", Price = 2.0], [OrderID = 6, CustomerID = 1, Item = "Tackle box", Price = 20.0], [OrderID = 7, CustomerID = 5, Item = "Bait", Price = 3.25], [OrderID = 8, CustomerID = 5, Item = "Fishing Rod", Price = 100.0], [OrderID = 9, CustomerID = 6, Item = "Bait", Price = 3.25]}), "CustomerID")
```

<code></code>

<table> <tr> <th>CustomerID</th> <th>Name</th> <th>Phone</th> <th>OrderID</th> <th>Item</th> <th>Price</th> </tr> <tr> <td>1</td> <td>Bob</td> <td>123-4567</td> <td>1</td> <td>Fishing rod</td> <td>100</td> </tr> <tr> <td>1</td> <td>Bob</td> <td>123-4567</td> <td>2</td> <td>1 lb. worms</td> <td>5</td> </tr> <tr> <td>2</td> <td>Jim</td> <td>987-6543</td> <td>3</td> <td>Fishing net</td> <td>25</td> </tr> <tr> <td>3</td> <td>Paul</td> <td>543-7890</td> <td>4</td> <td>Fish tazer</td> <td>200</td> </tr> <tr> <td>3</td> <td>Paul</td> <td>543-7890</td> <td>5</td> <td>Bandaids</td> <td>2</td> </tr> <tr> <td>1</td> <td>Bob</td> <td>123-4567</td> <td>6</td> <td>Tackle box</td> <td>20</td> </tr> </table>

  
