---
title: "Table.Transpose | Microsoft Docs"
ms.date: 4/21/2020
ms.service: powerquery

ms.reviewer: gepopell
ms.topic: reference
author: dougklopfenstein
ms.author: v-douklo

---
# Table.Transpose

## Syntax

<pre>
Table.Transpose(<b>table</b> as table, optional <b>columns</b> as any) as table
</pre> 
  
## About  
Makes columns into rows and rows into columns.

## Example 1
Make the rows of the table of name-value pairs into columns.

```powerquery-m
Table.Transpose(
    Table.FromRecords({
        [Name = "Full Name", Value = "Fred"], 
        [Name = "Age", Value = 42], 
        [Name = "Country", Value = "UK"]
    })
)
```

<table> <tr> <th>Column1</th> <th>Column2</th> <th>Column3</th> </tr> <tr> <td>Full Name</td> <td>Age</td> <td>Country</td> </tr> <tr> <td>Fred</td> <td>42</td> <td>UK</td> </tr> </table>
