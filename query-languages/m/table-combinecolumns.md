---
description: "Learn more about: Table.CombineColumns"
title: "Table.CombineColumns | Microsoft Docs"
ms.date: 3/14/2022
ms.service: powerquery

ms.reviewer: ehvonleh
ms.topic: reference
author: dougklopfenstein
ms.author: dougklo

---
# Table.CombineColumns

## Syntax

<pre>
Table.CombineColumns(<b>table</b> as table, <b>sourceColumns</b> as list, <b>combiner</b> as function, <b>column</b> as text) as table
</pre>
  
## About

Combines the specified columns into a new column using the specified combiner function.

## Example 1

Combine the last and first names into a new column, separated by a comma.

**Usage**

```powerquery-m
Table.CombineColumns(
    Table.FromRecords({[FirstName = "Bob", LastName = "Smith"]}),
    {"LastName", "FirstName"},
    Combiner.CombineTextByDelimiter(",", QuoteStyle.None),
    "FullName"
)
```

**Output**

```powerquery-m
Table.FromRecords({[FullName = "Smith,Bob"]})
```
