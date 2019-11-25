---
title: "Type.IsOpenRecord | Microsoft Docs"
ms.date: 8/2/2019
ms.service: powerquery

ms.reviewer: gepopell
ms.topic: reference
author: dougklopfenstein
ms.author: v-douklo

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
Type.IsOpenRecord(type [ A = number,...])
```

`true`
