---
title: "EVEN Function (DAX) | Microsoft Docs"
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
ms.assetid: 2ac6e520-bc8e-464d-b938-92284ec61f11
caps.latest.revision: 4
author: "Minewiskan"
ms.author: "owend"
manager: "mblythe"
---
# EVEN Function (DAX)
Returns number rounded up to the nearest even integer. You can use this function for processing items that come in twos. For example, a packing crate accepts rows of one or two items. The crate is full when the number of items, rounded up to the nearest two, matches the crate's capacity.  
  
## Syntax  
  
```  
EVEN(number)  
```  
  
#### Parameters  
  
|Term|Definition|  
|--------|--------------|  
|number|The value to round.|  
  
## Return Value  
Returns number rounded up to the nearest even integer.  
  
## Remarks  
If number is nonnumeric, EVEN returns the #VALUE! error value.  
  
Regardless of the sign of number, a value is rounded up when adjusted away from zero. If number is an even integer, no rounding occurs.  
  
## Example  
  
|Formula|Description|Result|  
|-----------|---------------|----------|  
|=EVEN(1.5)|Rounds 1.5 to the nearest even integer|2|  
|=EVEN(3)|Rounds 3 to the nearest even integer|4|  
|=EVEN(2)|Rounds 2 to the nearest even integer|2|  
|=EVEN(-1)|Rounds -1 to the nearest even integer|-2|  
  
