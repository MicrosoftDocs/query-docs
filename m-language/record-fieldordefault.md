---
title: "Record.FieldOrDefault | Microsoft Docs"
ms.custom: ""
ms.date: "12/28/2017"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: 72317d05-f7f2-4f48-9426-240db65479cb
caps.latest.revision: 6
author: "Minewiskan"
ms.author: "owend"
manager: "erikre"
---
# Record.FieldOrDefault
This topic applies to the Power Query Formula Language which can be used with [Power Query](https://support.office.com/article/Introduction-to-Microsoft-Power-Query-for-Excel-6E92E2F4-2079-4E1F-BAD5-89F6269CD605) and [Power BI Desktop](http://go.microsoft.com/fwlink/p/?LinkId=618607) to build queries that mashup data. See the list of [function categories](https://msdn.microsoft.com/en-us/library/mt211003.aspx).  
  
## About  
Returns the value of a field from a record, or the default value if the field does not exist.  
  
```  
Record.FieldOrDefault(record as record, field as text, optional defaultValue as any) as any  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|record|The Record to check.|  
|field|The field to return.|  
|optional defaultValue|The default value to return if the field does not exist.|  
  
## Examples  
  
```  
Record.FieldOrDefault([CustomerID =1, Name="Bob"], "Phone") equals null  
```  
  
```  
Record.FieldOrDefault([CustomerID =1, Name="Bob"], "Phone", "123-4567") equals "123-4567"  
```  
