---
title: "INTERSECT Function (DAX) | Microsoft Docs"
ms.prod: dax
ms.date: 5/22/2018
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# INTERSECT Function (DAX)
Returns the row intersection of two tables, retaining duplicates.  
  
## Syntax  
  
```  
INTERSECT(<table_expression1>, <table_expression2>)  
```  
  
#### Parameters  
  
|Term|Definition|  
|--------|--------------|  
|Table_expression|Any DAX expression that returns a table.|  
  
## Return Value  
A table that contains all the rows in table_expression1 that are also in table_expression2  
  
## Exceptions  
  
## Remarks  
Intersect is not commutative. In general, Intersect(T1, T2) will have a different result set than Intersect(T2, T1).  
  
Duplicate rows are retained. If a row appears in table_expression1 and table_expression2, it and all duplicates in table_expression_1 are included in the result set.  
  
The column names will match the column names in table_expression1.  
  
The returned table has lineage based on the columns in table_expression1 , regardless of the lineage of the columns in the second table. For example, if the first column of first table_expression has lineage to the base column C1 in the model, the intersect will reduce the rows based on the intersect on first column of second table_expression and keep the lineage on base column C1 intact.  
  
Columns are compared based on positioning, and data comparison with no type coercion.  
  
The returned table does not include columns from tables related to table_expression1.  
  
## Example  
States1  
  
|State|  
|---------|  
|A|  
|A|  
|B|  
|B|  
|B|  
|C|  
|D|  
|D|  
  
States2  
  
|State|  
|---------|  
|B|  
|C|  
|D|  
|D|  
|D|  
|E|  
  
Intersect(States1, States2)  
  
|State|  
|---------|  
|B|  
|B|  
|B|  
|C|  
|D|  
|D|  
  
Intersect(States2, States1)  
  
|State|  
|---------|  
|B|  
|C|  
|D|  
|D|  
|D|  
  
