---
title: "Type.ClosedRecord | Microsoft Docs"
ms.date: 8/2/2019
ms.service: powerquery

ms.reviewer: gepopell
ms.topic: reference
author: dougklopfenstein
ms.author: v-douklo

---
# Type.ClosedRecord

## Syntax

<pre>
Type.ClosedRecord(<b>type</b> as type) as type 
</pre>
  
## About  
Returns a closed version of the given `record` `type` (or the same type, if it is already closed).

## Example 1
Create a closed version of `type [ A = number,…]`.

```powerquery-m
Type.ClosedRecord(type [ A = number,...])
```

`type [ A = number ]`
