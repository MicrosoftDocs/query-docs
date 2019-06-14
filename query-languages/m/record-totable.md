---
title: "Record.ToTable | Microsoft Docs"
ms.date: 6/15/2019
ms.service: powerquery

ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# Record.ToTable

  
## About  
Returns a table containing the columns <code>Name</code> and <code>Value</code> with a row for each field in <code>record</code>.
  
## Syntax

<pre>
Record.ToTable(<b>record</b> as record) as table
</pre>
  
## Example
Return the table from the record.

```powerquery-m
Record.ToTable([OrderID = 1, CustomerID = 1, Item = "Fishing rod", Price = 100.0])
```

<table> <tr> <th>Name</th> <th>Value</th> </tr> <tr> <td>OrderID</td> <td>1</td> </tr> <tr> <td>CustomerID</td> <td>1</td> </tr> <tr> <td>Item</td> <td>Fishing rod</td> </tr> <tr> <td>Price</td> <td>100</td> </tr> </table>
  
  
