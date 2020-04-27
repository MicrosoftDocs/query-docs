---
title: "Table.Range | Microsoft Docs"
ms.date: 4/21/2020
ms.service: powerquery

ms.reviewer: gepopell
ms.topic: reference
author: dougklopfenstein
ms.author: v-douklo

---
# Table.Range

## Syntax

<pre>
Table.Range(<b>table</b> as table, <b>offset</b> as number, optional <b>count</b> as nullable number) as table
</pre>
  
## About  
Returns the rows from the `table` starting at the specified `offset`. An optional parameter, `count`, specifies how many rows to return. By default, all the rows after the offset are returned.

## Example 1
Return all the rows starting at offset 1 in the table.

```powerquery-m
Table.Range(
    Table.FromRecords({
        [CustomerID = 1, Name = "Bob", Phone = "123-4567"],
        [CustomerID = 2, Name = "Jim", Phone = "987-6543"],
        [CustomerID = 3, Name = "Paul", Phone = "543-7890"],
        [CustomerID = 4, Name = "Ringo", Phone = "232-1550"]
    }),
    1
)
```

<table> <tr> <th>CustomerID</th> <th>Name</th> <th>Phone</th> </tr> <tr> <td>2</td> <td>Jim</td> <td>987-6543</td> </tr> <tr> <td>3</td> <td>Paul</td> <td>543-7890</td> </tr> <tr> <td>4</td> <td>Ringo</td> <td>232-1550</td> </tr> </table>

## Example 2
Return one row starting at offset 1 in the table.

```powerquery-m
Table.Range(
    Table.FromRecords({
        [CustomerID = 1, Name = "Bob", Phone = "123-4567"],
        [CustomerID = 2, Name = "Jim", Phone = "987-6543"],
        [CustomerID = 3, Name = "Paul", Phone = "543-7890"],
        [CustomerID = 4, Name = "Ringo", Phone = "232-1550"]
    }),
    1,
    1
)
```

<table> <tr> <th>CustomerID</th> <th>Name</th> <th>Phone</th> </tr> <tr> <td>2</td> <td>Jim</td> <td>987-6543</td> </tr> </table>
