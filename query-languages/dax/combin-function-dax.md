---
title: "COMBIN Function (DAX) | Microsoft Docs"
ms.service: powerbi 

ms.date: 11/07/2018
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# COMBIN Function (DAX)
Returns the number of combinations for a given number of items. Use COMBIN to determine the total possible number of groups for a given number of items.  
  
## Syntax  
  
```dax
COMBIN(number, number_chosen)  
```
  
#### Parameters  
  
|Term|Definition|  
|--------|--------------|  
|number|The number of items.|  
|number_chosen|The number of items in each combination.|  
  
## Return Value  
Returns the number of combinations for a given number of items.  
  
## Remarks  
Numeric arguments are truncated to integers.  
  
If either argument is nonnumeric, COMBIN returns the #VALUE! error value.  
  
If number &lt; 0, number_chosen &lt; 0, or number &lt; number_chosen, COMBIN returns the #NUM! error value.  
  
A combination is any set or subset of items, regardless of their internal order. Combinations are distinct from permutations, for which the internal order is significant.  
  
The number of combinations is as follows, where number = n and number_chosen = k:  

![combin formula](media/dax-combin-formula1.png)
  
Where  

![combin formula result](media/dax-combin-formula2.png)
  
## Example  
  
|Formula|Description|Result|  
|-----------|---------------|----------|  
|=COMBIN(8,2)|Possible two-person teams that can be formed from 8 candidates.|28|  
  
