---
description: "Learn more about: Record.RenameFields"
title: "Record.RenameFields | Microsoft Docs"
ms.date: 3/9/2022
ms.service: powerquery

ms.topic: reference
author: dougklopfenstein
ms.author: dougklo

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

**Usage**

```powerquery-m
Record.RenameFields(
    [OrderID = 1, CustomerID = 1, Item = "Fishing rod", UnitPrice = 100.0],
    {"UnitPrice", "Price"}
)
```

**Output**

`[OrderID = 1, CustomerID = 1, Item = "Fishing rod", Price = 100.0]`

## Example 2

Rename the fields "UnitPrice" to "Price" and "OrderNum" to "OrderID" from the record.

**Usage**

```powerquery-m
Record.RenameFields(
    [OrderNum = 1, CustomerID = 1, Item = "Fishing rod", UnitPrice = 100.0],
    {
        {"UnitPrice", "Price"},
        {"OrderNum", "OrderID"}
    }
)
```

**Output**

`[OrderID = 1, CustomerID = 1, Item = "Fishing rod", Price = 100.0]`
