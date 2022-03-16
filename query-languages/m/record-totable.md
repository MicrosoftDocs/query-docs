---
description: "Learn more about: Record.ToTable"
title: "Record.ToTable | Microsoft Docs"
ms.date: 3/9/2022
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

**Usage**

```powerquery-m
Record.ToTable([OrderID = 1, CustomerID = 1, Item = "Fishing rod", Price = 100.0])
```

**Output**

```powerquery-m
Table.FromRecords({
    [Name = "OrderID", Value = 1],
    [Name = "CustomerID", Value = 1],
    [Name = "Item", Value = "Fishing rod"],
    [Name = "Price", Value = 100]
})
```
