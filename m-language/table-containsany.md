---
title: "Table.ContainsAny | Microsoft Docs"
ms.custom: ""
ms.date: "01/19/2018"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: 852ca74a-89dc-4dfb-85fa-8f7c094d3c0f
caps.latest.revision: 7
author: "Minewiskan"
ms.author: "owend"
manager: "kfile"
---
# Table.ContainsAny

  
## About  
Determines whether any of the specified records appear as rows in the table.  
  
```  
Table.ContainsAny(table as table, rows as list, optional equationCriteria as any) as logical  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|table|The Table to check.|  
|rows|The List of rows to check for.|  
|optional equationCriteria|An optional value that specifies how to control comparison between the rows of the table.|  
  
## <a name="__toc360789673"></a>Remarks  
  
-   Table.ContainsAny is similar to List.ContainsAny but requires a table as input.  
  
## <a name="__goback"></a>Example  
  
```  
Table.ContainsAny(  
  
    Table.FromRecords( {[A=1, B=2],[A=2, B=3],[A=3, B=4]}),  
  
    {[A=1, B=2],[A=2, B=4]},  
  
    {"A", "B"}) equals true  
```  
