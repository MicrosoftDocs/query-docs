---
title: "UTCNOW Function (DAX) | Microsoft Docs"
ms.service: powerbi 

ms.date: 11/07/2018
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# UTCNOW Function (DAX)
Returns the current UTC date and time
  
## Syntax  
  
```dax
UTCNOW()  
```
  
## Return Value  
A (**datetime)**.  
  
## Remarks  

The result of the UTCNOW function changes only when the formula is refreshed. It is not continuously updated. 
  
## Example  
The following:
  
```dax
EVALUATE { FORMAT(UTCNOW(), "General Date") } 
```

Returns:

|[Value]  |
|---------|
|2/2/2018 4:48:08 AM    |


## See Also  
[NOW Function &#40;DAX&#41;](now-function-dax.md)  
[UTCTODAY Function &#40;DAX&#41;](utctoday-function-dax.md)  
  
