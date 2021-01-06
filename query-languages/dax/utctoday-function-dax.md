---
title: "UTCTODAY function (DAX) | Microsoft Docs"
ms.service: powerbi 
ms.date: 01/06/2021
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend

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

- UTCTODAY returns the time value 12:00:00 PM for all dates.

- The UTCNOW function is similar but returns the exact time and date.
  
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

[NOW function](now-function-dax.md)  
[UTCNOW function](utcnow-function-dax.md)  
