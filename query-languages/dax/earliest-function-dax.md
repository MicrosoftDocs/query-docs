---
title: "EARLIEST function (DAX) | Microsoft Docs"
ms.service: powerbi 
ms.date: 07/05/2020
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
  
## Return value

A column with filters removed.  
  
## Remarks

The EARLIEST function is similar to EARLIER, but lets you specify one additional level of recursion.  
  
## Example

The current sample data does not support this scenario.  
  
```dax
= EARLIEST(<column>)  
```
  
## See also

[EARLIER function](earlier-function-dax.md)  
[Filter functions](filter-functions-dax.md)  
