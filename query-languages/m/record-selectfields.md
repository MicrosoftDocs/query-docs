---
description: "Learn more about: Record.SelectFields"
title: "Record.SelectFields"
ms.date: 3/9/2022
ms.service: powerquery
ms.topic: reference
author: dougklopfenstein
ms.author: dougklo

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

**Usage**

```powerquery-m
Record.SelectFields(
    [OrderID = 1, CustomerID = 1, Item = "Fishing rod", Price = 100.0],
    {"Item", "Price"}
)
```

**Output**

`[Item = "Fishing rod", Price = 100]`
