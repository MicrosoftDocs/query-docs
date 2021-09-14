---
description: "Learn more about: Table.CombineColumns"
title: "Table.CombineColumns | Microsoft Docs"
ms.date: 9/13/2021
ms.service: powerquery

ms.reviewer: gepopell
ms.topic: reference
author: dougklopfenstein
ms.author: bezhan

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

```powerquery-m
Table.CombineColumns(
    Table.FromRecords({[FirstName = "Bob", LastName = "Smith"]}),
    {"LastName", "FirstName"},
    Combiner.CombineTextByDelimiter(",", QuoteStyle.None),
    "FullName"
)
```

```powerquery-m
Table.FromRecords({[FullName = "Smith,Bob"]})
```
