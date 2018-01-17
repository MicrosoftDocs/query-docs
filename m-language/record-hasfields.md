---
title: "Record.HasFields | Microsoft Docs"
ms.custom: ""
ms.date: "12/28/2017"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: a3ce4df9-2f77-4161-a017-3c34dd8f12f1
caps.latest.revision: 6
author: "Minewiskan"
ms.author: "owend"
manager: "erikre"
---
# Record.HasFields
This topic applies to the Power Query Formula Language which can be used with [Power Query](https://support.office.com/article/Introduction-to-Microsoft-Power-Query-for-Excel-6E92E2F4-2079-4E1F-BAD5-89F6269CD605) and [Power BI Desktop](http://go.microsoft.com/fwlink/p/?LinkId=618607) to build queries that mashup data. See the list of [function categories](https://msdn.microsoft.com/en-us/library/mt211003.aspx).  
  
## About  
Returns true if the field name or field names are present in a record.  
  
```  
Record.HasFields(record as record, fields as any) as logical  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|record|The Record to check against.|  
|fields|A text value or a list of text values.|  
  
## <a name="__toc360789150"></a>Examples:  
  
```  
Record.HasFields([CustomerID = 1, Name = "Bob", Phone = "123-4567"],"CustomerID") equals true  
```  
  
```  
Record.HasFields([CustomerID = 1, Name = "Bob", Phone = "123-4567"],{"CustomerID", "Address"}) equals false  
```  
