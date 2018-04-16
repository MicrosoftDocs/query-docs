---
title: "Table.TransformRows | Microsoft Docs"
ms.date: 4/16/2018
ms.service: powerbi
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# Table.TransformRows

  
## About  
Transforms the rows from a table using a transform function.  
  
```  
Table.TransformRows(table as table, transform as function) as list  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|table|The Table to modify.|  
|transform|The transform function to use.|  
  
## <a name="__toc360789652"></a>Remarks  
  
-   Table.TransformRows is similar to List.Transform but requires a table as input.  
  
## <a name="__goback"></a>Example  
`Table.TransformRows(    Table.FromRecords({[A=1], [A=2], [A=3], [A=4], [A=5]}),    each [A]) equals {1, 2, 3, 4, 5}`  
  
