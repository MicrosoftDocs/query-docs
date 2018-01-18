---
title: "Record.Field | Microsoft Docs"
ms.custom: ""
ms.date: "12/28/2017"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: c9cddf5e-42b8-4096-ad29-46c43c405e98
caps.latest.revision: 7
author: "Minewiskan"
ms.author: "owend"
manager: "erikre"
---
# Record.Field
This topic applies to the Power Query Formula Language which can be used with [Power Query](https://support.office.com/article/Introduction-to-Microsoft-Power-Query-for-Excel-6E92E2F4-2079-4E1F-BAD5-89F6269CD605) and [Power BI Desktop](http://go.microsoft.com/fwlink/p/?LinkId=618607) to build queries that mashup data. See the list of [function categories](https://msdn.microsoft.com/en-us/library/mt211003.aspx).  
  
## About  
Returns the value of the given field.  This function can be used to dynamically create field lookup syntax for a given record. In that way it is a dynamic verison of the record[field] syntax.  
  
```  
Record.Field(record as record, field as text) as any  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|record|The record to check.|  
|field|The field to obain the value for.|  
  
## <a name="__goback"></a>Example  
  
```  
Record.Field([CustomerID = 1, Name = "Bob", Phone = "123-4567"], "CustomerID") equals 1  
```  
