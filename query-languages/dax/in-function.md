---
title: "IN Function | Microsoft Docs"
ms.service: powerbi
ms.date: 4/13/2018
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# IN Function
Returns True if the scalar value shows up in at least one row of the input relation.
  
## Syntax  
  
```  
IN 
```  
  
#### Parameters  
  
|Term|Definition|  
|--------|--------------|  
|**scalar expression**||  
|**table expression**||  

  
## Return Value  

  
## Remarks  

  
## Example  

```
Filtered Sales:=CALCULATE (
        [Internet Total Sales], 'Product'[Color] IN { "Red", "Blue", "Black" }
    )
```
  
## See Also  

  
