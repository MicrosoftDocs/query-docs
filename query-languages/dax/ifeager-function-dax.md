---
title: "IF.EAGER function (DAX) | Microsoft Docs"
ms.service: powerbi 
ms.date: 03/27/2020
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend

---
# IF.EAGER

Checks whether a condition is met, and returns one value if TRUE, and another value if FALSE. Uses eager execution.
  
## Syntax  
  
```dax
IF.EAGER ( <LogicalTest>, <ResultIfTrue> [, <ResultIfFalse>] ) 
```
  
### Parameters  
  
|Term|Definition|  
|--------|--------------|  
|LogicalTest|Any value or expression that can be evaluated to TRUE or FALSE.|  
|ResultIfTrue|The value that is returned if the logical test is TRUE.|
|ResultIfFalse|(Optional) The value that is returned if the logical test is FALSE; if omitted, BLANK is returned.|

## Return value

Any type of value that can be returned by an expression.
