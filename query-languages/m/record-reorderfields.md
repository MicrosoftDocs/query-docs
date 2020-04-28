---
title: "Record.ReorderFields | Microsoft Docs"
ms.date: 4/20/2020
ms.service: powerquery

ms.reviewer: gepopell
ms.topic: reference
author: dougklopfenstein
ms.author: v-douklo

---
# Record.ReorderFields

## Syntax

<pre>
Record.ReorderFields(<b>record</b> as record, <b>fieldOrder</b> as list, optional <b>missingField</b> as nullable number) as record
</pre>
  
## About  
Returns a record after reordering the fields in `record` in the order of fields specified in list `fieldOrder`. Field values are maintained and fields not listed in `fieldOrder` are left in their original position.

## Example 1
Reorder some of the fields in the record.

```powerquery-m
Record.ReorderFields(
    [CustomerID = 1, OrderID = 1, Item = "Fishing rod", Price = 100.0],
    {"OrderID", "CustomerID"}
)
```

<table> <tr> <th>OrderID</th> <td>1</td> </tr> <tr> <th>CustomerID</th> <td>1</td> </tr> <tr> <th>Item</th> <td>Fishing rod</td> </tr> <tr> <th>Price</th> <td>100</td> </tr> </table>
