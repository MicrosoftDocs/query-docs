---
title: "UTCNOW Function (DAX) | Microsoft Docs"
ms.custom: ""
ms.date: "03/05/2018"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "analysis-services"
  - "daxlang"
ms.topic: "language-reference"
ms.assetid:
author: "Minewiskan"
ms.author: "owend"
manager: "kfile"
---
# UTCTODAY Function (DAX)
Returns the current UTC date.
  

  
## Syntax  
  
```  
UTCTODAY()  
```  
  
## Return Value  
A date.  
  
## Remarks  

UTCTODAY returns the time value 12:00:00 PM for all dates.    
The UTCNOW function is similar but returns the exact time and date.
  
## Example  
The following:
  
```  
EVALUATE { FORMAT(UTCTODAY(), "General Date") } 
```  
Returns:

|[Value]  |
|---------|
|2/2/2018    |


## See Also  
[NOW Function &#40;DAX&#41;](now-function-dax.md)  
[UTCNOW Function &#40;DAX&#41;](utcnow-function-dax.md)  
  
