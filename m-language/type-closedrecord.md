---
title: "Type.ClosedRecord | Microsoft Docs"
ms.custom: ""
ms.date: "12/28/2017"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: f1b7376e-a5e1-41a4-ae91-d6058ad609e9
caps.latest.revision: 5
author: "Minewiskan"
ms.author: "owend"
manager: "erikre"
---
# Type.ClosedRecord
This topic applies to the Power Query Formula Language which can be used with [Power Query](https://support.office.com/article/Introduction-to-Microsoft-Power-Query-for-Excel-6E92E2F4-2079-4E1F-BAD5-89F6269CD605) and [Power BI Desktop](http://go.microsoft.com/fwlink/p/?LinkId=618607) to build queries that mashup data. See the list of [function categories](https://msdn.microsoft.com/en-us/library/mt211003.aspx).  
  
## About  
The given type must be a record type returns a closed version of the given record type (or the same type, if it is already closed)  
  
```  
Type.ClosedRecord(#"type" as type) as type  
```  
  
## Example  
  
```  
Type.ClosedRecord( type [ A = number,?] ) equals type [A=number]  
```  
