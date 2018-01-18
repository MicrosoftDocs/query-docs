---
title: "Table.ExpandListColumn | Microsoft Docs"
ms.custom: ""
ms.date: "12/28/2017"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: b7807a22-b0f9-4bd9-af2c-ef4c44d10682
caps.latest.revision: 8
author: "Minewiskan"
ms.author: "owend"
manager: "erikre"
---
# Table.ExpandListColumn
This topic applies to the Power Query Formula Language which can be used with [Power Query](https://support.office.com/article/Introduction-to-Microsoft-Power-Query-for-Excel-6E92E2F4-2079-4E1F-BAD5-89F6269CD605) and [Power BI Desktop](http://go.microsoft.com/fwlink/p/?LinkId=618607) to build queries that mashup data. See the list of [function categories](https://msdn.microsoft.com/en-us/library/mt211003.aspx).  
  
## About  
Given a column of lists in a table, create a copy of a row for each value in its list.  
  
```  
Table.ExpandListColumn(table as table, column as text) as table  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|table|The Table to modify.|  
|column|The column to expand.|  
  
## Example  
  
```  
Table.ExpandListColumn(  
  
    Table.FromRecords(  
  
    {  
  
    [Name= {"Bob", "Jim", "Paul"}, Discount = .15]  
  
}), "Name")  
```  
  
|Name|Discount|  
|--------|------------|  
|Bob|0.15|  
|Jim|0.15|  
|Paul|0.15|  
  
