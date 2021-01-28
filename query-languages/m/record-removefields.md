---
description: "Learn more about: Record.RemoveFields"
title: "Record.RemoveFields | Microsoft Docs"
ms.date: 4/20/2020
ms.service: powerquery

ms.reviewer: gepopell
ms.topic: reference
author: dougklopfenstein
ms.author: bezhan

---
# Record.RemoveFields

## Syntax

<pre>
Record.RemoveFields(<b>record</b> as record, <b>fields</b> as any, optional <b>missingField</b> as nullable number) as record
</pre>
  
## About  
Returns a record that removes all the fields specified in list `fields` from the input `record`. If the field specified does not exist, an exception is thrown.

## Example 1
Remove the field "Price" from the record.

```powerquery-m
Record.RemoveFields([CustomerID = 1, Item = "Fishing rod", Price = 18.00], "Price")
```

<table> <tr> <th>CustomerID</th> <td>1</td> </tr> <tr> <th>Item</th> <td>Fishing rod</td> </tr> </table>

## Example 2
Remove the fields "Price" and "Item" from the record.

```powerquery-m
Record.RemoveFields([CustomerID = 1, Item = "Fishing rod", Price = 18.00], {"Price", "Item"})
```

<table> <tr> <th>CustomerID</th> <td>1</td> </tr> </table>
