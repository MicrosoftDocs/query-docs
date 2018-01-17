---
title: "Table.FromList | Microsoft Docs"
ms.custom: ""
ms.date: "12/28/2017"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: 417691ac-74f6-4331-8c4a-893da2d72d5a
caps.latest.revision: 7
author: "Minewiskan"
ms.author: "owend"
manager: "erikre"
---
# Table.FromList
This topic applies to the Power Query Formula Language which can be used with [Power Query](https://support.office.com/article/Introduction-to-Microsoft-Power-Query-for-Excel-6E92E2F4-2079-4E1F-BAD5-89F6269CD605) and [Power BI Desktop](http://go.microsoft.com/fwlink/p/?LinkId=618607) to build queries that mashup data. See the list of [function categories](https://msdn.microsoft.com/en-us/library/mt211003.aspx).  
  
## About  
Converts a list into a table by applying the specified splitting function to each item in the list.  
  
```  
Table.FromList(list as list, optional splitter as nullable function, optional columns as any, optional default as any, optional extraValues as any) as table  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|list|The List to convert.|  
|optional splitter|Splitter function.|  
|optional columns|A list of text values specifying the column names of the resulting table.|  
|optional default|A default can be provided to be used for missing values in the table.|  
|optional extraValues|Extra values for each item in the list.|  
  
## Example  
  
```  
Table.FromList(  
  
    {[CustomerID =1, Name ="Bob", Phone = "123-4567"] ,  
  
    [CustomerID =2, Name ="Jim", Phone = "987-6543"]},  
  
    Record.FieldValues, {"CustomerID", "Name", "Phone"})  
```  
  
|CustomerID|Name|Phone|  
|--------------|--------|---------|  
|1|Bob|123-4567|  
|2|Jim|987-6543|  
  
