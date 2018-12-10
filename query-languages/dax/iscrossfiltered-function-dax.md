---
title: "ISCROSSFILTERED function (DAX) | Microsoft Docs"
ms.service: powerbi 
ms.date: 12/10/2018
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# ISCROSSFILTERED
Returns TRUE when *columnName* or another column in the same or related table is being filtered.  
  
## Syntax  
  
```dax
ISCROSSFILTERED(<columnName>)  
```
  
#### Parameters  

|Term|Definition|  
|--------|--------------|  
|columnName|The name of an existing column, using standard DAX syntax. It cannot be an expression.| 
  
## Return value  
**TRUE** when *columnName* or another column in the same or related table is being filtered. Otherwise returns **FALSE**.  
  
## Remarks  
  
-   A column is said to be cross-filtered when a filter applied to another column in the same table or in a related table affects *columnName* by filtering it.  A column is said to be filtered *directly* when the filter or filters apply over the column.  
  
-   The related function [ISFILTERED function &#40;DAX&#41;](isfiltered-function-dax.md) returns TRUE when *columnName* is filtered directly.  
  
  
## See also  
[ISFILTERED function &#40;DAX&#41;](isfiltered-function-dax.md)  
[FILTERS function &#40;DAX&#41;](filters-function-dax.md)  
[HASONEFILTER function &#40;DAX&#41;](hasonefilter-function-dax.md)  
[HASONEVALUE function &#40;DAX&#41;](hasonevalue-function-dax.md)  
  
