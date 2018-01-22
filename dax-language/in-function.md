---
title: "IN Function | Microsoft Docs"
ms.custom: ""
ms.date: "12/28/2017"
ms.reviewer: ""
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: 68b7f08c-e33f-4f90-93e7-8ca75f50339b
caps.latest.revision: 2
author: "Minewiskan"
ms.author: "owend"
manager: "kfile"
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

  
