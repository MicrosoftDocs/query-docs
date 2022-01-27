---
description: "Learn more about: ISCROSSFILTERED"
title: "ISCROSSFILTERED function (DAX) | Microsoft Docs"
ms.service: powerbi 
ms.date: 01/26/2022
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
  
- A column or table is said to be cross-filtered when a filter is applied to *ColumnName*, any column in *TableName*, or to any column in a related table.

- A column or table is said to be filtered directly when a filter is applied to *ColumnName* or to any column in *TableName*. Therefore, the [ISFILTERED](isfiltered-function-dax.md) function also returns TRUE when *ColumnName* or any column in *TableName* is being filtered.  

- A column or table can be both filtered directly and cross-filtered when a filter is applied to *ColumnName* or any column in *TableName*, but cannot be filtered directly if filters are applied only to a different column in the same or a related table.

- [!INCLUDE [function-not-supported-in-directquery-mode](includes/function-not-supported-in-directquery-mode.md)]

## See also

[ISFILTERED function](isfiltered-function-dax.md)  
[FILTERS function](filters-function-dax.md)  
[HASONEFILTER function](hasonefilter-function-dax.md)  
[HASONEVALUE function](hasonevalue-function-dax.md)  
