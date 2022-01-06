---
description: "Learn more about: ISCROSSFILTERED"
title: "ISCROSSFILTERED function (DAX) | Microsoft Docs"
ms.service: powerbi 
ms.date: 01/04/2022
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend 
recommendations: false

---
# ISCROSSFILTERED

Returns TRUE when the specified table or column is cross-filtered.
  
## Syntax  
  
```dax
ISCROSSFILTERED(<TableNameOrColumnName>)  
```
  
### Parameters  

|Term|Definition|  
|--------|--------------|  
|TableNameOrColumnName|The name of an existing table or column. It cannot be an expression.|
  
## Return value

TRUE when *ColumnName* or a column of *TableName* is being cross-filtered. Otherwise returns FALSE.
  
## Remarks  
  
- A column is said to be cross-filtered when a filter applied to another column in the same table or in a related table affects *ColumnName* by filtering it. A column is said to be filtered *directly* when the filter or filters apply over the column.  
  
- The related function [ISFILTERED function](isfiltered-function-dax.md) returns TRUE when *TableName* or *ColumnName* is filtered directly.  

- [!INCLUDE [function-not-supported-in-directquery-mode](includes/function-not-supported-in-directquery-mode.md)]

## See also

[ISFILTERED function](isfiltered-function-dax.md)  
[FILTERS function](filters-function-dax.md)  
[HASONEFILTER function](hasonefilter-function-dax.md)  
[HASONEVALUE function](hasonevalue-function-dax.md)  
