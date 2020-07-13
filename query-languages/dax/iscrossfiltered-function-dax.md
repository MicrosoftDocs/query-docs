---
title: "ISCROSSFILTERED function (DAX) | Microsoft Docs"
ms.service: powerbi 
ms.date: 07/08/2020
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend

---
# ISCROSSFILTERED

Returns TRUE when *columnName* or another column in the same or related table is being filtered.  
  
## Syntax  
  
```dax
ISCROSSFILTERED(<columnName>)  
```
  
### Parameters  

|Term|Definition|  
|--------|--------------|  
|columnName|The name of an existing column, using standard DAX syntax. It cannot be an expression.| 
  
## Return value

**TRUE** when *columnName* or another column in the same or related table is being filtered. Otherwise returns **FALSE**.  
  
## Remarks  
  
- A column is said to be cross-filtered when a filter applied to another column in the same table or in a related table affects *columnName* by filtering it.  A column is said to be filtered *directly* when the filter or filters apply over the column.  
  
- The related function [ISFILTERED function](isfiltered-function-dax.md) returns TRUE when *columnName* is filtered directly.  
  
## See also

[ISFILTERED function](isfiltered-function-dax.md)  
[FILTERS function](filters-function-dax.md)  
[HASONEFILTER function](hasonefilter-function-dax.md)  
[HASONEVALUE function](hasonevalue-function-dax.md)  
