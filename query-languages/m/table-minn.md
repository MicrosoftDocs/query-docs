---
title: "Table.MinN | Microsoft Docs"
ms.date: 4/16/2018
ms.prod: power-query
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# Table.MinN

  
## About  
Returns the smallest N rows in the given table. After the rows are sorted, the countOrCondition parameter must be specified to further filter the result.  
  
## Syntax

<pre>
Table.MinN(table as table, comparisonCriteria as any, countOrCondition as any) as table  
</pre>
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|table|The Table to check.|  
|comparisonCriteria|Smallest N rows comparison criteria.|  
|countOrCondition|After the rows are sorted, countOrCondition further filters the result.|  
  
The **countOrCondition** argument has two possible settings:  
  
|Setting|Description|  
|-----------|---------------|  
|as a number|A list of items up to countOrCondition items in ascending order is returned.|  
|as a condition|A list of items that initially meet the condition is returned. Once an item fails the condition, no further items are considered.|  
  
## Examples  
  
```powerquery-m
Table.MinN(Employees, "Salary", 3) equals  
```  
  
|Name|Level|Salary|  
|--------|---------|----------|  
|Margo|3|45000|  
|Nikki|5|75000|  
|Andrew|6|85000|  
  
```powerquery-m
Table.MinN(Employees, "Salary", each [Level] < 6) equals  
```  
  
|Name|Level|Salary|  
|--------|---------|----------|  
|Margo|3|45000|  
|Nikki|5|75000|  
  
