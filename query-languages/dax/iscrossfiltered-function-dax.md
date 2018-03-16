---
title: "ISCROSSFILTERED Function (DAX) | Microsoft Docs"
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
  - "sql13.as.daxref.ISCROSSFILTERED.f1"
helpviewer_keywords: 
  - "ISCROSSFILTERED function"
ms.assetid: bbba9123-3c8a-45d3-ad63-e9e4db9e946a
caps.latest.revision: 8
author: "Minewiskan"
ms.author: "owend"
manager: "kfile"
---
# ISCROSSFILTERED Function (DAX)
Returns TRUE when *columnName* or another column in the same or related table is being filtered.  
  
## Syntax  
  
```  
ISCROSSFILTERED(<columnName>)  
```  
  
#### Parameters  
columnName  
The name of an existing column, using standard DAX syntax. It cannot be an expression.  
  
## Return Value  
**TRUE** when *columnName* or another column in the same or related table is being filtered. Otherwise returns **FALSE**.  
  
## Remarks  
  
-   A column is said to be cross-filtered when a filter applied to another column in the same table or in a related table affects *columnName* by filtering it.  A column is said to be filtered *directly* when the filter or filters apply over the column.  
  
-   The related function [ISFILTERED Function &#40;DAX&#41;](isfiltered-function-dax.md) returns TRUE when *columnName* is filtered directly.  
  
  
## See Also  
[ISFILTERED Function &#40;DAX&#41;](isfiltered-function-dax.md)  
[FILTERS Function &#40;DAX&#41;](filters-function-dax.md)  
[HASONEFILTER Function &#40;DAX&#41;](hasonefilter-function-dax.md)  
[HASONEVALUE Function &#40;DAX&#41;](hasonevalue-function-dax.md)  
  
