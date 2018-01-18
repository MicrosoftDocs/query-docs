---
title: "Table.InsertRows | Microsoft Docs"
ms.custom: ""
ms.date: "12/28/2017"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: eb5d977c-9a6f-46a5-9e64-9b4563f28ec6
caps.latest.revision: 8
author: "Minewiskan"
ms.author: "owend"
manager: "erikre"
---
# Table.InsertRows
This topic applies to the Power Query Formula Language which can be used with [Power Query](https://support.office.com/article/Introduction-to-Microsoft-Power-Query-for-Excel-6E92E2F4-2079-4E1F-BAD5-89F6269CD605) and [Power BI Desktop](http://go.microsoft.com/fwlink/p/?LinkId=618607) to build queries that mashup data. See the list of [function categories](https://msdn.microsoft.com/en-us/library/mt211003.aspx).  
  
## About  
Returns a table with the list of rows inserted into the table at an index. Each row to insert must match the row type of the table..  
  
```  
Table.InsertRows(table as table, offset as number, rows as list) as table  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|table|The Table to insert rows into.|  
|offset|The row number to insert at.|  
|rows|The List of rows to insert.|  
  
## Remark  
  
-   Table.InsertRows is similar to List.InsertRange but requires a table as input.  
  
## Example  
  
```  
Table.InsertRows(Table.FromRecords({  
  
    [CustomerID = 1, Name = "Bob", Phone = "123-4567"],  
  
    [CustomerID = 2, Name = "Jim", Phone = "987-6543"] }),  
  
    2,  
  
    { [CustomerID = 3, Name = "Paul", Phone = "543-7890"] })  
  
Table.InsertRows(Table.FromRecords({  
  
    [CustomerID = 1, Name = "Bob", Phone = "123-4567"],  
  
    [CustomerID = 2, Name = "Jim", Phone = "987-6543"] }),  
  
    2,  
  
    { [CustomerID = 3, Name = "Paul", Phone = "543-7890"] })  
```  
  
|CustomerID|Name|Phone|  
|--------------|--------|---------|  
|1|Bob|123-4567|  
|2|Jim|987-6543|  
|3|Paul|543-7890|  
  
