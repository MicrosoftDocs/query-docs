---
title: "Table.ContainsAny | Microsoft Docs"
ms.custom: ""
ms.date: "12/28/2017"
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
manager: "erikre"
---
# Table.ContainsAny
This topic applies to the Power Query Formula Language which can be used with [Power Query](https://support.office.com/article/Introduction-to-Microsoft-Power-Query-for-Excel-6E92E2F4-2079-4E1F-BAD5-89F6269CD605) and [Power BI Desktop](http://go.microsoft.com/fwlink/p/?LinkId=618607) to build queries that mashup data. See the list of [function categories](https://msdn.microsoft.com/en-us/library/mt211003.aspx).  
  
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
