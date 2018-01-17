---
title: "SINH Function (DAX) | Microsoft Docs"
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
ms.assetid: 8cebf19d-c513-4721-b52e-b10202db4a9c
caps.latest.revision: 4
author: "Minewiskan"
ms.author: "owend"
manager: "mblythe"
---
# SINH Function (DAX)
Returns the hyperbolic sine of a number.  
  
## Syntax  
  
```  
SINH(number)  
```  
  
#### Parameters  
  
|Term|Definition|  
|--------|--------------|  
|number|Required. Any real number.|  
  
## Return Value  
Returns the hyperbolic sine of a number.  
  
## Remarks  
The formula for the hyperbolic sine is:  
  
![Formula](../DAX/media/dax-sinh-formula.gif "Formula")  
  
## Example  
  
|Formula|Description|Result|  
|-----------|---------------|----------|  
|=2.868*SINH(0.0342\*1.03)|Probability of obtaining a result of less than 1.03 seconds.|0.1010491|  
  
