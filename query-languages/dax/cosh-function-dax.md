---
title: "COSH Function (DAX) | Microsoft Docs"
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
ms.assetid: 07434e76-5be2-4559-a4e1-73a696a75e34
caps.latest.revision: 4
author: "Minewiskan"
ms.author: "owend"
manager: "kfile"
---
# COSH Function (DAX)
Returns the hyperbolic cosine of a number.  
  
## Syntax  
  
```  
COSH(number)  
```  
  
#### Parameters  
  
|Term|Definition|  
|--------|--------------|  
|number|Required. Any real number for which you want to find the hyperbolic cosine.|  
  
## Return Value  
The hyperbolic cosine of a number.  
  
## Remarks  
The formula for the hyperbolic cosine is:  
  
![Formula](media/dax-cosh-formula.png)  
  
## Example  
  
|Formula|Description|Result|  
|-----------|---------------|----------|  
|=COSH(4)|Hyperbolic cosine of 4|27.308233|  
|=COSH(EXP(1))|Hyperbolic cosine of the base of the natural logarithm.|7.6101251|  
  
