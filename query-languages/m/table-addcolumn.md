---
title: "Table.AddColumn | Microsoft Docs"
ms.date: 4/20/2020
ms.service: powerquery

ms.reviewer: gepopell
ms.topic: reference
author: dougklopfenstein
ms.author: v-douklo

---
# Table.AddColumn

## Syntax

<pre>
Table.AddColumn(<b>table</b> as table, <b>newColumnName</b> as text, <b>columnGenerator</b> as function, optional <b>columnType</b> as nullable type) as table
</pre>
  
## About  
Adds a column named `newColumnName` to the table `table`. The values for the column are computed using the specified selection function `columnGenerator` with each row taken as an input.

## Example 1
Add a column named "TotalPrice" to the table with each value being the sum of column [Price] and column [Shipping].

```powerquery-m
Table.AddColumn( 
    Table.FromRecords({ 
        [OrderID = 1, CustomerID = 1, Item = "Fishing rod", Price = 100.0, Shipping = 10.00], 
        [OrderID = 2, CustomerID = 1, Item = "1 lb. worms", Price = 5.0, Shipping = 15.00], 
        [OrderID = 3, CustomerID = 2, Item = "Fishing net", Price = 25.0, Shipping = 10.00] 
    }), 
    "TotalPrice", 
    each [Price] + [Shipping] 
)
```

<table> <tr> <th>OrderID</th> <th>CustomerID</th> <th>Item</th> <th>Price</th> <th>Shipping</th> <th>TotalPrice</th> </tr> <tr> <td>1</td> <td>1</td> <td>Fishing rod</td> <td>100</td> <td>10</td> <td>110</td> </tr> <tr> <td>2</td> <td>1</td> <td>1 lb. worms</td> <td>5</td> <td>15</td> <td>20</td> </tr> <tr> <td>3</td> <td>2</td> <td>Fishing net</td> <td>25</td> <td>10</td> <td>35</td> </tr> </table>
