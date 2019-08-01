---
title: "Record.SelectFields | Microsoft Docs"
ms.date: 8/1/2019
ms.service: powerquery

ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# Record.SelectFields

## Syntax

<pre>
Record.SelectFields(<b>record</b> as record, <b>fields</b> as any, optional <b>missingField</b> as nullable number) as record 
</pre>
  
## About  
Returns a record which includes only the fields specified in list `fields` from the input `record`.

## Example 1
Select the fields "Item" and "Price" in the record.

```powerquery-m
Record.SelectFields( [OrderID = 1, CustomerID = 1, Item = "Fishing rod", Price = 100.0] , {"Item", "Price"})
```

<table> <tr> <th>Item</th> <td>Fishing rod</td> </tr> <tr> <th>Price</th> <td>100</td> </tr> </table>
