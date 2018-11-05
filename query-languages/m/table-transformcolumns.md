---
title: "Table.TransformColumns | Microsoft Docs"
ms.date: 4/16/2018
ms.service: powerquery

ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# Table.TransformColumns

  
## About  
Transforms columns from a table using a function.  
  
## Syntax

<pre>
Table.TransformColumns(table as table, transformOperations as list, optional defaultTransformation as nullable function, optional missingField as nullable number) as table  
</pre>
  
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
  
```powerquery-m 
Table.TransformColumns(      
Table.FromRecords({[A="1", B=2], [A="5", B=10]}),      
{"A", Number.FromText})   
equals  Table.FromRecords({[A=1,B=2], [A=5,B=10]})  
```  
  
```powerquery-m
Table.TransformColumns(     
Table.FromRecords({[A="1",B=2], [A="5", B=10]}),      
{{"A", Number.FromText},       
{"B", each _ + 1}})   
equals  Table.FromRecords({[A=1,B=3], [A=5,B=11]})  
```  
  
```powerquery-m 
Table.TransformColumns(      
Table.FromRecords({[A="1",B=2], [A="5", B=10]}),      
{"X", Number.FromText})   
equals  Expression.Error  
```  
  
```powerquery-m 
Table.TransformColumns(      
Table.FromRecords({[A="1",B=2], [A="5", B=10]}),      
{"X", Number.FromText},      
MissingField.Ignore)   
equals  Table.FromRecords({[A="1",B=2], [A="5",B=10]})  
```  
  
```powerquery-m
Table.TransformColumns(      
Table.FromRecords({[A="1",B=2], [A="5", B=10]}),      
{"X", Number.FromText},      
MissingField.UseNull)   
equals  Table.FromRecords({[A="1",B=2,X=/* Expression.Error*/],   
[A="5",B=10,X=/* Expression.Error error*/]})  
```  
