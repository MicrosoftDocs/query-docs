---
description: "Learn more about: Table.First"
title: "Table.First | Microsoft Docs"
ms.date: 4/20/2020
ms.service: powerquery

ms.reviewer: gepopell
ms.topic: reference
author: dougklopfenstein
ms.author: bezhan

---
# Table.First

## Syntax

<pre>
Table.First(<b>table</b> as table, optional <b>default</b> as any) as any 
</pre>
  
## About  
Returns the first row of the `table` or an optional default value, `default`, if the table is empty.

## Example 1
Find the first row of the table.

```powerquery-m
Table.First(
    Table.FromRecords({
        [CustomerID = 1, Name = "Bob", Phone = "123-4567"],
        [CustomerID = 2, Name = "Jim", Phone = "987-6543"],
        [CustomerID = 3, Name = "Paul", Phone = "543-7890"]
    })
)
```

<table> <tr> <th>CustomerID</th> <td>1</td> </tr> <tr> <th>Name</th> <td>Bob</td> </tr> <tr> <th>Phone</th> <td>123-4567</td> </tr> </table>

## Example 2
Find the first row of the table `({})` or return [a = 0, b = 0] if empty.

```powerquery-m
Table.First(Table.FromRecords({}), [a = 0, b = 0])
```

<table> <tr> <th>a</th> <td>0</td> </tr> <tr> <th>b</th> <td>0</td> </tr> </table>
