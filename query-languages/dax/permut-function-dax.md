---
description: "Learn more about: PERMUT"
title: "PERMUT function (DAX) | Microsoft Docs"
ms.service: powerbi 
ms.date: 08/07/2020
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend 
recommendations: false

---
# PERMUT

Returns the number of permutations for a given number of objects that can be selected from number objects. A permutation is any set or subset of objects or events where internal order is significant. Permutations are different from combinations, for which the internal order is not significant. Use this function for lottery-style probability calculations.  
  
## Syntax  
  
```dax
PERMUT(number, number_chosen)  
```
  
### Parameters  
  
|Term|Definition|  
|--------|--------------|  
|number|Required. An integer that describes the number of objects.|  
|number_chosen|Required. An integer that describes the number of objects in each permutation.|  
  
## Return value

Returns the number of permutations for a given number of objects that can be selected from number objects  
  
## Remarks

- Both arguments are truncated to integers.  

- If number or number_chosen is nonnumeric, PERMUT returns the #VALUE! error value.  

- If number ≤ 0 or if number_chosen &lt; 0, PERMUT returns the #NUM! error value.  

- If number &lt; number_chosen, PERMUT returns the #NUM! error value.  

- The equation for the number of permutations is:  

    $$P\_{k,n} = \frac{n!}{(n-k)!}$$

- [!INCLUDE [function-not-supported-in-directquery-mode](includes/function-not-supported-in-directquery-mode.md)]

## Example  

In the following formula, permutations possible for a group of 3 objects where 2 are chosen:

```dax
= PERMUT(3,2)
```

Result,

6
