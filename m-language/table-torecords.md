---
title: "Table.ToRecords | Microsoft Docs"
ms.custom: ""
ms.date: "12/28/2017"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: af5e62d2-28ac-438a-a080-273c6dd4d064
caps.latest.revision: 5
author: "Minewiskan"
ms.author: "owend"
manager: "erikre"
---
# Table.ToRecords
This topic applies to the Power Query Formula Language which can be used with [Power Query](https://support.office.com/article/Introduction-to-Microsoft-Power-Query-for-Excel-6E92E2F4-2079-4E1F-BAD5-89F6269CD605) and [Power BI Desktop](http://go.microsoft.com/fwlink/p/?LinkId=618607) to build queries that mashup data. See the list of [function categories](https://msdn.microsoft.com/en-us/library/mt211003.aspx).  
  
## About  
Returns a list of records from an input table.  
  
```  
Table.ToRecords(table as table) as list  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|table|The Table to convert.|  
  
## Example  
  
```  
Table.ToRecords(Table.FromRows({{"1", "2"}},{"a", "b"})) equals {[a = "1", b = "2"]}  
```  
