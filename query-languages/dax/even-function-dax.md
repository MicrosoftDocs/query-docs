---
title: "EVEN Function (DAX) | Microsoft Docs"
ms.prod: dax
ms.date: 4/13/2018
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# EVEN Function (DAX)
Returns number rounded up to the nearest even integer. You can use this function for processing items that come in twos. For example, a packing crate accepts rows of one or two items. The crate is full when the number of items, rounded up to the nearest two, matches the crate's capacity.  
  
## Syntax  
  
```  
EVEN(number)  
```  
  
#### Parameters  
  
|Term|Definition|  
|--------|--------------|  
|number|The value to round.|  
  
## Return Value  
Returns number rounded up to the nearest even integer.  
  
## Remarks  
If number is nonnumeric, EVEN returns the #VALUE! error value.  
  
Regardless of the sign of number, a value is rounded up when adjusted away from zero. If number is an even integer, no rounding occurs.  
  
## Example  
  
|Formula|Description|Result|  
|-----------|---------------|----------|  
|=EVEN(1.5)|Rounds 1.5 to the nearest even integer|2|  
|=EVEN(3)|Rounds 3 to the nearest even integer|4|  
|=EVEN(2)|Rounds 2 to the nearest even integer|2|  
|=EVEN(-1)|Rounds -1 to the nearest even integer|-2|  
  
