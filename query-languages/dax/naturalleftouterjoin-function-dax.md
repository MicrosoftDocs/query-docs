---
title: "NATURALLEFTOUTERJOIN Function (DAX) | Microsoft Docs"
ms.custom: ""
ms.date: "12/28/2017"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "analysis-services"
  - "daxlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: 0cdca2c2-9040-4c72-82d8-551c2465adb1
caps.latest.revision: 7
author: "Minewiskan"
ms.author: "owend"
manager: "kfile"
---
# NATURALLEFTOUTERJOIN Function (DAX)
> [!NOTE]  
> This function is included in SQL Server 2016 Analysis Services (SSAS), Power Pivot in Excel 2016, and Power BI Desktop only. Information provided here is subject to change.  
  
Performs an inner join of a table with another table. The tables are joined on common columns (by name) in the two tables. If the two tables have no common column names, an error is returned.  
  
## Syntax  
  
```  
NATURALLEFTOUTERJOIN(<leftJoinTable>, <rightJoinTable>)  
```  
  
#### Parameters  
  
|Term|Definition|  
|--------|--------------|  
|**leftJoinTable**|A table expression defining the table on the left side of the join.|  
|**rightJoinTable**|A table expression defining the table on the right side of the join.|  
  
## Return Value  
A table which includes only rows from rightJoinTable for which the values in the common columns specified are also present in leftJoinTable. The table returned will have the common columns from the left table and the other columns from both the tables.  
  
## Remarks  
There is no sort order guarantee for the results.  
  
Columns being joined on must have the same data type in both tables.  
  
Only columns from the same source table (have the same lineage) are joined on. For example, Products[ProductID], WebSales[ProductdID], StoreSales[ProductdID] with many-to-one relationships between WebSales and StoreSales and the Products table based on the ProductID column, WebSales and StoreSales tables are joined on [ProductID].  
  
Strict comparison semantics are used during join. There is no type coercion; for example, 1 does not equal 1.0.  
  
