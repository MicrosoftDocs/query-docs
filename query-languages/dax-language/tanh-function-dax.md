---
title: "TANH Function (DAX) | Microsoft Docs"
ms.custom: ""
ms.date: "12/28/2017"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "analysis-services"
  - "daxlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: f571414c-dd4e-48e2-9b98-be534231129d
caps.latest.revision: 4
author: "Minewiskan"
ms.author: "owend"
manager: "kfile"
---
# TANH Function (DAX)
Returns the hyperbolic tangent of a number.  
  
## Syntax  
  
```  
TANH(number)  
```  
  
#### Parameters  
  
|Term|Definition|  
|--------|--------------|  
|number|Required. Any real number.|  
  
## Return Value  
Returns the hyperbolic tangent of a number.  
  
## Remarks  
The formula for the hyperbolic tangent is:  
  
![Formula](media/dax-tanh-formula.png)  
  
## Example  
  
|Formula|Description|Result|  
|-----------|---------------|----------|  
|=TANH(-2)|Hyperbolic tangent of -2 (-0.96403)|-0.964028|  
|=TANH(0)|Hyperbolic tangent of 0 (0)|0|  
|=TANH(0.5)|Hyperbolic tangent of 0.5 (0.462117)|0.462117|  
  
