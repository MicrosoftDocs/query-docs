---
title: "Number.Ln | Microsoft Docs"
ms.date: 7/31/2019
ms.service: powerquery

ms.reviewer: gepopell
ms.topic: reference
author: dougklopfenstein
ms.author: v-douklo

---
# Number.Ln

## Syntax

<pre>
Number.Ln(<b>number</b> as nullable number) as nullable number 
</pre>
  
## About  
Returns the natural logarithm of a number, `number`. If `number` is null `Number.Ln` returns null.

####Example 1
Get the natural logarithm of 15.

```powerquery-m
Number.Ln(15)
```

`2.70805020110221`
