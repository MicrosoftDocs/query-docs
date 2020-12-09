---
title: "Table.AddIndexColumn | Microsoft Docs"
ms.date: 06/15/2020
ms.service: powerquery

ms.reviewer: gepopell
ms.topic: reference
author: dougklopfenstein
ms.author: bezhan

---
# Table.AddIndexColumn

## Syntax

<pre>
Table.AddIndexColumn(<b>table</b> as table, <b>newColumnName</b> as text, optional <b>initialValue</b> as nullable number, optional <b>increment</b> as nullable number, optional <b>columnType</b> as nullable type) as table
</pre>
  
## About  
Appends a column named `newColumnName` to the `table` with explicit position values. An optional value, `initialValue`, the initial index value. An optional value, `increment`, specifies how much to increment each index value.

## Example 1
Add an index column named "Index" to the table.

```powerquery-m
Table.AddIndexColumn(
    Table.FromRecords({
        [CustomerID = 1, Name = "Bob", Phone = "123-4567"],
        [CustomerID = 2, Name = "Jim", Phone = "987-6543"],
        [CustomerID = 3, Name = "Paul", Phone = "543-7890"],
        [CustomerID = 4, Name = "Ringo", Phone = "232-1550"]
    }),
    "Index"
)
```

<table> <tr> <th>CustomerID</th> <th>Name</th> <th>Phone</th> <th>Index</th> </tr> <tr> <td>1</td> <td>Bob</td> <td>123-4567</td> <td>0</td> </tr> <tr> <td>2</td> <td>Jim</td> <td>987-6543</td> <td>1</td> </tr> <tr> <td>3</td> <td>Paul</td> <td>543-7890</td> <td>2</td> </tr> <tr> <td>4</td> <td>Ringo</td> <td>232-1550</td> <td>3</td> </tr> </table>

## Example 2
Add an index column named "index", starting at value 10 and incrementing by 5, to the table.

```powerquery-m
Table.AddIndexColumn(
    Table.FromRecords({
        [CustomerID = 1, Name = "Bob", Phone = "123-4567"],
        [CustomerID = 2, Name = "Jim", Phone = "987-6543"],
        [CustomerID = 3, Name = "Paul", Phone = "543-7890"],
        [CustomerID = 4, Name = "Ringo", Phone = "232-1550"]
    }),
    "Index",
    10,
    5
)
```

<table> <tr> <th>CustomerID</th> <th>Name</th> <th>Phone</th> <th>Index</th> </tr> <tr> <td>1</td> <td>Bob</td> <td>123-4567</td> <td>10</td> </tr> <tr> <td>2</td> <td>Jim</td> <td>987-6543</td> <td>15</td> </tr> <tr> <td>3</td> <td>Paul</td> <td>543-7890</td> <td>20</td> </tr> <tr> <td>4</td> <td>Ringo</td> <td>232-1550</td> <td>25</td> </tr> </table>
