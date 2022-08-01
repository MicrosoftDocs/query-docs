---
description: "Learn more about: Table.Keys"
title: "Table.Keys"
ms.date: 4/13/2022
---
# Table.Keys

## Syntax

<pre> 
Table.Keys(<b>table</b> as table) as list
</pre>
  
## About

Returns the keys of the specified table.

## Example 1

Get the list of keys for a table.

**Usage**

```powerquery-m
let
    table = Table.FromRecords({
        [Id = 1, Name = "Hello There"],
        [Id = 2, Name = "Good Bye"]
    }),
    tableWithKeys = Table.AddKey(table, {"Id"}, true),
    keys = Table.Keys(tableWithKeys)
in
    keys
```

**Output**

`{[Columns = {"Id"}, Primary = true]}`
