---
title: "UTCNOW function (DAX) | Microsoft Docs"
ms.service: powerbi 
ms.date: 12/10/2018
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# UTCTODAY
Returns the current UTC date.
  

  
## Syntax  
  
```dax
UTCTODAY()  
```
  
## Return value  
A date.  
  
## Remarks  

UTCTODAY returns the time value 12:00:00 PM for all dates.    
The UTCNOW function is similar but returns the exact time and date.
  
## Example  
The following:
  
```dax
EVALUATE { FORMAT(UTCTODAY(), "General Date") } 
```

Returns:

|[Value]  |
|---------|
|2/2/2018    |


## See also  
[NOW function &#40;DAX&#41;](now-function-dax.md)  
[UTCNOW function &#40;DAX&#41;](utcnow-function-dax.md)  
  
