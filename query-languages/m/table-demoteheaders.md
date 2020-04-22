---
title: "Table.DemoteHeaders | Microsoft Docs"
ms.date: 4/20/2020
ms.service: powerquery

ms.reviewer: gepopell
ms.topic: reference
author: dougklopfenstein
ms.author: v-douklo

---
# Table.DemoteHeaders

## Syntax

<pre>
Table.DemoteHeaders(<b>table</b> as table) as table
</pre>
  
## About  
Demotes the column headers (i.e. column names) to the first row of values. The default column names are "Column1", "Column2" and so on.

## Example 1
Demote the first row of values in the table.

```powerquery-m
Table.DemoteHeaders( 
    Table.FromRecords({ 
        [CustomerID = 1, Name = "Bob", Phone = "123-4567"], 
        [CustomerID = 2, Name = "Jim", Phone = "987-6543"] 
    })
)
```

<table> <tr> <th>Column1</th> <th>Column2</th> <th>Column3</th> </tr> <tr> <td>CustomerID</td> <td>Name</td> <td>Phone</td> </tr> <tr> <td>1</td> <td>Bob</td> <td>123-4567</td> </tr> <tr> <td>2</td> <td>Jim</td> <td>987-6543</td> </tr> </table>
