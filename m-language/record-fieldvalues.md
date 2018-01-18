---
title: "Record.FieldValues | Microsoft Docs"
ms.custom: ""
ms.date: "12/28/2017"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: c2374a35-3e11-4e26-ac38-3b1fb57b9ffd
caps.latest.revision: 6
author: "Minewiskan"
ms.author: "owend"
manager: "erikre"
---
# Record.FieldValues
This topic applies to the Power Query Formula Language which can be used with [Power Query](https://support.office.com/article/Introduction-to-Microsoft-Power-Query-for-Excel-6E92E2F4-2079-4E1F-BAD5-89F6269CD605) and [Power BI Desktop](http://go.microsoft.com/fwlink/p/?LinkId=618607) to build queries that mashup data. See the list of [function categories](https://msdn.microsoft.com/en-us/library/mt211003.aspx).  
  
## About  
Returns a list of field values in order of the record's fields.  
  
```  
Record.FieldValues(record as record) as list  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|record|The record to check.|  
  
## Example  
  
```  
Record.FieldValues( [CustomerID = 1, Name = "Bob", Phone = "123-4567"] ) equals {1, "Bob", "123-4567"}  
```  
