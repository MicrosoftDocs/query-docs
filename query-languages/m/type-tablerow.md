---
description: "Learn more about: Type.TableRow"
title: "Type.TableRow"
ms.subservice: m-source
ms.topic: reference
---
# Type.TableRow

## Syntax

<pre>
Type.TableRow(<b>table</b> as type) as type
</pre>
  
## About

Returns the row type of the specified table type. The result will always be a record type.

## Example 1

Return the row type information for a simple table.

**Usage**

```powerquery-m
let
    tableRowType = Type.TableRow(Value.Type(#table({"Column1"}, {})))
in
    Type.RecordFields(tableRowType)
```

**Output**

`[Column1 = [Type = type any, Optional = false]]`

## Related content

* [Types and type conversion](type-conversion.md)
