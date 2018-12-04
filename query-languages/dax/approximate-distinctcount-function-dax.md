---
title: "APPROXIMATEDISTINCTCOUNT function (DAX) | Microsoft Docs"
ms.service: powerbi 
ms.date: 12/04/2018
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# APPROXIMATEDISTINCTCOUNT function (DAX)

Returns the approximate number of rows that contain distinct values in a column. This function can query large amounts of data with significantly better performance than DISTINCTCOUNT, with slight deviation from the exact result. This function only applies to DirectQuery connections to a limited number of data sources. See Remarks for details.
  
## Syntax  
  
```dax
APPROXIMATEDISTINCTCOUNT(<columnName>)
```
  
#### Parameters  

|Term  |Description|  
|---------|---------|
|column     | The column that contains the values to be counted. This cannot be an expression.  |        

  
## Return value  
The approximate number of distinct values in *column*.  
  
## Remarks  

The only argument allowed to this function is a column. You can use columns containing any type of data. When the function finds no rows to count, it returns a BLANK, otherwise it returns the count of distinct values.

This feature is not available in Intellisense.

This function is currently supported for DirectQuery connections to the following data sources:
- Amazon Redshift
- Azure Databricks
- Azure SQL Database
- Azure SQL Data Warehouse
- Vertica (beta)

  


