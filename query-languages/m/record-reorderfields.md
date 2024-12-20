---
description: "Learn more about: Record.ReorderFields"
title: "Record.ReorderFields"
ms.subservice: m-source
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

**Usage**

```powerquery-m
Record.ReorderFields(
    [CustomerID = 1, OrderID = 1, Item = "Fishing rod", Price = 100.0],
    {"OrderID", "CustomerID"}
)
```

**Output**

`[OrderID = 1, CustomerID = 1, Item = "Fishing rod", Price = 100.0]`
