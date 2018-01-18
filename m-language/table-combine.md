---
title: "Table.Combine | Microsoft Docs"
ms.custom: ""
ms.date: "12/28/2017"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: dbbe7a29-d9a7-4f6b-b2e2-2a24e4e2fd98
caps.latest.revision: 8
author: "Minewiskan"
ms.author: "owend"
manager: "erikre"
---
# Table.Combine
This topic applies to the Power Query Formula Language which can be used with [Power Query](https://support.office.com/article/Introduction-to-Microsoft-Power-Query-for-Excel-6E92E2F4-2079-4E1F-BAD5-89F6269CD605) and [Power BI Desktop](http://go.microsoft.com/fwlink/p/?LinkId=618607) to build queries that mashup data. See the list of [function categories](https://msdn.microsoft.com/en-us/library/mt211003.aspx).  
  
## About  
Returns a table that is the result of merging a list of tables. The tables must all have the same row type structure.  
  
```  
Table.Combine(tables as list) as table  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|tables|The List of tables to combine.|  
  
## Example  
  
```  
Table.Combine({  
  
    Table.FromRecords({  
  
        [CustomerID = 1, Name = "Bob", Phone = "123-4567"],  
  
        [CustomerID = 2, Name = "Jim", Phone = "987-6543"] }),  
  
    Table.FromRecords({  
  
        [CustomerID = 3, Name = "Paul", Phone = "543-7890"]})  
  
    })  
```  
  
|CustomerID|Name|Phone|  
|--------------|--------|---------|  
|1|Bob|123-4567|  
|2|Jim|987-6543|  
|3|Paul|543-7890|  
  
