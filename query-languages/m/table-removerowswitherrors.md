---
description: "Learn more about: Table.RemoveRowsWithErrors"
title: "Table.RemoveRowsWithErrors | Microsoft Docs"
ms.date: 3/10/2022
ms.service: powerquery

ms.reviewer: gepopell
ms.topic: reference
author: dougklopfenstein
ms.author: bezhan

---
# Table.RemoveRowsWithErrors

## Syntax

<pre>
Table.RemoveRowsWithErrors(<b>table</b> as table, optional <b>columns</b> as nullable list) as table
</pre>
  
## About

Returns a table with the rows removed from the input table that contain an error in at least one of the cells. If a columns list is specified, then only the cells in the specified columns are inspected for errors.

## Example 1

Remove error value from first row.

**Usage**

```powerquery-m
Table.RemoveRowsWithErrors(
    Table.FromRecords({
        [Column1 = ...],
        [Column1 = 2],
        [Column1 = 3]
    })
)
```

**Output**

```powerquery-m
Table.FromRecords({
    [Column1 = 2],
    [Column1 = 3]
})
```
