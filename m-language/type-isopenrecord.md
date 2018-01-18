---
title: "Type.IsOpenRecord | Microsoft Docs"
ms.custom: ""
ms.date: "12/28/2017"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: 4fa1b072-5b30-41ef-addb-4799200b88f4
caps.latest.revision: 5
author: "Minewiskan"
ms.author: "owend"
manager: "erikre"
---
# Type.IsOpenRecord
This topic applies to the Power Query Formula Language which can be used with [Power Query](https://support.office.com/article/Introduction-to-Microsoft-Power-Query-for-Excel-6E92E2F4-2079-4E1F-BAD5-89F6269CD605) and [Power BI Desktop](http://go.microsoft.com/fwlink/p/?LinkId=618607) to build queries that mashup data. See the list of [function categories](https://msdn.microsoft.com/en-us/library/mt211003.aspx).  
  
## About  
Returns whether a record type is open.  
  
```  
Type.IsOpenRecord(#"type" as type) as logical  
```  
  
## Examples  
  
```  
Type.IsOpenRecord(type [ A = number,?]) equals true  
```  
  
```  
Type.IsOpenRecord(type [ A = number]) equals false  
```  
