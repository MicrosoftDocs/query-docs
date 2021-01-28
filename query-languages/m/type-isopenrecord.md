---
description: "Learn more about: Type.IsOpenRecord"
title: "Type.IsOpenRecord | Microsoft Docs"
ms.date: 4/21/2020
ms.service: powerquery

ms.reviewer: gepopell
ms.topic: reference
author: dougklopfenstein
ms.author: bezhan

---
# Type.IsOpenRecord

## Syntax

<pre>
Type.IsOpenRecord(<b>type</b> as type) as logical
</pre>
  
## About  
Returns a `logical` indicating whether a record `type` is open.

## Example 1
Determine if the record `type [ A = number, ...]` is open.

```powerquery-m
Type.IsOpenRecord(type [A = number, ...])
```

`true`
