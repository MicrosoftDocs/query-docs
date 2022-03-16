---
description: "Learn more about: Type.OpenRecord"
title: "Type.OpenRecord | Microsoft Docs"
ms.date: 3/14/2022
ms.service: powerquery

ms.reviewer: gepopell
ms.topic: reference
author: dougklopfenstein
ms.author: bezhan

---
# Type.OpenRecord

## Syntax

<pre>
Type.OpenRecord(<b>type</b> as type) as type
</pre>
  
## About

Returns an opened version of the given `record` `type` (or the same type, if it is already opened).

## Example 1

Create an opened version of `type [ A = number]`.

**Usage**

```powerquery-m
Type.OpenRecord(type [A = number])
```

**Output**

`type [A = number, ...]`
