---
title: "Table.TransformRows | Microsoft Docs"
ms.custom: ""
ms.date: "12/28/2017"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: 1ba121ec-2efc-47fd-b4e2-1ec15b295bba
caps.latest.revision: 5
author: "Minewiskan"
ms.author: "owend"
manager: "erikre"
---
# Table.TransformRows
This topic applies to the Power Query Formula Language which can be used with [Power Query](https://support.office.com/article/Introduction-to-Microsoft-Power-Query-for-Excel-6E92E2F4-2079-4E1F-BAD5-89F6269CD605) and [Power BI Desktop](http://go.microsoft.com/fwlink/p/?LinkId=618607) to build queries that mashup data. See the list of [function categories](https://msdn.microsoft.com/en-us/library/mt211003.aspx).  
  
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
  
