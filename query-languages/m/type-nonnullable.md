---
description: "Learn more about: Type.NonNullable"
title: "Type.NonNullable | Microsoft Docs"
ms.date: 3/14/2022
ms.service: powerquery

ms.topic: reference
author: dougklopfenstein
ms.author: dougklo

---
# Type.NonNullable

## Syntax

<pre>
Type.NonNullable(<b>type</b> as type) as type
</pre>
  
## About

Returns the non `nullable` type from the `type`.

## Example 1

Return the non nullable type of `type nullable number`.

**Usage**

```powerquery-m
Type.NonNullable(type nullable number)
```

**Output**

`type number`
