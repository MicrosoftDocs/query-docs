---
title: "Record.ToTable | Microsoft Docs"
ms.date: 8/1/2019
ms.service: powerquery

ms.reviewer: gepopell
ms.topic: reference
author: dougklopfenstein
ms.author: bezhan

---
# Record.ToTable

## Syntax

<pre>
Record.ToTable(<b>record</b> as record) as table
</pre>
  
## About  
Returns a table containing the columns `Name` and `Value` with a row for each field in `record`.

## Example 1
Return the table from the record.

```powerquery-m
Record.ToTable([OrderID = 1, CustomerID = 1, Item = "Fishing rod", Price = 100.0])
```

<table> <tr> <th>Name</th> <th>Value</th> </tr> <tr> <td>OrderID</td> <td>1</td> </tr> <tr> <td>CustomerID</td> <td>1</td> </tr> <tr> <td>Item</td> <td>Fishing rod</td> </tr> <tr> <td>Price</td> <td>100</td> </tr> </table>
