---
title: "Record.RenameFields | Microsoft Docs"
ms.date: 4/20/2020
ms.service: powerquery

ms.reviewer: gepopell
ms.topic: reference
author: dougklopfenstein
ms.author: bezhan

---
# Record.RenameFields

## Syntax

<pre>
Record.RenameFields(<b>record</b> as record, <b>renames</b> as list, optional <b>missingField</b> as nullable number) as record  
</pre>
  
## About  
Returns a record after renaming fields in the input `record` to the new field names specified in list `renames`. For multiple renames, a nested list can be used ({ {old1, new1}, {old2, new2} }.

## Example 1
Rename the field "UnitPrice" to "Price" from the record.

```powerquery-m
Record.RenameFields(
    [OrderID = 1, CustomerID = 1, Item = "Fishing rod", UnitPrice = 100.0],
    {"UnitPrice", "Price"}
)
```

<table> <tr> <th>OrderID</th> <td>1</td> </tr> <tr> <th>CustomerID</th> <td>1</td> </tr> <tr> <th>Item</th> <td>Fishing rod</td> </tr> <tr> <th>Price</th> <td>100</td> </tr> </table>

## Example 2
Rename the fields "UnitPrice" to "Price" and "OrderNum" to "OrderID" from the record.

```powerquery-m
Record.RenameFields(
    [OrderNum = 1, CustomerID = 1, Item = "Fishing rod", UnitPrice = 100.0],
    {
        {"UnitPrice", "Price"},
        {"OrderNum", "OrderID"}
    }
)
```

<table> <tr> <th>OrderID</th> <td>1</td> </tr> <tr> <th>CustomerID</th> <td>1</td> </tr> <tr> <th>Item</th> <td>Fishing rod</td> </tr> <tr> <th>Price</th> <td>100</td> </tr> </table>
