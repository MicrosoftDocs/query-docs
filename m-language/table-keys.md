---
title: "Table.Keys | Microsoft Docs"
ms.custom: ""
ms.date: "12/28/2017"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: 337e589b-4ff2-49d1-bcf6-68a3c4f95413
caps.latest.revision: 7
author: "Minewiskan"
ms.author: "owend"
manager: "erikre"
---
# Table.Keys
This topic applies to the Power Query Formula Language which can be used with [Power Query](https://support.office.com/article/Introduction-to-Microsoft-Power-Query-for-Excel-6E92E2F4-2079-4E1F-BAD5-89F6269CD605) and [Power BI Desktop](http://go.microsoft.com/fwlink/p/?LinkId=618607) to build queries that mashup data. See the list of [function categories](https://msdn.microsoft.com/en-us/library/mt211003.aspx).  
  
## About  
Returns a list of key column names from a table.  
  
```  
Table.Keys(table as table) as list  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|table|Table to return a list of key column names from.|  
  
## Example  
  
```  
let  
  
    table = Table.FromRecords(  
  
    {  
  
        [CustomerID = 1, Name = "Bob", Phone = "123-4567"],  
  
        [CustomerID = 2, Name = "Jim", Phone = "987-6543"]  
  
}),  
  
    resultTable = Table.AddKey(table, {"CustomerID"}, true),  
  
    keys = Table.Keys(resultTable),  
  
    #"Table from List" = Table.FromList(keys, Splitter.SplitByNothing(), null, null, ExtraValues.Error),  
  
    #"Expand Column1" = Table.ExpandRecordColumn(#"Table from List", "Column1", {"Columns", "Primary"}, {"Column1.Columns", "Column1.Primary"}),  
  
    #"Expand Column1.Columns" = Table.ExpandListColumn(#"Expand Column1", "Column1.Columns")  
  
in  
  
    #"Expand Column1.Columns"  
```  
  
|Column1.Columns|Column1.Primary|  
|-------------------|-------------------|  
|CustomerID|1|  
  
