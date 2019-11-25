---
title: "Type.IsNullable | Microsoft Docs"
ms.date: 8/2/2019
ms.service: powerquery

ms.reviewer: gepopell
ms.topic: reference
author: dougklopfenstein
ms.author: v-douklo

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

```powerquery-m
Type.IsNullable(type number)
```

`false`

## Example 2
Determine if `type nullable number` is nullable.

```powerquery-m
Type.IsNullable(type nullable number)
```

`true`
