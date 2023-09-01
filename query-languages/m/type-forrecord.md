---
description: "Learn more about: Type.ForRecord"
title: "Type.ForRecord"
---
# Type.ForRecord

## Syntax

<pre>
Type.ForRecord(<b>fields</b> as record, <b>open</b> as logical) as type
</pre>

## About

Returns a type that represents records with specific type constraints on fields.

## Example 1

Dynamically generate a table type.

**Usage**

```powerquery-m
let
    columnNames = {"Name", "Score"},
    columnTypes = {type text, type number},
    rowColumnTypes = List.Transform(columnTypes, (t) => [Type = t, Optional = false]),
    rowType = Type.ForRecord(Record.FromList(rowColumnTypes, columnNames), false)
in
    #table(type table rowType, {{"Betty", 90.3}, {"Carl", 89.5}})
```

**Output**

```powerquery-m
#table(
    type table [Name = text, Score = number],
    {{"Betty", 90.3}, {"Carl", 89.5}}
)
```
