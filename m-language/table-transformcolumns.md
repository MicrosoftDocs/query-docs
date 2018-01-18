---
title: "Table.TransformColumns | Microsoft Docs"
ms.custom: ""
ms.date: "12/28/2017"
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
manager: "erikre"
---
# Table.TransformColumns
This topic applies to the Power Query Formula Language which can be used with [Power Query](https://support.office.com/article/Introduction-to-Microsoft-Power-Query-for-Excel-6E92E2F4-2079-4E1F-BAD5-89F6269CD605) and [Power BI Desktop](http://go.microsoft.com/fwlink/p/?LinkId=618607) to build queries that mashup data. See the list of [function categories](https://msdn.microsoft.com/en-us/library/mt211003.aspx).  
  
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
