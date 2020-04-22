---
title: "Table.RemoveLastN | Microsoft Docs"
ms.date: 4/21/2020
ms.service: powerquery

ms.reviewer: gepopell
ms.topic: reference
author: dougklopfenstein
ms.author: v-douklo

---
# Table.RemoveLastN

## Syntax

<pre>
Table.RemoveLastN(<b>table</b> as table, optional <b>countOrCondition</b> as any) as table
</pre> 
  
## About  
Returns a table that does not contain the last `countOrCondition` rows of the table `table`. The number of rows removed depends on the optional parameter `countOrCondition`. <ul> <li> If <code>countOrCondition</code> is omitted only the last row is removed. </li> <li> If <code>countOrCondition</code> is a number, that many rows (starting at the bottom) will be removed. </li> <li> If <code>countOrCondition</code> is a condition, the rows that meet the condition will be removed until a row does not meet the condition.</li> </ul>

## Example 1
Remove the last row of the table.

```powerquery-m
Table.RemoveLastN(
    Table.FromRecords({
        [CustomerID = 1, Name = "Bob", Phone = "123-4567"],
        [CustomerID = 2, Name = "Jim", Phone = "987-6543"],
        [CustomerID = 3, Name = "Paul", Phone = "543-7890"],
        [CustomerID = 4, Name = "Ringo", Phone = "232-1550"]
    }), 
    1
)
```

<table> <tr> <th>CustomerID</th> <th>Name</th> <th>Phone</th> </tr> <tr> <td>1</td> <td>Bob</td> <td>123-4567</td> </tr> <tr> <td>2</td> <td>Jim</td> <td>987-6543</td> </tr> <tr> <td>3</td> <td>Paul</td> <td>543-7890</td> </tr> </table>

## Example 2
Remove the last rows where [CustomerID] > 2 of the table.

```powerquery-m
Table.RemoveLastN(
    Table.FromRecords({
        [CustomerID = 1, Name = "Bob", Phone = "123-4567"],
        [CustomerID = 2, Name = "Jim", Phone = "987-6543"],
        [CustomerID = 3, Name = "Paul", Phone = "543-7890"],
        [CustomerID = 4, Name = "Ringo", Phone = "232-1550"]
    }), 
    each [CustomerID] >= 2
)
```

<table> <tr> <th>CustomerID</th> <th>Name</th> <th>Phone</th> </tr> <tr> <td>1</td> <td>Bob</td> <td>123-4567</td> </tr> </table>
