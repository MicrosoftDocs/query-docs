---
title: "Table.TransformColumns | Microsoft Docs"
ms.custom: ""
ms.date: "01/19/2018"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: 523173e7-96ed-4d33-918b-4329b4be6223
caps.latest.revision: 5
author: "Minewiskan"
ms.author: "owend"
manager: "kfile"
---
# Table.TransformColumns

  
## About  
Transforms columns from a table using a function.  
  
```  
Table.TransformColumns(table as table, transformOperations as list, optional defaultTransformation as nullable function, optional missingField as nullable number) as table  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|table|The Table to modify.|  
|transformOperations|The list of transformOperations to run.|  
|optional defaultTransformation|The default table transformation.|  
|optional missingField|Missing field value.|  
  
## <a name="__toc360789645"></a>Remarks  
  
-   Table.TransformColumns is similar to Record.TransformFields applied to every row in a table.  
  
## Examples  
  
```  
Table.TransformColumns(      
Table.FromRecords({[A="1", B=2], [A="5", B=10]}),      
{"A", Number.FromText})   
equals  Table.FromRecords({[A=1,B=2], [A=5,B=10]})  
```  
  
```  
Table.TransformColumns(     
Table.FromRecords({[A="1",B=2], [A="5", B=10]}),      
{{"A", Number.FromText},       
{"B", each _ + 1}})   
equals  Table.FromRecords({[A=1,B=3], [A=5,B=11]})  
```  
  
```  
Table.TransformColumns(      
Table.FromRecords({[A="1",B=2], [A="5", B=10]}),      
{"X", Number.FromText})   
equals  Expression.Error  
```  
  
```  
Table.TransformColumns(      
Table.FromRecords({[A="1",B=2], [A="5", B=10]}),      
{"X", Number.FromText},      
MissingField.Ignore)   
equals  Table.FromRecords({[A="1",B=2], [A="5",B=10]})  
```  
  
```  
Table.TransformColumns(      
Table.FromRecords({[A="1",B=2], [A="5", B=10]}),      
{"X", Number.FromText},      
MissingField.UseNull)   
equals  Table.FromRecords({[A="1",B=2,X=/* Expression.Error*/],   
[A="5",B=10,X=/* Expression.Error error*/]})  
```  
