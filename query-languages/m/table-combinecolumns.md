---
description: "Learn more about: Table.CombineColumns"
title: "Table.CombineColumns"
ms.subservice: m-source
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
