---
title: "Table.FromRecords | Microsoft Docs"
ms.custom: ""
ms.date: "12/28/2017"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: 3e492f3a-cce8-4066-b902-9cfcb0156b2f
caps.latest.revision: 7
author: "Minewiskan"
ms.author: "owend"
manager: "erikre"
---
# Table.FromRecords
This topic applies to the Power Query Formula Language which can be used with [Power Query](https://support.office.com/article/Introduction-to-Microsoft-Power-Query-for-Excel-6E92E2F4-2079-4E1F-BAD5-89F6269CD605) and [Power BI Desktop](http://go.microsoft.com/fwlink/p/?LinkId=618607) to build queries that mashup data. See the list of [function categories](https://msdn.microsoft.com/en-us/library/mt211003.aspx).  
  
## About  
Returns a table from a list of records.  
  
```  
Table.FromRecords(records as list, optional columns as any) as table  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|records|The List to convert.|  
|optional columns|An optional list of column names, or a table type could be provided as the second argument, which much match names found in the records. Record fields which don?t appear in the list are ignored.|  
  
## <a name="__goback"></a>Examples  
  
```  
Table.FromRecords({  
  
    [CustomerID = 1, Name = "Bob", Phone = "123-4567"],  
  
    [CustomerID = 2, Name = "Jim", Phone = "987-6543"],  
  
    [CustomerID = 3, Name = "Paul", Phone = "543-7890"]})  
```  
  
|CustomerID|Name|Phone|  
|--------------|--------|---------|  
|1|Bob|123-4567|  
|2|Jim|987-6543|  
|3|Paul|543-7890|  
  
