---
title: "IN function | Microsoft Docs"
ms.service: powerbi 
ms.date: 07/08/2020
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend

---
# IN

Returns True if the scalar value shows up in at least one row of the input relation.
  
## Syntax  
  
```dax
IN
```
  
### Parameters  
  
|Term|Definition|  
|--------|--------------|  
|scalar expression||  
|table expression||  

## Return value

True
  
## Remarks

None
  
## Example  

```dax
Filtered Sales:=CALCULATE (
        [Internet Total Sales], 'Product'[Color] IN { "Red", "Blue", "Black" }
    )
```

