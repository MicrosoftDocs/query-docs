---
title: "EARLIEST function (DAX) | Microsoft Docs"
ms.service: powerbi 
ms.date: 12/10/2018
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend

---
# EARLIEST
Returns the current value of the specified column in an outer evaluation pass of the specified column.  
  
## Syntax  
  
```dax
EARLIEST(<column>)  
```
  
### Parameters  
  
|Term|Definition|  
|--------|--------------|  
|column|A reference to a column.|  
  
## Property Value/Return value  
A column with filters removed.  
  
## Remarks  
The EARLIEST function is similar to EARLIER, but lets you specify one additional level of recursion.  
  
## Example  
The current sample data does not support this scenario.  
  
```dax
=EARLIEST(<column>)  
```
  
## See also  
[EARLIER function &#40;DAX&#41;](earlier-function-dax.md)  
[Filter functions &#40;DAX&#41;](filter-functions-dax.md)  
  
