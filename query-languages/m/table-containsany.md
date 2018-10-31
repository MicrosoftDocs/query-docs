---
title: "Table.ContainsAny | Microsoft Docs"
ms.date: 4/16/2018
ms.prod: power-query
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# Table.ContainsAny

  
## About  
Determines whether any of the specified records appear as rows in the table.  
  
## Syntax

<pre>
Table.ContainsAny(table as table, rows as list, optional equationCriteria as any) as logical  
</pre>
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|table|The Table to check.|  
|rows|The List of rows to check for.|  
|optional equationCriteria|An optional value that specifies how to control comparison between the rows of the table.|  
  
## <a name="__toc360789673"></a>Remarks  
  
-   Table.ContainsAny is similar to List.ContainsAny but requires a table as input.  
  
## <a name="__goback"></a>Example  
  
```powerquery-m
Table.ContainsAny(  
  
    Table.FromRecords( {[A=1, B=2],[A=2, B=3],[A=3, B=4]}),  
  
    {[A=1, B=2],[A=2, B=4]},  
  
    {"A", "B"}) equals true  
```  
