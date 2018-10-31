---
title: "Table.Min | Microsoft Docs"
ms.date: 4/16/2018
ms.prod: power-query
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# Table.Min

  
## About  
Returns the smallest row or rows from a table using a comparisonCriteria.  
  
## Syntax

<pre>
Table.Min(table as table, comparisonCriteria as any, optional default as any) as table  
</pre>
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|table|The Table to check.|  
|comparisonCriteria|Smallest row or rows comparison criteria.|  
|optional default|Default value.|  
  
## <a name="__toc360789713"></a>Remarks  
  
-   Table.Min is similar to List.Min but requires a table as input.  
  
## Example  
  
```powerquery-m
let  
  
    Employees = Table.FromRecords(  
  
        {[Name="Bill",   Level=7,  Salary=100000],  
  
        [Name="Barb",   Level=8,  Salary=150000],  
  
        [Name="Andrew", Level=6,  Salary=85000],  
  
        [Name="Nikki",  Level=5,  Salary=75000],  
  
        [Name="Margo",  Level=3,  Salary=45000],  
  
        [Name="Jeff",   Level=10, Salary=200000]},  
  
    type table [  
  
        Name = text,  
  
        Level = number,  
  
        Salary = number  
  
])  
  
in  
  
    Table.Min(Employees, "Salary")  
  
equals [Name = "Margo", Level = 3, Salary = 45000]  
```  
  
|||  
|-|-|  
|Name|Margo|  
|Level|3|  
|Salary|45000|  
  
