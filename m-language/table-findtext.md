---
title: "Table.FindText | Microsoft Docs"
ms.custom: ""
ms.date: "12/28/2017"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: f60fc7cf-ccfe-458e-97f1-37e22c2c7be0
caps.latest.revision: 7
author: "Minewiskan"
ms.author: "owend"
manager: "erikre"
---
# Table.FindText
This topic applies to the Power Query Formula Language which can be used with [Power Query](https://support.office.com/article/Introduction-to-Microsoft-Power-Query-for-Excel-6E92E2F4-2079-4E1F-BAD5-89F6269CD605) and [Power BI Desktop](http://go.microsoft.com/fwlink/p/?LinkId=618607) to build queries that mashup data. See the list of [function categories](https://msdn.microsoft.com/en-us/library/mt211003.aspx).  
  
## About  
Returns a table containing only the rows that have the specified text within one of their cells or any part thereof.  
  
```  
Table.FindText (table as table, text as text) as table  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|table|The Table to modify.|  
|text|The text to compare against.|  
  
## Example  
  
```  
Table.FindText(Table.FromRecords(  
  
{  
  
      [CustomerID = 1, Name = "Bob", Phone = "123-4567"],  
  
      [CustomerID = 2, Name = "Jim", Phone = "987-6543"] ,  
  
      [CustomerID = 3, Name = "Paul", Phone = "543-7890"] ,  
  
      [CustomerID = 4, Name = "Ringo", Phone = "232-1550"]  
  
}  
  
), "Bob")  
```  
  
|CustomerID|Name|Phone|  
|--------------|--------|---------|  
|1|Bob|123-4567|  
  
