---
description: "Learn more about: Type.ReplaceTableKeys"
title: "Type.ReplaceTableKeys"
ms.subservice: m-source
---
# Type.ReplaceTableKeys

## Syntax

<pre>
Type.ReplaceTableKeys(<b>tableType</b> as type, <b>keys</b> as list) as type
</pre>

## About

Returns a new table type with all keys replaced by the specified list of keys.

Each key is defined using a record in the following form:

* `Columns`: a list of the column names that define the key
* `Primary`: `true` if the key is the table's primary key; otherwise, `false`

The specified list of keys is validated to ensure that no more than one primary key is defined and that all key column names exist on the table type.

## Example 1

Replace the key information on a table type.

**Usage**

```powerquery-m
let
    BaseType = type table [ID = number, FirstName = text, LastName = text],
    KeysAdded = Type.ReplaceTableKeys(
        BaseType, 
        {
            [Columns = {"ID"}, Primary = true],
            [Columns = {"FirstName", "LastName"}, Primary = false]
        }
    ),
    DetailsOfKeys = Type.TableKeys(KeysAdded)
in
    DetailsOfKeys
```

**Output**

```powerquery-m
{
    [Columns = {"ID"}, Primary = true],
    [Columns = {"FirstName", "LastName"}, Primary = false]
}
```

## Example 2

Clear the key information previously defined on a table type.

**Usage**

```powerquery-m
let
    TypeWithKey = Type.AddTableKey(type table [ID = number, Name = text], {"ID"}, true),
    KeyRemoved = Type.ReplaceTableKeys(TypeWithKey, {}),
    DetailsOfKeys = Type.TableKeys(KeyRemoved)
in
    DetailsOfKeys
```

**Output**

```powerquery-m
{}
```
