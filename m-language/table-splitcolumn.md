---
title: "Table.SplitColumn | Microsoft Docs"
ms.custom: ""
ms.date: "12/28/2017"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: 81fbb1b1-ac01-4715-a6ef-7b8e90b631bb
caps.latest.revision: 8
author: "Minewiskan"
ms.author: "owend"
manager: "erikre"
---
# Table.SplitColumn
This topic applies to the Power Query Formula Language which can be used with [Power Query](https://support.office.com/article/Introduction-to-Microsoft-Power-Query-for-Excel-6E92E2F4-2079-4E1F-BAD5-89F6269CD605) and [Power BI Desktop](http://go.microsoft.com/fwlink/p/?LinkId=618607) to build queries that mashup data. See the list of [function categories](https://msdn.microsoft.com/en-us/library/mt211003.aspx).  
  
## About  
Returns a new set of columns from a single column applying a splitter function to each value.  
  
```  
Table.SplitColumn(table as table, sourceColumn as text, splitter as function, optional columnNamesOrNumber as any, optional default as any, optional extraValues as any) as record  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|table|The Table to modify.|  
|sourceColumn|The column to modify.|  
|splitter||  
|columnNamesOrNumber|List of column names that do not conflict with columns from the target table.|  
|optional default|Default value.|  
|extraValues|Handles of extra values or overflow values.|  
  
## Example  
  
```  
let  
  
    Customers = Table.FromRecords({  
  
          [CustomerID = 1, Name = "Bob", Phone = "123-4567"],  
  
          [CustomerID = 2, Name = "Jim", Phone = "987-6543"],  
  
          [CustomerID = 3, Name = "Paul", Phone = "543-7890"],  
  
          [CustomerID = 4, Name = "Ringo", Phone = "232-1550"]  
  
})  
  
in  
  
    Table.SplitColumn(Customers,"Name",Splitter.SplitTextByDelimiter("i"),2)  
```  
  
|CustomerID|Name.1|Name.2|Phone|  
|--------------|----------|----------|---------|  
|1|Bob||123-4567|  
|2|J|m|987-6543|  
|3|Paul||543-7890|  
|4|R|ngo|232-1550|  
  
