---
description: "Learn more about: Table.SingleRow"
title: "Table.SingleRow | Microsoft Docs"
ms.date: 3/10/2022
ms.service: powerquery

ms.reviewer: gepopell
ms.topic: reference
author: dougklopfenstein
ms.author: bezhan

---
# Table.SingleRow

## Syntax

<pre>
Table.SingleRow(<b>table</b> as table) as record  
</pre>
  
## About

Returns the single row in the one row `table`. If the `table` has more than one row, an exception is thrown.

## Example 1

Return the single row in the table.

**Usage**

```powerquery-m
Table.SingleRow(Table.FromRecords({[CustomerID = 1, Name = "Bob", Phone = "123-4567"]}))
```

**Output**

`[CustomerID = 1, Name = "Bob", Phone = "123-4567"]`
