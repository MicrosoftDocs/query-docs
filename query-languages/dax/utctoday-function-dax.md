---
title: "UTCNOW Function (DAX) | Microsoft Docs"
ms.prod: dax
ms.date: 5/22/2018
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# UTCTODAY Function (DAX)
Returns the current UTC date.
  

  
## Syntax  
  
```dax
UTCTODAY()  
```
  
## Return Value  
A date.  
  
## Remarks  

UTCTODAY returns the time value 12:00:00 PM for all dates.    
The UTCNOW function is similar but returns the exact time and date.
  
## Example  
The following:
  
```dax
EVALUATE { FORMAT(UTCTODAY(), "General Date") } 
```dax
Returns:

|[Value]  |
|---------|
|2/2/2018    |


## See Also  
[NOW Function &#40;DAX&#41;](now-function-dax.md)  
[UTCNOW Function &#40;DAX&#41;](utcnow-function-dax.md)  
  
