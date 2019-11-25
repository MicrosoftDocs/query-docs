---
title: "Table.LastN | Microsoft Docs"
ms.date: 8/1/2019
ms.service: powerquery

ms.reviewer: gepopell
ms.topic: reference
author: dougklopfenstein
ms.author: v-douklo

---
# Table.LastN

## Syntax

<pre>
Table.LastN(<b>table</b> as table, <b>countOrCondition</b> as any) as table 
</pre>
  
## About  
Returns the last row(s) from the table, `table`, depending on the value of `countOrCondition`: <ul> <li> If <code>countOrCondition</code> is a number, that many rows will be returned starting from position (end - <code>countOrCondition</code>). </li> <li> If <code>countOrCondition</code> is a condition, the rows that meet the condition will be returned in ascending position until a row does not meet the condition.</li> </ul>

## Example 1
Find the last two rows of the table.

```powerquery-m
Table.LastN(Table.FromRecords({[CustomerID = 1, Name = "Bob", Phone = "123-4567"], [CustomerID = 2, Name = "Jim", Phone = "987-6543"] , [CustomerID = 3, Name = "Paul", Phone = "543-7890"]}), 2)
```

<table> <tr> <th>CustomerID</th> <th>Name</th> <th>Phone</th> </tr> <tr> <td>2</td> <td>Jim</td> <td>987-6543</td> </tr> <tr> <td>3</td> <td>Paul</td> <td>543-7890</td> </tr> </table>

## Example 2
Find the last rows where [a] > 0 in the table.

```powerquery-m
Table.LastN(Table.FromRecords({[a = -1, b = -2], [a = 3, b = 4], [a = 5, b = 6]}), each _ [a] > 0)
```

<table> <tr> <th>a</th> <th>b</th> </tr> <tr> <td>3</td> <td>4</td> </tr> <tr> <td>5</td> <td>6</td> </tr> </table>
