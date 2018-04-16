---
title: "PERMUT Function (DAX) | Microsoft Docs"
ms.service: powerbi
ms.date: 4/13/2018
ms.reviewer: minewiskan
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# PERMUT Function (DAX)
Returns the number of permutations for a given number of objects that can be selected from number objects. A permutation is any set or subset of objects or events where internal order is significant. Permutations are different from combinations, for which the internal order is not significant. Use this function for lottery-style probability calculations.  
  
## Syntax  
  
```  
PERMUT(number, number_chosen)  
```  
  
#### Parameters  
  
|Term|Definition|  
|--------|--------------|  
|number|Required. An integer that describes the number of objects.|  
|number_chosen|Required. An integer that describes the number of objects in each permutation.|  
  
## Return Value  
Returns the number of permutations for a given number of objects that can be selected from number objects  
  
## Remarks  
Both arguments are truncated to integers.  
  
If number or number_chosen is nonnumeric, PERMUT returns the #VALUE! error value.  
  
If number ≤ 0 or if number_chosen &lt; 0, PERMUT returns the #NUM! error value.  
  
If number &lt; number_chosen, PERMUT returns the #NUM! error value.  
  
The equation for the number of permutations is:  
  
![Formula](media/dax-permut-formula.png)  
  
## Example  
  
|Formula|Description|Result|  
|-----------|---------------|----------|  
|=PERMUT(3,2)|Permutations possible for a group of 3 objects where 2 are chosen.|6|  
  
