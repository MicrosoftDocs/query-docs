---
description: "Learn more about: Table.Unpivot"
title: "Table.Unpivot"
ms.date: 3/10/2022
ms.service: powerquery

ms.topic: reference
author: dougklopfenstein
ms.author: dougklo

---
# Table.Unpivot

## Syntax

<pre>
Table.Unpivot(<b>table</b> as table, <b>pivotColumns</b> as list, <b>attributeColumn</b> as text, <b>valueColumn</b> as text) as table
</pre>
  
## About

Translates a set of columns in a table into attribute-value pairs, combined with the rest of the values in each row.

## Example 1

Take the columns "a", "b", and "c" in the table `({[ key = "x", a = 1, b = null, c = 3 ], [ key = "y", a = 2, b = 4, c = null ]})` and unpivot them into attribute-value pairs.

**Usage**

```powerquery-m
Table.Unpivot(
    Table.FromRecords({
        [key = "x", a = 1, b = null, c = 3],
        [key = "y", a = 2, b = 4, c = null]
    }),
    {"a", "b", "c"},
    "attribute",
    "value"
)
```

**Output**

```powerquery-m
Table.FromRecords({
    [key = "x", attribute = "a", value = 1],
    [key = "x", attribute = "c", value = 3],
    [key = "y", attribute = "a", value = 2],
    [key = "y", attribute = "b", value = 4]
})
```
