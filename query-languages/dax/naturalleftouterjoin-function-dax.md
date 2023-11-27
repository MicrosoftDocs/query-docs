---
description: "Learn more about: NATURALLEFTOUTERJOIN"
title: "NATURALLEFTOUTERJOIN function (DAX) | Microsoft Docs"
---
# NATURALLEFTOUTERJOIN
  
Performs a join of the LeftTable with the RightTable by using the Left Outer Join semantics.
  
## Syntax  
  
```dax
NATURALLEFTOUTERJOIN(<LeftTable>, <RightTable>)  
```
  
### Parameters  
  
|Term|Definition|  
|--------|--------------|  
|LeftTable|A table expression defining the table on the left side of the join.|  
|RightTable|A table expression defining the table on the right side of the join.|  
  
## Return value

A table which includes only rows from RightTable for which the values in the common columns specified are also present in LeftTable. The table returned will have the common columns from the left table and the other columns from both the tables.  
  
## Remarks

- Tables are joined on common columns (by name) in the two tables. If the two tables have no common column names, an error is returned.

- There is no sort order guarantee for the results.  
  
- Columns being joined on must have the same data type in both tables.  
  
- Only columns from the same source table (have the same lineage) are joined on. For example, Products[ProductID], WebSales[ProductdID], StoreSales[ProductdID] with many-to-one relationships between WebSales and StoreSales and the Products table based on the ProductID column, WebSales and StoreSales tables are joined on [ProductID].  
  
- Strict comparison semantics are used during join. There is no type coercion; for example, 1 does not equal 1.0.  

- [!INCLUDE [function-not-supported-in-directquery-mode](includes/function-not-supported-in-directquery-mode.md)]

## Related content

[NATURALINNERJOIN](naturalinnerjoin-function-dax.md)
