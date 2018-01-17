---
title: "Table.DemoteHeaders | Microsoft Docs"
ms.custom: ""
ms.date: "12/28/2017"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: 9cbb6d7d-29f1-4f33-8fc7-bede921d5b08
caps.latest.revision: 9
author: "Minewiskan"
ms.author: "owend"
manager: "erikre"
---
# Table.DemoteHeaders
This topic applies to the Power Query Formula Language which can be used with [Power Query](https://support.office.com/article/Introduction-to-Microsoft-Power-Query-for-Excel-6E92E2F4-2079-4E1F-BAD5-89F6269CD605) and [Power BI Desktop](http://go.microsoft.com/fwlink/p/?LinkId=618607) to build queries that mashup data. See the list of [function categories](https://msdn.microsoft.com/en-us/library/mt211003.aspx).  
  
## About  
Demotes the header row down into the first row of a table.  
  
```  
Table.DemoteHeaders(table as table) as table  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|table|The Table to modify.|  
  
## Example  
  
```  
Table.DemoteHeaders(Table.FromRecords(  
  
{  
  
    [CustomerID=1, Name="Bob", Phone = "123-4567" ]  
  
}  
  
))  
```  
  
|Column1|Column2|Column3|  
|-----------|-----------|-----------|  
|CustomerID|Name|Phone|  
|1|Bob|123-4567|  
  
