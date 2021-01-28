---
description: "Learn more about: Table.AlternateRows"
title: "Table.AlternateRows | Microsoft Docs"
ms.date: 4/20/2020
ms.service: powerquery

ms.reviewer: gepopell
ms.topic: reference
author: dougklopfenstein
ms.author: bezhan

---
# Table.AlternateRows

## Syntax

<pre>
Table.AlternateRows(<b>table</b> as table, <b>offset</b> as number, <b>skip</b> as number, <b>take</b> as number) as table
</pre>
  
## About  
Keeps the initial offset then alternates taking and skipping the following rows. <ul> <li><code>table</code>: The input table.</li> <li><code>offset</code>: The number of rows to keep before starting iterations.</li> <li><code>skip</code>: The number of rows to remove in each iteration.</li> <li><code>take</code>: The number of rows to keep in each iteration.</li> </ul> 

## Example 1
Return a table from the table that, starting at the first row, skips 1 value and then keeps 1 value.

```powerquery-m
Table.AlternateRows(
    Table.FromRecords({
        [CustomerID = 1, Name = "Bob", Phone = "123-4567"],
        [CustomerID = 2, Name = "Jim", Phone = "987-6543"],
        [CustomerID = 3, Name = "Paul", Phone = "543-7890"]
    }),
    1,
    1,
    1
)
```

<table> <tr> <th>CustomerID</th> <th>Name</th> <th>Phone</th> </tr> <tr> <td>1</td> <td>Bob</td> <td>123-4567</td> </tr> <tr> <td>3</td> <td>Paul</td> <td>543-7890</td> </tr> </table>
