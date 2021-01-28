---
description: "Learn more about: ISFILTERED"
title: "ISFILTERED function (DAX) | Microsoft Docs"
ms.service: powerbi 
ms.date: 07/08/2020
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend

---
# ISFILTERED

Returns TRUE when *columnName* is being filtered directly. If there is no filter on the column or if the filtering happens because a different column in the same table or in a related table is being filtered then the function returns **FALSE**.  
  
## Syntax  
  
```dax
ISFILTERED(<columnName>)  
```
  
### Parameters  

|Term|Definition|  
|--------|--------------|  
|columnName|The name of an existing column, using standard DAX syntax. It cannot be an expression.| 
  
## Return value

TRUE when *columnName* is being filtered directly.  
  
## Remarks  
  
- *columnName* is said to be filtered directly when the filter or filters apply over the column; a column is said to be cross-filtered when a filter applied to another column in the same table or in a related table affects *columnName* the column by filtering it as well.  
  
- The related function [ISCROSSFILTERED](iscrossfiltered-function-dax.md) returns TRUE when *columnName* or another column in the same or related table is being filtered.  

- [!INCLUDE [function-not-supported-in-directquery-mode](includes/function-not-supported-in-directquery-mode.md)]

## See also

[ISCROSSFILTERED function](iscrossfiltered-function-dax.md)  
[FILTERS function](filters-function-dax.md)  
[HASONEFILTER function](hasonefilter-function-dax.md)  
[HASONEVALUE function](hasonevalue-function-dax.md)  
