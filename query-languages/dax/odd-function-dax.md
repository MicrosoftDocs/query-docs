---
title: "ODD Function (DAX) | Microsoft Docs"
ms.prod: dax
ms.date: 4/13/2018
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# ODD Function (DAX)
Returns number rounded up to the nearest odd integer.  
  
## Syntax  
  
```  
ODD(number)  
```  
  
#### Parameters  
  
|Term|Definition|  
|--------|--------------|  
|number|Required. The value to round.|  
  
## Return Value  
Returns number rounded up to the nearest odd integer.  
  
## Remarks  
If number is nonnumeric, ODD returns the #VALUE! error value.  
  
Regardless of the sign of number, a value is rounded up when adjusted away from zero. If number is an odd integer, no rounding occurs.  
  
## Example  
  
|Formula|Description|Result|  
|-----------|---------------|----------|  
|=ODD(1.5)|Rounds 1.5 up to the nearest odd integer.|3|  
|=ODD(3)|Rounds 3 up to the nearest odd integer.|3|  
|=ODD(2)|Rounds 2 up to the nearest odd integer.|3|  
|=ODD(-1)|Rounds -1 up to the nearest odd integer.|-1|  
|=ODD(-2)|Rounds -2 up (away from 0) to the nearest odd integer.|-3|  
  
