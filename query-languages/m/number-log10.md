---
title: "Number.Log10 | Microsoft Docs"
ms.date: 4/16/2018
ms.prod: power-query
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# Number.Log10

## Syntax

<pre>
Number.Log10(**number** as nullable number) as nullable number
</pre>

## About  
Returns the Base 10 logarithm of a number, `number`. If `number` is null `Number.Log10` returns null.
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|number|The number to calculate.|  
  
## Example 1
Get the base 10 logarithm of 2.


```powerquery-m
Number.Log10(2)
```

```powerquery-m
0.3010299956639812
```

