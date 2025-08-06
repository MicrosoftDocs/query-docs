---
description: "Learn more about: Table.AddKey"
title: "Table.AddKey"
ms.subservice: m-source
---
# Table.AddKey

## Syntax

<pre>
Table.AddKey(
    <b>table</b> as table,
    <b>columns</b> as list,
    <b>isPrimary</b> as logical
) as table
</pre>
  
## About

Adds a key to `table`, where `columns` is the list of column names that define the key, and `isPrimary` specifies whether the key is primary.

## Example 1

Add a single-column primary key to a table.

**Usage**

```powerquery-m
let
    table = Table.FromRecords({
        [Id = 1, Name = "Hello There"],
        [Id = 2, Name = "Good Bye"]
    }),
    resultTable = Table.AddKey(table, {"Id"}, true)
in
    resultTable
```

**Output**

```powerquery-m
Table.FromRecords({
    [Id = 1, Name = "Hello There"],
    [Id = 2, Name = "Good Bye"]
})
```
