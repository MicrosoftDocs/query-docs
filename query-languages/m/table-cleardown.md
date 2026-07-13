---
description: "Learn more about: Table.ClearDown"
title: "Table.ClearDown"
ms.date: 7/9/2026
ms.subservice: m-source
ms.topic: reference
---

# Table.ClearDown

## Syntax

<pre>
Table.ClearDown(<b>table</b> as table, <b>columns</b> as list) as table
</pre>

## About

Replaces the specified `columns` with null when all their values are repeated from the previous row.

## Example

Clear the Region and Place columns when they're both repeated.

**Usage**

```powerquery-m
Table.ClearDown(
    Table.FromRecords({
        [Region = "West", Place = 1, Name = "Bob"],
        [Region = "West", Place = 1, Name = "John"],
        [Region = "West", Place = 2, Name = "Brad"],
        [Region = "East", Place = 3, Name = "Mark"],
        [Region = "East", Place = 3, Name = "Tom"]
    }),
    {"Region", "Place"}
)
```

**Output**

```powerquery-m
Table.FromRecords({
    [Region = "West", Place = 1, Name = "Bob"],
    [Region = null, Place = null, Name = "John"],
    [Region = "West", Place = 2, Name = "Brad"],
    [Region = "East", Place = 3, Name = "Mark"],
    [Region = null, Place = null, Name = "Tom"]
})
```
