---
description: "Learn more about: Type.TableKeys"
title: "Type.TableKeys"
ms.subservice: m-source
ms.topic: reference
---

# Type.TableKeys

## Syntax

<pre>
Type.TableKeys(<b>tableType</b> as type) as list
</pre>

## About

Returns the possibly empty list of keys for the given table type.

Each key is defined using a record in the following form:

* `Columns`: a list of the column names that define the key
* `Primary`: `true` if the key is the table's primary key; otherwise, `false`

## Example

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

`{[Columns = {"ID"}, Primary = true]}`
