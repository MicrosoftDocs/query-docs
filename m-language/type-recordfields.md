---
title: "Type.RecordFields | Microsoft Docs"
ms.custom: ""
ms.date: "12/28/2017"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: afaaee3e-a41c-4225-89b4-4ae7e06609f1
caps.latest.revision: 6
author: "Minewiskan"
ms.author: "owend"
manager: "erikre"
---
# Type.RecordFields
This topic applies to the Power Query Formula Language which can be used with [Power Query](https://support.office.com/article/Introduction-to-Microsoft-Power-Query-for-Excel-6E92E2F4-2079-4E1F-BAD5-89F6269CD605) and [Power BI Desktop](http://go.microsoft.com/fwlink/p/?LinkId=618607) to build queries that mashup data. See the list of [function categories](https://msdn.microsoft.com/en-us/library/mt211003.aspx).  
  
## About  
Returns a record describing the fields of a record type with each field of the returned record type having a corresponding name and a value that is a record of the form [ Type = type, Opional = logical ].  
  
```  
Type.RecordFields(#"type" as type) as record  
```  
  
## Example  
  
```  
Type.RecordFields(type [ A = number, optional B = any])  
equals [  
A = [Type = number, Optional = false],  
B = [Type = any, Optional = true]  
]  
```  
