---
title: "Text.SplitAny | Microsoft Docs"
ms.custom: ""
ms.date: "12/28/2017"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: f6c87f47-6ff7-4875-9673-b9beba433738
caps.latest.revision: 5
author: "Minewiskan"
ms.author: "owend"
manager: "erikre"
---
# Text.SplitAny
This topic applies to the Power Query Formula Language which can be used with [Power Query](https://support.office.com/article/Introduction-to-Microsoft-Power-Query-for-Excel-6E92E2F4-2079-4E1F-BAD5-89F6269CD605) and [Power BI Desktop](http://go.microsoft.com/fwlink/p/?LinkId=618607) to build queries that mashup data. See the list of [function categories](https://msdn.microsoft.com/en-us/library/mt211003.aspx).  
  
## About  
Returns a list containing parts of a text value that are delimited by any separator text values.  
  
```  
Text.SplitAny(string as text,  separator as text) as list  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|string|The string to parse.|  
|separator|A delimiter value.|  
  
