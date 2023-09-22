---
description: "Learn more about: Type.TableKeys"
title: "Type.TableKeys"
ms.date: 10/7/2022
---
# Type.TableKeys

## Syntax

<pre>
Type.TableKeys(<b>tableType</b> as type) as list
</pre>

## About

Returns the possibly empty list of keys for the given table type.

Each key is described using a record in the following form: 
```powerquery-m
[
    Columns = { text }, // list of column names defining the key
    Primary = logical // indicates whether the key is the primary key
]
```

## Example 1

Return the key information for a table type.

**Usage**

```powerquery-m
let
    BaseType = type table [ID = number, Name = text],
    AddKey = Type.AddTableKey(BaseType, {"ID"}, true),
    DetailsOfKeys = Type.TableKeys(AddKey)
in
    DetailsOfKeys
```

**Output**

```powerquery-m
{[Columns = {"ID"}, Primary = true]}
```