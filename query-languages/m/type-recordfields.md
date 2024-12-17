---
description: "Learn more about: Type.RecordFields"
title: "Type.RecordFields"
ms.subservice: m-source
---
# Type.RecordFields

## Syntax

<pre>
Type.RecordFields(<b>type</b> as type) as record
</pre>

## About

Returns a record describing the fields of a record `type`. Each field of the returned record type has a corresponding name and a value, in the form of a record `[ Type = type, Optional = logical ]`.
  
## Example 1

Find the name and value of the record `[ A = number, optional B = any]`.

**Usage**

```powerquery-m
Type.RecordFields(type [A = number, optional B = any])
```

**Output**

```powerquery-m
[
    A = [Type = type number, Optional = false],
    B = [Type = type any, Optional = true]
]
```
