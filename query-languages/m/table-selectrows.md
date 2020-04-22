---
title: "Table.SelectRows | Microsoft Docs"
ms.date: 4/21/2020
ms.service: powerquery

ms.reviewer: gepopell
ms.topic: reference
author: dougklopfenstein
ms.author: v-douklo

---
# Table.SelectRows

## Syntax

<pre>
Table.SelectRows(<b>table</b> as table, <b>condition</b> as function) as table
</pre>
  
## About  
Returns a table of rows from the `table`, that matches the selection `condition`.

## Example 1
Select the rows in the table where the values in [CustomerID] column are greater than 2.

```powerquery-m
Table.SelectRows(
    Table.FromRecords({ 
        [CustomerID = 1, Name = "Bob", Phone = "123-4567"], 
        [CustomerID = 2, Name = "Jim", Phone = "987-6543"] , 
        [CustomerID = 3, Name = "Paul", Phone = "543-7890"] , 
        [CustomerID = 4, Name = "Ringo", Phone = "232-1550"] 
    }), 
    each [CustomerID] > 2
)
```

<table> <tr> <th>CustomerID</th> <th>Name</th> <th>Phone</th> </tr> <tr> <td>3</td> <td>Paul</td> <td>543-7890</td> </tr> <tr> <td>4</td> <td>Ringo</td> <td>232-1550</td> </tr> </table>

## Example 2
Select the rows in the table where the names do not contain a "B".

```powerquery-m
Table.SelectRows(
    Table.FromRecords({ 
        [CustomerID = 1, Name = "Bob", Phone = "123-4567"], 
        [CustomerID = 2, Name = "Jim", Phone = "987-6543"] , 
        [CustomerID = 3, Name = "Paul", Phone = "543-7890"] , 
        [CustomerID = 4, Name = "Ringo", Phone = "232-1550"] 
    }), 
    each not Text.Contains([Name], "B")
)
```

<table> <tr> <th>CustomerID</th> <th>Name</th> <th>Phone</th> </tr> <tr> <td>2</td> <td>Jim</td> <td>987-6543</td> </tr> <tr> <td>3</td> <td>Paul</td> <td>543-7890</td> </tr> <tr> <td>4</td> <td>Ringo</td> <td>232-1550</td> </tr> </table>
