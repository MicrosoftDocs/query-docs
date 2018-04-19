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
<code>Number.Log10(**number** as nullable number) as nullable number</code>

## About  
Returns the Base 10 logarithm of a number, <code>number</code>. If <code>number</code> is null <code>Number.Log10</code> returns null.
  
```  
Number.Log10 (number as nullable number)  as nullable number  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|number|The number to calculate.|  
  
## Example 1
Get the base 10 logarithm of 2.


```
Number.Log10(2)
```


```
0.3010299956639812
```

