---
description: "Learn more about: Record.FieldNames"
title: "Record.FieldNames"
ms.subservice: m-source
ms.topic: reference
---

# Record.FieldNames

## Syntax

<pre>
Record.FieldNames(<b>record</b> as record) as list
</pre>

## About

Returns the names of the fields in the record `record` as text.

## Example

Find the names of the fields in the record.

**Usage**

```powerquery-m
Record.FieldNames([OrderID = 1, CustomerID = 1, Item = "Fishing rod", Price = 100.0])
```

**Output**

`{"OrderID", "CustomerID", "Item", "Price"}`
