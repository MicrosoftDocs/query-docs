---
title: "Text.PadStart | Microsoft Docs"
ms.custom: ""
ms.date: "12/28/2017"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: 2026d85e-adc3-4d2f-adb0-fb34c1e1e724
caps.latest.revision: 6
author: "Minewiskan"
ms.author: "owend"
manager: "erikre"
---
# Text.PadStart
This topic applies to the Power Query Formula Language which can be used with [Power Query](https://support.office.com/article/Introduction-to-Microsoft-Power-Query-for-Excel-6E92E2F4-2079-4E1F-BAD5-89F6269CD605) and [Power BI Desktop](http://go.microsoft.com/fwlink/p/?LinkId=618607) to build queries that mashup data. See the list of [function categories](https://msdn.microsoft.com/en-us/library/mt211003.aspx).  
  
## About  
Returns a text value padded at the beginning with pad to make it at least length characters.  If pad is not specified, whitespace is used as pad.  
  
```  
Text.PadStart(text as nullable text, length as number, optional pad as nullable text) as nullable text  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|text|The text to parse.|  
|length|The length to pad to.|  
|optional pad|The text to pad with.  If pad is not specified, whitespace is used as pad.|  
  
## Examples  
  
```  
Text.PadStart("xyz", 5, "a") equals "aaxyz"  
```  
  
```  
Text.PadStart("xyz", 9, "pad") equals error  
```  
