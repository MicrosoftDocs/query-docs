---
description: "Learn more about: Value.ReplaceType"
title: "Value.ReplaceType | Microsoft Docs"
ms.date: 4/13/2022
ms.service: powerquery

ms.reviewer: gepopell
ms.topic: reference
author: dougklopfenstein
ms.author: bezhan

---
# Value.ReplaceType

## Syntax

<pre>
Value.ReplaceType(<b>value</b> as any, <b>type</b> as type) as any
</pre>
  
## About

Replaces the `value`'s type with the provided `type`.

## Example 1

Replace the default type of a record with a more specific type.

**Usage**

```powerquery-m
Type.RecordFields(
    Value.Type(
        Value.ReplaceType(
            [Column1 = 123],
            type [Column1 = number]
        )
    )
)[Column1][Type]
```

**Output**

`type number`
