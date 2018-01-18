---
title: "Record.FieldNames | Microsoft Docs"
ms.custom: ""
ms.date: "12/28/2017"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: 30cc514f-9b96-4d90-af5a-3556aacedf6c
caps.latest.revision: 6
author: "Minewiskan"
ms.author: "owend"
manager: "erikre"
---
# Record.FieldNames
This topic applies to the Power Query Formula Language which can be used with [Power Query](https://support.office.com/article/Introduction-to-Microsoft-Power-Query-for-Excel-6E92E2F4-2079-4E1F-BAD5-89F6269CD605) and [Power BI Desktop](http://go.microsoft.com/fwlink/p/?LinkId=618607) to build queries that mashup data. See the list of [function categories](https://msdn.microsoft.com/en-us/library/mt211003.aspx).  
  
## About  
Returns a list of field names in order of the record's fields.  
  
```  
Record.FieldNames(record as record) as list  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|record|The Record to check.|  
  
## Example  
  
```  
Record.FieldNames( [OrderID = 1, CustomerID = 1, Item = "Fishing rod", Price = 100.0] )  
```  
  
```  
equals {"OrderID","CustomerID", "Bait", "Price"}  
```  
