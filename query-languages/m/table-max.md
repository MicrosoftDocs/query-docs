---
title: "Table.Max | Microsoft Docs"
ms.date: 4/16/2018
ms.prod: power-query
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# Table.Max

  
## About  
Returns the largest row or rows from a table using a comparisonCriteria.  
  
## Syntax

<pre> 
Table.Max(table as table, comparisonCriteria as any, optional default as any) as any  
</pre>
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|table|The Table to check.|  
|comparisonCriteria|largest row or rows comparison criteria.|  
|optional default|Default value.|  
  
## <a name="__toc360789706"></a>Remarks  
Table.Max is similar to List.Max but requires a table as input.  
  
## Example  
  
```powerquery-m 
Table.Max(Employees, "Salary") equals [Name="Jeff", Level=10, Salary=200000]  
```  
  
|||  
|-|-|  
|Name|Jeff|  
|Level|10|  
|Salary|200000|  
  
