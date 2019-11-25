---
title: "Table.RemoveFirstN | Microsoft Docs"
ms.date: 10/10/2019
ms.service: powerquery
ms.reviewer: gepopell
ms.topic: reference
author: dougklopfenstein
ms.author: v-douklo
---
# Table.RemoveFirstN
  
## Syntax

<pre>
Table.RemoveFirstN(<b>table</b> as table, optional <b>countOrCondition</b> as any) as table 
</pre>
  
## About  
Returns a table that does not contain the first specified number of rows, `countOrCondition`, of the table `table`. The number of rows removed depends on the optional parameter `countOrCondition`. <ul> <li> If <code>countOrCondition</code> is omitted only the first row is removed. </li> <li> If <code>countOrCondition</code> is a number, that many rows (starting at the top) will be removed. </li> <li> If <code>countOrCondition</code> is a condition, the rows that meet the condition will be removed until a row does not meet the condition.</li> </ul>

## Example 1
Remove the first row of the table.

```powerquery-m
Table.RemoveFirstN(Table.FromRecords({[CustomerID = 1, Name = "Bob", Phone = "123-4567"], [CustomerID = 2, Name = "Jim", Phone = "987-6543"], [CustomerID = 3, Name = "Paul", Phone = "543-7890"], [CustomerID = 4, Name = "Ringo", Phone = "232-1550"]}), 1)
```

<table> <tr> <th>CustomerID</th> <th>Name</th> <th>Phone</th> </tr> <tr> <td>2</td> <td>Jim</td> <td>987-6543</td> </tr> <tr> <td>3</td> <td>Paul</td> <td>543-7890</td> </tr> <tr> <td>4</td> <td>Ringo</td> <td>232-1550</td> </tr> </table>

## Example 2
Remove the first two rows of the table.

```powerquery-m
Table.RemoveFirstN(Table.FromRecords({[CustomerID = 1, Name = "Bob", Phone = "123-4567"], [CustomerID = 2, Name = "Jim", Phone = "987-6543"], [CustomerID = 3, Name = "Paul", Phone = "543-7890"], [CustomerID = 4, Name = "Ringo", Phone = "232-1550"]}), 2)
```

<table> <tr> <th>CustomerID</th> <th>Name</th> <th>Phone</th> </tr> <tr> <td>3</td> <td>Paul</td> <td>543-7890</td> </tr> <tr> <td>4</td> <td>Ringo</td> <td>232-1550</td> </tr> </table>

## Example 3
Remove the first rows where [CustomerID] <=2 of the table.

```powerquery-m
Table.RemoveFirstN(Table.FromRecords({[CustomerID = 1, Name = "Bob", Phone = "123-4567"], [CustomerID = 2, Name = "Jim", Phone = "987-6543"] , [CustomerID = 3, Name = "Paul", Phone = "543-7890"] , [CustomerID = 4, Name = "Ringo", Phone = "232-1550"]}), each [CustomerID] <= 2)
```

<table> <tr> <th>CustomerID</th> <th>Name</th> <th>Phone</th> </tr> <tr> <td>3</td> <td>Paul</td> <td>543-7890</td> </tr> <tr> <td>4</td> <td>Ringo</td> <td>232-1550</td> </tr> </table>
