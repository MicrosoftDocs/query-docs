---
title: "Table.Min | Microsoft Docs"
ms.custom: ""
ms.date: "01/19/2018"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: 4580f870-b809-4060-9d0c-618b5a0b82b5
caps.latest.revision: 7
author: "Minewiskan"
ms.author: "owend"
manager: "kfile"
---
# Table.Min

  
## About  
Returns the smallest row or rows from a table using a comparisonCriteria.  
  
```  
Table.Min(table as table, comparisonCriteria as any, optional default as any) as table  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|table|The Table to check.|  
|comparisonCriteria|Smallest row or rows comparison criteria.|  
|optional default|Default value.|  
  
## <a name="__toc360789713"></a>Remarks  
  
-   Table.Min is similar to List.Min but requires a table as input.  
  
## Example  
  
```  
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
  
