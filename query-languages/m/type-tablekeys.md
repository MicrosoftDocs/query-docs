---
description: "Learn more about: Type.TableKeys"
title: "Type.TableKeys"
---
# Type.TableKeys

## Syntax

<pre>
Type.TableKeys(<b>tableType</b> as type) as list
</pre>

## About

Returns the possibly empty list of keys for the given table type.

Each key is described by a record in the following form: 
* `Columns`: a list of the column names that define the key
* `Primary`: `true` if the key is the table's primary key; otherwise, `false`

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
