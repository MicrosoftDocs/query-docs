---
description: "Learn more about: Table.UnpivotOtherColumns"
title: "Table.UnpivotOtherColumns"
ms.subservice: m-source
ms.topic: reference
---

# Table.UnpivotOtherColumns

## Syntax

<pre>
Table.UnpivotOtherColumns(
    <b>table</b> as table,
    <b>pivotColumns</b> as list,
    <b>attributeColumn</b> as text,
    <b>valueColumn</b> as text
) as table
</pre>
  
## About

Translates all columns other than a specified set into attribute-value pairs, combined with the rest of the values in each row.

## Example 1

Translates all columns other than a specified set into attribute-value pairs, combined with the rest of the values in each row.

**Usage**

```powerquery-m
Table.UnpivotOtherColumns(
    Table.FromRecords({
        [key = "key1", attribute1 = 1, attribute2 = 2, attribute3 = 3],
        [key = "key2", attribute1 = 4, attribute2 = 5, attribute3 = 6]
    }),
    {"key"},
    "column1",
    "column2"
)
```

**Output**

```powerquery-m
Table.FromRecords({
    [key = "key1", column1 = "attribute1", column2 = 1],
    [key = "key1", column1 = "attribute2", column2 = 2],
    [key = "key1", column1 = "attribute3", column2 = 3],
    [key = "key2", column1 = "attribute1", column2 = 4],
    [key = "key2", column1 = "attribute2", column2 = 5],
    [key = "key2", column1 = "attribute3", column2 = 6]
})
```
