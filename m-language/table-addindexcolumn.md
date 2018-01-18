---
title: "Table.AddIndexColumn | Microsoft Docs"
ms.custom: ""
ms.date: "12/28/2017"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: 78d8d8ab-f9ce-4328-805b-89bf4ce945da
caps.latest.revision: 8
author: "Minewiskan"
ms.author: "owend"
manager: "erikre"
---
# Table.AddIndexColumn
This topic applies to the Power Query Formula Language which can be used with [Power Query](https://support.office.com/article/Introduction-to-Microsoft-Power-Query-for-Excel-6E92E2F4-2079-4E1F-BAD5-89F6269CD605) and [Power BI Desktop](http://go.microsoft.com/fwlink/p/?LinkId=618607) to build queries that mashup data. See the list of [function categories](https://msdn.microsoft.com/en-us/library/mt211003.aspx).  
  
## About  
Returns a table with a new column with a specific name that, for each row, contains an index of the row in the table.  
  
```  
Table.AddIndexColumn(table as table, newColumnName as text, optional initialValue as nullable number, optional increment as nullable number) as table  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|table|The Table to modify.|  
|newColumnName|The name of the new column.|  
|optional initialValue|The initial column index. The default initial index is 0.|  
|optional increment|The column index increment. The default increment is 1.|  
  
## Examples  
  
```  
Table.AddIndexColumn(Table.FromRecords(  
  
{  
  
      [CustomerID = 1, Name = "Bob", Phone = "123-4567"],  
  
      [CustomerID = 2, Name = "Jim", Phone = "987-6543"] ,  
  
      [CustomerID = 3, Name = "Paul", Phone = "543-7890"] ,  
  
      [CustomerID = 4, Name = "Ringo", Phone = "232-1550"]  
  
}  
  
), "Index")  
```  
  
|CustomerID|Name|Phone|Index|  
|--------------|--------|---------|---------|  
|1|Bob|123-4567|0|  
|2|Jim|987-6543|1|  
|3|Paul|543-7890|2|  
|4|Ringo|232-1550|3|  
  
```  
Table.AddIndexColumn(Table.FromRecords(  
  
{  
  
      [CustomerID = 1, Name = "Bob", Phone = "123-4567"],  
  
      [CustomerID = 2, Name = "Jim", Phone = "987-6543"] ,  
  
      [CustomerID = 3, Name = "Paul", Phone = "543-7890"] ,  
  
      [CustomerID = 4, Name = "Ringo", Phone = "232-1550"]  
  
}  
  
), "Index", 1, 2)  
```  
  
|CustomerID|Name|Phone|Index|  
|--------------|--------|---------|---------|  
|1|Bob|123-4567|1|  
|2|Jim|987-6543|3|  
|3|Paul|543-7890|5|  
|4|Ringo|232-1550|7|  
  
