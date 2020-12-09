---
title: "Record.FieldNames | Microsoft Docs"
ms.date: 8/1/2019
ms.service: powerquery

ms.reviewer: gepopell
ms.topic: reference
author: dougklopfenstein
ms.author: bezhan

---
# Record.FieldNames

## Syntax

<pre>
Record.FieldNames(<b>record</b> as record) as list
</pre>
  
## About  
Returns the names of the fields in the record `record` as text.

## Example 1
Find the names of the fields in the record.

```powerquery-m
Record.FieldNames([OrderID = 1, CustomerID = 1, Item = "Fishing rod", Price = 100.0])
```

<table> <tr><td>OrderID</td></tr> <tr><td>CustomerID</td></tr> <tr><td>Item</td></tr> <tr><td>Price</td></tr> </table>
