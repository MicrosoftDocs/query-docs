---
description: "Learn more about: Type.IsNullable"
title: "Type.IsNullable | Microsoft Docs"
ms.date: 3/14/2022
ms.service: powerquery

ms.reviewer: ehvonleh
ms.topic: reference
author: dougklopfenstein
ms.author: dougklo

---
# Type.IsNullable

## Syntax

<pre>  
Type.IsNullable(<b>type</b> as type) as logical
</pre>
  
## About

Returns `true` if a type is a `nullable` type; otherwise, `false`.

## Example 1

Determine if `number` is nullable.

**Usage**

```powerquery-m
Type.IsNullable(type number)
```

**Output**

`false`

## Example 2

Determine if `type nullable number` is nullable.

**Usage**

```powerquery-m
Type.IsNullable(type nullable number)
```

**Output**

`true`
