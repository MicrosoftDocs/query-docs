---
title: "ISFILTERED Function (DAX) | Microsoft Docs"
ms.prod: dax
ms.date: 5/22/2018
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# ISFILTERED Function (DAX)
Returns TRUE when *columnName* is being filtered directly. If there is no filter on the column or if the filtering happens because a different column in the same table or in a related table is being filtered then the function returns **FALSE**.  
  
## Syntax  
  
```  
ISFILTERED(<columnName>)  
```  
  
#### Parameters  
columnName  
The name of an existing column, using standard DAX syntax. It cannot be an expression.  
  
## Return Value  
TRUE when *columnName* is being filtered directly.  
  
## Remarks  
  
-   *columnName* is said to be filtered directly when the filter or filters apply over the column; a column is said to be cross-filtered when a filter applied to another column in the same table or in a related table affects *columnName* the column by filtering it as well.  
  
-   The related function [ISCROSSFILTERED Function &#40;DAX&#41;](iscrossfiltered-function-dax.md) returns TRUE when *columnName* or another column in the same or related table is being filtered.  
  
  
  
## See Also  
[ISCROSSFILTERED Function &#40;DAX&#41;](iscrossfiltered-function-dax.md)  
[FILTERS Function &#40;DAX&#41;](filters-function-dax.md)  
[HASONEFILTER Function &#40;DAX&#41;](hasonefilter-function-dax.md)  
[HASONEVALUE Function &#40;DAX&#41;](hasonevalue-function-dax.md)  
  
