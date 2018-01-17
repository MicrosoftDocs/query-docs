---
title: "Text.Combine | Microsoft Docs"
ms.custom: ""
ms.date: "12/28/2017"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: 230d8a0a-7d1a-4de3-b01d-ef42168f0d7c
caps.latest.revision: 5
author: "Minewiskan"
ms.author: "owend"
manager: "erikre"
---
# Text.Combine
This topic applies to the Power Query Formula Language which can be used with [Power Query](https://support.office.com/article/Introduction-to-Microsoft-Power-Query-for-Excel-6E92E2F4-2079-4E1F-BAD5-89F6269CD605) and [Power BI Desktop](http://go.microsoft.com/fwlink/p/?LinkId=618607) to build queries that mashup data. See the list of [function categories](https://msdn.microsoft.com/en-us/library/mt211003.aspx).  
  
## About  
Returns a text value that is the result of joining all text values with each value separated by a separator.  
  
```  
Text.Combine(text as list,  separator as nullable text) as text  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|text|The list of text to combine.|  
|separator|The separator to use when combining.  This will only appear between the specified text values, not at the beginning or the end.|  
  
## Example  
  
```  
Text.Combine({"a", "b", "c"}, ",") equals "a,b,c"  
```  
