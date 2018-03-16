---
title: "Table.MaxN | Microsoft Docs"
ms.custom: ""
ms.date: "01/19/2018"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: ed5bf480-b42c-4874-8966-87194855ebff
caps.latest.revision: 6
author: "Minewiskan"
ms.author: "owend"
manager: "kfile"
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
