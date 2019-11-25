---
title: "Comparer.Ordinal | Microsoft Docs"
ms.date: 7/29/2019
ms.service: powerquery

ms.reviewer: gepopell
ms.topic: reference
author: dougklopfenstein
ms.author: v-douklo

---
# Comparer.Ordinal

## Syntax

<pre>
Comparer.Ordinal(<b>x</b> as any, <b>y</b> as any) as number 
</pre> 
  
## About  
Returns a comparer function which uses Ordinal rules to compare the provided values `x` and `y`.

## Example 1
Using Ordinal rules, compare if "encyclopædia" and "encyclopaedia" are equivalent. Note these are equivalent using `Comparer.FromCulture("en-us")`. 

```powerquery-m
Comparer.Equals(Comparer.Ordinal, "encyclopædia", "encyclopaedia")
```

`false`