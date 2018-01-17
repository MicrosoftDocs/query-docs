---
title: "Text.ReplaceRange | Microsoft Docs"
ms.custom: ""
ms.date: "12/28/2017"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: 5d3440ea-cdf0-440f-9d53-5e763d474100
caps.latest.revision: 6
author: "Minewiskan"
ms.author: "owend"
manager: "erikre"
---
# Text.ReplaceRange
This topic applies to the Power Query Formula Language which can be used with [Power Query](https://support.office.com/article/Introduction-to-Microsoft-Power-Query-for-Excel-6E92E2F4-2079-4E1F-BAD5-89F6269CD605) and [Power BI Desktop](http://go.microsoft.com/fwlink/p/?LinkId=618607) to build queries that mashup data. See the list of [function categories](https://msdn.microsoft.com/en-us/library/mt211003.aspx).  
  
## About  
Replaces length characters in a text value starting at a zero-based offset with the new text value.  
  
```  
Text.ReplaceRange(text as nullable text, offset as number, length as number, newText as text) as nullable text  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|text|The text to parse.|  
|offset|The beginning of the range.|  
|length|The length of the range.|  
|newText|The replacement text.|  
  
## Example  
  
```  
Text.ReplaceRange("abcdef", 2, 3, "xyz") equals "abxyzf"  
```  
