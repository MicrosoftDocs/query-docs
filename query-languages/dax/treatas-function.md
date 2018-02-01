---
title: "TREATAS Function | Microsoft Docs"
ms.custom: ""
ms.date: "12/28/2017"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "daxlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: 9b909c66-949a-4634-bf81-6afda2315cd3
caps.latest.revision: 4
author: "Minewiskan"
ms.author: "owend"
manager: "kfile"
---
# TREATAS Function
Applies the result of a table expression as filters to columns from an unrelated table. 
  
## Syntax  
  
```  
TREATAS(table_expression, <column>[, <column>[, <column>[,…]]]} )  
```  
  
#### Parameters  
  
|Term|Definition|  
|--------|--------------|  
|table_expression|An expression that results in a table.| 
|column|One or more existing columns. It cannot be an expression. |  

## Return Value  

A table that contains all the rows in column(s) that are also in table_expression.
  
## Remarks  
The number of columns specified must match the number of columns in the table expression and be in the same order.

If a value returned in the table expression does not exist in the column, it is ignored. For example, TREATAS({"Red", "Green", "Yellow"}, DimProduct[Color]) sets a filter on column DimProduct[Color] with three values "Red", "Green", and "Yellow". If "Yellow" does not exist in  DimProduct[Color], the effective filter values would are "Red" and "Green".

Best for use when a relationship does not exist between the tables.


## Examples  
In the following example, the model contains two unrelated product tables. If a user applies a filter to DimProduct1[ProductCategory] selecting Bikes, Seats, Tires, the same filter, Bikes, Seats, Tires is applied to DimProduct2[ProductCategory].


```
CALCULATE(
SUM(Sales[Amount]), 
TREATAS(VALUES(DimProduct1[ProductCategory]), DimProduct2[ProductCategory])
)
```

## See Also  
 [INTERSECT Function](intersect-function-dax.md)
 
[FILTER Function](filter-function-dax.md)

  

  
