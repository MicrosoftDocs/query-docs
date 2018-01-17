---
title: "EARLIEST Function (DAX) | Microsoft Docs"
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
f1_keywords: 
  - "sql13.as.daxref.EARLIEST.f1"
helpviewer_keywords: 
  - "EARLIEST function"
ms.assetid: 9befa04d-78db-492e-a463-80b8b77206d6
caps.latest.revision: 4
author: "Minewiskan"
ms.author: "owend"
manager: "mblythe"
---
# EARLIEST Function (DAX)
Returns the current value of the specified column in an outer evaluation pass of the specified column.  
  
## Syntax  
  
```  
EARLIEST(<column>)  
```  
  
#### Parameters  
  
|Term|Definition|  
|--------|--------------|  
|**column**|A reference to a column.|  
  
## Property Value/Return Value  
A column with filters removed.  
  
## Remarks  
The EARLIEST function is similar to EARLIER, but lets you specify one additional level of recursion.  
  
## Example  
The current sample data does not support this scenario.  
  
```  
=EARLIEST(<column>)  
```  
  
## See Also  
[EARLIER Function &#40;DAX&#41;](../DAX/earlier-function-dax.md)  
[Filter Functions &#40;DAX&#41;](../DAX/filter-functions-dax.md)  
  
