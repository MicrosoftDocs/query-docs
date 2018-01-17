---
title: "Table.ReplaceErrorValues | Microsoft Docs"
ms.custom: ""
ms.date: "12/28/2017"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: 8df701a7-479c-4b56-91ee-fe49a31cee81
caps.latest.revision: 5
author: "Minewiskan"
ms.author: "owend"
manager: "erikre"
---
# Table.ReplaceErrorValues
This topic applies to the Power Query Formula Language which can be used with [Power Query](https://support.office.com/article/Introduction-to-Microsoft-Power-Query-for-Excel-6E92E2F4-2079-4E1F-BAD5-89F6269CD605) and [Power BI Desktop](http://go.microsoft.com/fwlink/p/?LinkId=618607) to build queries that mashup data. See the list of [function categories](https://msdn.microsoft.com/en-us/library/mt211003.aspx).  
  
## About  
Replaces the error values in the specified columns with the corresponding specified value.  
  
```  
Table.ReplaceErrorValues(table as table, errorReplacement as list) as table  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|table|The Table to modify.|  
|errorReplacement|The list of columns and the value to replace the errors with. The form of the list is {{column1, value1},?}|  
  
## <a name="__toc360789538"></a>Remarks  
  
-   There may be only one replacement value per column, specifying the column more than one will result in an error  
  
## Example  
  
```  
Table.ReplaceErrorValues(  
  
    Table.FromRows({{1,"hello"},{3,...}}, {"Column1","Column2"}),  
  
    {"Column2", "world"})  
```  
  
|Column1|Column2|  
|-----------|-----------|  
|1|hello|  
|2|world|  
  
