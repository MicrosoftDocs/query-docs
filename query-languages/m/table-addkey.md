---
description: "Learn more about: Table.AddKey"
title: "Table.AddKey | Microsoft Docs"
ms.date: 3/10/2022
ms.service: powerquery

ms.reviewer: gepopell
ms.topic: reference
author: dougklopfenstein
ms.author: bezhan

---
# Table.AddKey

## Syntax

<pre>
Table.AddKey(<b>table</b> as table, <b>columns</b> as list, <b>isPrimary</b> as logical) as table
</pre>
  
## About

Add a key to `table`, given `columns` is the subset of `table`'s column names that defines the key, and `isPrimary` specifies whether the key is primary.

## Example 1

Add a key to {[Id = 1, Name = "Hello There"], [Id = 2, Name = "Good Bye"]} that comprise of {"Id"} and make it a primary.

**Usage**

```powerquery-m
let
    tableType = type table [Id = Int32.Type, Name = text],
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
