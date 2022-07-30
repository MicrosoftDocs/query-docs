---
description: "Learn more about: Table.ReplaceKeys"
title: "Table.ReplaceKeys"
ms.date: 4/13/2022
ms.service: powerquery

ms.topic: reference
author: dougklopfenstein
ms.author: dougklo

---
# Table.ReplaceKeys

## Syntax

<pre>
Table.ReplaceKeys(<b>table</b> as table, <b>keys</b> as list) as table
</pre>
  
## About

Replaces the keys of the specified table.

## Example 1

Replace the existing keys of a table.

**Usage**

```powerquery-m
let
    table = Table.FromRecords({
        [Id = 1, Name = "Hello There"],
        [Id = 2, Name = "Good Bye"]
    }),
    tableWithKeys = Table.AddKey(table, {"Id"}, true),
    resultTable = Table.ReplaceKeys(tableWithKeys, {[Columns = {"Id"}, Primary = false]})
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
