---
title: "UNION function (DAX) | Microsoft Docs"
ms.service: powerbi 
ms.date: 07/13/2020
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend

---
# UNION
  
Creates a union (join) table from a pair of tables.  
  
## Syntax  
  
```dax
UNION(<table_expression1>, <table_expression2> [,<table_expression>]…)  
```
  
### Parameters  
  
|Term|Definition|  
|--------|--------------|  
|table_expression|Any DAX expression that returns a table.|  
  
## Return value

A table that contains all the rows from each of the two table expressions.  
  
## Remarks

- The two tables must have the same number of columns.  
  
- Columns are combined by position in their respective tables.  
  
- The column names in the return table will match the column names in table_expression1.  
  
- Duplicate rows are retained.  
  
- The returned table has lineage where possible. For example, if the first column of each table_expression has lineage to the same base column C1 in the model, the first column in the UNION result will have lineage to C1. However, if combined columns have lineage to different base columns, or if there is an extension column, the resulting column in UNION will have no lineage.  
  
- When data types differ, the resulting data type is determined based on the rules for data type coercion.  
  
- The returned table will not contain columns from related tables.  

- [!INCLUDE [function-not-supported-in-directquery-mode](includes/function-not-supported-in-directquery-mode.md)]

## Example

The following expression creates a union by combining the USAInventory table and the INDInventory table into a single table:  

```dax
UNION(UsaInventory, IndInventory)
```

**USAInventory**
  
|Country|State|Count|Total|  
|-----------|---------|---------|---------|  
|USA|CA|5|500|  
|USA|WA|10|900|  
  
**INDInventory**
  
|Country|State|Count|Total|  
|-----------|---------|---------|---------|  
|IND|JK|20|800|  
|IND|MH|25|1000|  
|IND|WB|10|900|  
  
Return table,  
  
|Country|State|Count|Total|  
|-----------|---------|---------|---------|  
|USA|CA|5|500|  
|USA|WA|10|900|  
|IND|JK|20|800|  
|IND|MH|25|1000|  
|IND|WB|10|900|  
