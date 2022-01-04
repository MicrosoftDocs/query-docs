---
description: "Learn more about: ISFILTERED"
title: "ISFILTERED function (DAX) | Microsoft Docs"
ms.service: powerbi 
ms.date: 01/04/2022
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend 
recommendations: false

---
# ISFILTERED

Returns TRUE when the specified table or column is being filtered directly.
  
## Syntax  
  
```dax
ISFILTERED(<TableNameOrColumnName>)  
```
  
### Parameters  

|Term|Definition|  
|--------|--------------|  
|TableNameOrColumnName|The name of an existing table or column. It cannot be an expression.|
  
## Return value

TRUE when *ColumnName* or a column of *TableName* is being filtered directly. If there is no filter or if the filtering happens because a different column in the same table or in a related table is being filtered, then FALSE is returned.  
  
## Remarks  
  
- *ColumnName* is said to be filtered directly when the filter or filters apply over the column. A column is said to be cross-filtered when a filter applied to another column in the same table or in a related table affects *ColumnName* by filtering it as well.  
  
- The related function [ISCROSSFILTERED](iscrossfiltered-function-dax.md) returns TRUE when *TableName* or *ColumnName* or another column in the same or related table is being filtered.  

- [!INCLUDE [function-not-supported-in-directquery-mode](includes/function-not-supported-in-directquery-mode.md)]

## See also

[ISCROSSFILTERED function](iscrossfiltered-function-dax.md)  
[FILTERS function](filters-function-dax.md)  
[HASONEFILTER function](hasonefilter-function-dax.md)  
[HASONEVALUE function](hasonevalue-function-dax.md)  
