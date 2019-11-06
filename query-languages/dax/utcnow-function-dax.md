---
title: "UTCNOW function (DAX) | Microsoft Docs"
ms.service: powerbi 
ms.date: 12/10/2018
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend

---
# UTCNOW
Returns the current UTC date and time
  
## Syntax  
  
```dax
UTCNOW()  
```
  
## Return value  
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


## See also  
[NOW function &#40;DAX&#41;](now-function-dax.md)  
[UTCTODAY function &#40;DAX&#41;](utctoday-function-dax.md)  
  
