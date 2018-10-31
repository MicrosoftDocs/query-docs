---
title: "EARLIEST Function (DAX) | Microsoft Docs"
ms.prod: powerbi 
ms.technology: dax
ms.date: 5/22/2018
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# EARLIEST Function (DAX)
Returns the current value of the specified column in an outer evaluation pass of the specified column.  
  
## Syntax  
  
```dax
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
  
```dax
=EARLIEST(<column>)  
```
  
## See Also  
[EARLIER Function &#40;DAX&#41;](earlier-function-dax.md)  
[Filter Functions &#40;DAX&#41;](filter-functions-dax.md)  
  
