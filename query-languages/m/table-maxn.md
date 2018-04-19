---
title: "Table.MaxN | Microsoft Docs"
ms.date: 4/16/2018
ms.prod: power-query
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# Table.MaxN

  
## About  
Returns the largest N rows from a table. After the rows are sorted, the countOrCondition parameter must be specified to further filter the result.  
  
```  
Table.MaxN(table as table, comparisonCriteria as any, countOrCondition as any) as table  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|table|The Table to check.|  
|comparisonCriteria|Largest N rows comparison criteria.|  
|countOrCondition|After the rows are sorted, **countOrCondition** further filters the result.|  
  
The **countOrCondition** arument has two possible settings:  
  
|Argument|Description|  
|------------|---------------|  
|as a number|A list of items up to countOrCondition items in ascending order is returned.|  
|as a condition|A list of items that initially meet the condition is returned. Once an item fails the condition, no further items are considered.|  
  
## Examples  
  
```  
Table.MaxN(Employees, "Salary", 3)   
equals  Table.FromRecords({[Name="Jeff", Level=10, Salary=200000]   
[Name="Barb", Level=8,  Salary=150000]   
[Name="Bill", Level=7,  Salary=100000]})  
```  
  
```  
Table.MaxN(Employees, "Salary", each [Level] > 7)  
  
equals  Table.FromRecords( {[Name="Jeff", Level=10, Salary=200000]   
[Name="Barb", Level=8,  Salary=150000]})  
```  
