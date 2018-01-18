---
title: "Text.TrimStart | Microsoft Docs"
ms.custom: ""
ms.date: "12/28/2017"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: 1658d6d5-2f24-434a-b1d8-0fe37b3e9c5f
caps.latest.revision: 5
author: "Minewiskan"
ms.author: "owend"
manager: "erikre"
---
# Text.TrimStart
This topic applies to the Power Query Formula Language which can be used with [Power Query](https://support.office.com/article/Introduction-to-Microsoft-Power-Query-for-Excel-6E92E2F4-2079-4E1F-BAD5-89F6269CD605) and [Power BI Desktop](http://go.microsoft.com/fwlink/p/?LinkId=618607) to build queries that mashup data. See the list of [function categories](https://msdn.microsoft.com/en-us/library/mt211003.aspx).  
  
## About  
Removes any occurrences of the characters in trimChars from the start of the original text value.  
  
```  
Text.TrimStart(text as nullable text, optional trimChars as nullable list) as nullable text  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|text|The text to trim from.|  
|optional trimChars|A character value or a list of character values.|  
  
## <a name="__toc360788916"></a>Remarks  
  
-   If trimChars is not specified, then whitespace characters are trimmed.  
  
