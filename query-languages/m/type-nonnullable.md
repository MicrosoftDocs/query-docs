---
title: "Type.NonNullable | Microsoft Docs"
ms.date: 8/2/2019
ms.service: powerquery

ms.reviewer: gepopell
ms.topic: reference
author: dougklopfenstein
ms.author: bezhan

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

```powerquery-m
Type.NonNullable(type nullable number)
```

`type number`
