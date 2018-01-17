---
title: "Table.TransformColumnTypes | Microsoft Docs"
ms.custom: ""
ms.date: "12/28/2017"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: d70e2e34-479c-4663-aebf-e8bcf69ecd59
caps.latest.revision: 7
author: "Minewiskan"
ms.author: "owend"
manager: "erikre"
---
# Table.TransformColumnTypes
This topic applies to the Power Query Formula Language which can be used with [Power Query](https://support.office.com/article/Introduction-to-Microsoft-Power-Query-for-Excel-6E92E2F4-2079-4E1F-BAD5-89F6269CD605) and [Power BI Desktop](http://go.microsoft.com/fwlink/p/?LinkId=618607) to build queries that mashup data. See the list of [function categories](https://msdn.microsoft.com/en-us/library/mt211003.aspx).  
  
## About  
Transforms the column types from a table using a type.  
  
```  
Table.TransformColumnTypes(table as table, typeTransformations as list, optional culture as nullable text) as table  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|table|The Table to modify.|  
|typeTransformations|The List of typeTransofrmations to make.|  
|optional culture|A text value corresponding to the culture values supported on your version of Windows, such as "en-US". If the culture is not specified, the current user culture is used. For a list of culture names, see [National Language Support (NLS) API Reference](http://msdn.microsoft.com/en-us/goglobal/bb896001.aspx).|  
  
## Examples  
  
```  
Table.TransformColumnTypes(  
 Table.FromRecords({  
 [A="1",B=2], [A="5", B=10]}),   
 {"A", type number})  
  
 equals Table.FromRecords({  
 [A=1,B=2], [A=5,B=10]})  
```  
  
```  
Table.TransformColumnTypes(  
 Table.FromRecords({  
 [A="1",B=2],   
 [A="5", B=10]}),  
 {"X", type number})  
  
 equals Expression.Error  
```  
  
```  
Table.TransformColumnTypes(  
 Table.FromRecords({  
 [A="1/10/1990",B="29,000"],   
 [A="2/10/1990", B="29.000"]}),   
 {{"A", type date}, {"B", type number}}, "en-US")  
  
 equals Table.FromRecords({  
 [A=#date(1990, 10, 1),B=29000],   
 [A=#date(1990, 10, 2),B=29]})  
```  
