---
title: "APPROXIMATEDISTINCTCOUNT function (DAX) | Microsoft Docs"
ms.service: powerbi 
ms.date: 12/07/2018
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend

---
# APPROXIMATEDISTINCTCOUNT

> [!IMPORTANT]
> This function is **preview**. It is currently not supported by Microsoft Support. For additional limitations, see [Remarks](#remarks).

Returns the *approximate* number of rows that contain distinct values in a column. This function can query large amounts of data with potentially  better performance than DISTINCTCOUNT, with slight deviation from the exact result. 
  
## Syntax  
  
```dax
APPROXIMATEDISTINCTCOUNT(<columnName>)
```
  
### Parameters  

|Term  |Description|  
|---------|---------|
|column     | The column that contains the values to be counted. This cannot be an expression.  |        

  
## Return value  
The approximate number of distinct values in *column*.  
  
## Remarks  

The only argument to this function is a column. You can use columns containing any type of data. When the function finds no rows to count, it returns a BLANK, otherwise it returns the count of distinct values.

This function is **preview**. The following limitations apply:

- This function currently supports **DirectQuery** connections only to the following data sources:
    - Azure SQL Database
    - Azure SQL Data Warehouse

- This feature is not yet available in Intellisense.
