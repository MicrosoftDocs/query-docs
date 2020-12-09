---
title: "Table.RemoveRows | Microsoft Docs"
ms.date: 4/21/2020
ms.service: powerquery

ms.reviewer: gepopell
ms.topic: reference
author: dougklopfenstein
ms.author: bezhan

---
# Table.RemoveRows

## Syntax

<pre>
Table.RemoveRows(<b>table</b> as table, <b>offset</b> as number, optional <b>count</b> as nullable number) as table
</pre> 
  
## About  
Removes `count` of rows from the beginning of the `table`, starting at the `offset` specified. A default count of 1 is used if the `count` parameter isn't provided. 

## Example 1
Remove the first row from the table.

```powerquery-m
Table.RemoveRows(
    Table.FromRecords({
        [CustomerID = 1, Name = "Bob", Phone = "123-4567"],
        [CustomerID = 2, Name = "Jim", Phone = "987-6543"],
        [CustomerID = 3, Name = "Paul", Phone = "543-7890"],
        [CustomerID = 4, Name = "Ringo", Phone = "232-1550"]
    }),
    0
)
```

<table> <tr> <th>CustomerID</th> <th>Name</th> <th>Phone</th> </tr> <tr> <td>2</td> <td>Jim</td> <td>987-6543</td> </tr> <tr> <td>3</td> <td>Paul</td> <td>543-7890</td> </tr> <tr> <td>4</td> <td>Ringo</td> <td>232-1550</td> </tr> </table>

## Example 2
Remove the row at position 1 from the table.

```powerquery-m
Table.RemoveRows(
    Table.FromRecords({
        [CustomerID = 1, Name = "Bob", Phone = "123-4567"],
        [CustomerID = 2, Name = "Jim", Phone = "987-6543"],
        [CustomerID = 3, Name = "Paul", Phone = "543-7890"],
        [CustomerID = 4, Name = "Ringo", Phone = "232-1550"]
    }),
    1
)
```

<table> <tr> <th>CustomerID</th> <th>Name</th> <th>Phone</th> </tr> <tr> <td>1</td> <td>Bob</td> <td>123-4567</td> </tr> <tr> <td>3</td> <td>Paul</td> <td>543-7890</td> </tr> <tr> <td>4</td> <td>Ringo</td> <td>232-1550</td> </tr> </table>

## Example 3
Remove two rows starting at position 1 from the table.

```powerquery-m
Table.RemoveRows(
    Table.FromRecords({
        [CustomerID = 1, Name = "Bob", Phone = "123-4567"],
        [CustomerID = 2, Name = "Jim", Phone = "987-6543"],
        [CustomerID = 3, Name = "Paul", Phone = "543-7890"],
        [CustomerID = 4, Name = "Ringo", Phone = "232-1550"]
    }),
    1,
    2
)
```

<table> <tr> <th>CustomerID</th> <th>Name</th> <th>Phone</th> </tr> <tr> <td>1</td> <td>Bob</td> <td>123-4567</td> </tr> <tr> <td>4</td> <td>Ringo</td> <td>232-1550</td> </tr> </table>
