---
title: "HASONEFILTER Function (DAX) | Microsoft Docs"
ms.prod: dax
ms.date: 5/22/2018
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# HASONEFILTER Function (DAX)
Returns **TRUE** when the number of directly filtered values on *columnName* is one; otherwise returns **FALSE**.  
  
## Syntax  
  
```dax
HASONEFILTER(<columnName>)  
```
  
#### Parameters  
columnName  
The name of an existing column, using standard DAX syntax. It cannot be an expression.  
  
## Return Value  
**TRUE** when the number of directly filtered values on *columnName* is one; otherwise returns **FALSE**.  
  
## Remarks  
  
1.  This function is similar to HASONEVALUE() with the difference that HASONEVALUE() works based on cross-filters while HASONEFILTER() works by a direct filter.  
  
## Example  
The following example shows how to use HASONEFILTER() to return the filter for   ResellerSales_USD[ProductKey]) if there is one filter, or to return BLANK if there are no filters or more than one filter on ResellerSales_USD[ProductKey]).  
  
```dax
=IF(HASONEFILTER(ResellerSales_USD[ProductKey]),FILTERS(ResellerSales_USD[ProductKey]),BLANK())  
```
