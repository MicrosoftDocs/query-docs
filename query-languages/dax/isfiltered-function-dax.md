---
description: "Learn more about: ISFILTERED"
title: "ISFILTERED function (DAX) | Microsoft Docs"
ms.service: powerbi 
ms.subservice: dax 
ms.date: 01/26/2022
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

TRUE when *ColumnName* or a column of *TableName* is being filtered directly. Otherwise returns FALSE.
  
## Remarks  

- A column or table is said to be filtered directly when a filter is applied to *ColumnName* or any column of *TableName*.
  
- A column or table is said to be cross-filtered when a filter is applied to *ColumnName*, any column of *TableName*, or to any column of a related table. Therefore, the [ISCROSSFILTERED](iscrossfiltered-function-dax.md) function also returns TRUE when *ColumnName*, any column of *TableName*, or a column of a related table is filtered.

- [!INCLUDE [function-not-supported-in-directquery-mode](includes/function-not-supported-in-directquery-mode.md)]

## See also

[ISCROSSFILTERED function](iscrossfiltered-function-dax.md)  
[FILTERS function](filters-function-dax.md)  
[HASONEFILTER function](hasonefilter-function-dax.md)  
[HASONEVALUE function](hasonevalue-function-dax.md)  
