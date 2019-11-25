---
title: "Table.SplitColumn | Microsoft Docs"
ms.date: 8/1/2019
ms.service: powerquery

ms.reviewer: gepopell
ms.topic: reference
author: dougklopfenstein
ms.author: v-douklo

---
# Table.SplitColumn

## Syntax

<pre>
Table.SplitColumn(<b>table</b> as table, <b>sourceColumn</b> as text, <b>splitter</b> as function, optional <b>columnNamesOrNumber</b> as any, optional <b>default</b> as any, optional <b>extraColumns</b> as any) as table
</pre> 
  
## About  
Splits the specified columns into a set of additional columns using the specified splitter function.

## Example 1
Split the [Name] column at position of "i" into two columns

```powerquery-m
let Customers = Table.FromRecords({ [CustomerID = 1, Name = "Bob", Phone = "123-4567"], [CustomerID = 2, Name = "Jim", Phone = "987-6543"], [CustomerID = 3, Name = "Paul", Phone = "543-7890"], [CustomerID = 4, Name = "Cristina", Phone = "232-1550"] }) in Table.SplitColumn(Customers,"Name",Splitter.SplitTextByDelimiter("i"),2)
```

<table> <tr> <th>CustomerID</th> <th>Name.1</th> <th>Name.2</th> <th>Phone</th> </tr> <tr> <td>1</td> <td>Bob</td> <td></td> <td>123-4567</td> </tr> <tr> <td>2</td> <td>J</td> <td>m</td> <td>987-6543</td> </tr> <tr> <td>3</td> <td>Paul</td> <td></td> <td>543-7890</td> </tr> <tr> <td>4</td> <td>Cr</td> <td>st</td> <td>232-1550</td> </tr> </table>
