---
title: "HASONEFILTER Function (DAX) | Microsoft Docs"
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
  - "sql13.as.daxref.HASONEFILTER.f1"
helpviewer_keywords: 
  - "HASONEFILTER function"
ms.assetid: 10a9718e-fd47-4d81-a7ba-701e3e75042e
caps.latest.revision: 8
author: "Minewiskan"
ms.author: "owend"
manager: "mblythe"
---
# HASONEFILTER Function (DAX)
Returns **TRUE** when the number of directly filtered values on *columnName* is one; otherwise returns **FALSE**.  
  
## Syntax  
  
```  
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
  
```  
=IF(HASONEFILTER(ResellerSales_USD[ProductKey]),FILTERS(ResellerSales_USD[ProductKey]),BLANK())  
```  
