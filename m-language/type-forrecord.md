---
title: "Type.ForRecord | Microsoft Docs"
ms.custom: ""
ms.date: "12/28/2017"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: 0bbaa332-a3b4-4cc2-8311-1a11a837957f
caps.latest.revision: 5
author: "Minewiskan"
ms.author: "owend"
manager: "erikre"
---
# Type.ForRecord
This topic applies to the Power Query Formula Language which can be used with [Power Query](https://support.office.com/article/Introduction-to-Microsoft-Power-Query-for-Excel-6E92E2F4-2079-4E1F-BAD5-89F6269CD605) and [Power BI Desktop](http://go.microsoft.com/fwlink/p/?LinkId=618607) to build queries that mashup data. See the list of [function categories](https://msdn.microsoft.com/en-us/library/mt211003.aspx).  
  
## About  
Returns a Record type from a fields record.  
  
```  
Type.ForRecord(fields as record, open as logical) as type  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|fields|The record to convert.|  
|open|A logical value indicating if the returned type should be an open record.|  
  
## Example  
  
```  
Type.ForRecord(  
[  
X = [Type = type number, Optional = false],   
Y = [Type = type number, Optional = true]], true)  
equals type [ X = number, optional Y = number,...   
]  
```  
