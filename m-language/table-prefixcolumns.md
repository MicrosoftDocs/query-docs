---
title: "Table.PrefixColumns | Microsoft Docs"
ms.custom: ""
ms.date: "12/28/2017"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: 11c519ee-a710-45c9-9367-8b5ef7a7d613
caps.latest.revision: 7
author: "Minewiskan"
ms.author: "owend"
manager: "erikre"
---
# Table.PrefixColumns
This topic applies to the Power Query Formula Language which can be used with [Power Query](https://support.office.com/article/Introduction-to-Microsoft-Power-Query-for-Excel-6E92E2F4-2079-4E1F-BAD5-89F6269CD605) and [Power BI Desktop](http://go.microsoft.com/fwlink/p/?LinkId=618607) to build queries that mashup data. See the list of [function categories](https://msdn.microsoft.com/en-us/library/mt211003.aspx).  
  
## About  
Returns a table where the columns have all been prefixed with a text value.  
  
```  
Table.PrefixColumns(table as table, prefix as text) as table  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|table|The Table to modify.|  
|prefix|The prefix to add to every text value.|  
  
## Example  
  
```  
Table.PrefixColumns(Table.FromRecords(  
  
{  
  
    [CustomerID = 1, Name = "Bob", Phone = "123-4567"]  
  
}  
  
), "MyTable")  
```  
  
|MyTable.CustomerID|MyTable.Name|MyTable.Phone|  
|----------------------|----------------|-----------------|  
|1|Bob|123-4567|  
  
