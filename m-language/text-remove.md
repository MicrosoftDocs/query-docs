---
title: "Text.Remove | Microsoft Docs"
ms.custom: ""
ms.date: "12/28/2017"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: 472c8c4f-282d-4576-9787-d0b8d3802e1b
caps.latest.revision: 5
author: "Minewiskan"
ms.author: "owend"
manager: "erikre"
---
# Text.Remove
This topic applies to the Power Query Formula Language which can be used with [Power Query](https://support.office.com/article/Introduction-to-Microsoft-Power-Query-for-Excel-6E92E2F4-2079-4E1F-BAD5-89F6269CD605) and [Power BI Desktop](http://go.microsoft.com/fwlink/p/?LinkId=618607) to build queries that mashup data. See the list of [function categories](https://msdn.microsoft.com/en-us/library/mt211003.aspx).  
  
## About  
Removes all occurrences of a character or list of characters from a text value. The **removeChars** parameter can be a character value or a list of character values.  
  
```  
Text.Remove(text as nullable text, removeChars as any) as nullable text  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|text|The text to parse.|  
|removeChars|A character value or a list of character values to be removed.|  
  
## Examples  
  
```  
Text.Remove("a,b,;c",",")equals "ab;c"  
```  
  
```  
Text.Remove("a,b,;c",{",",";"}) equals "abc"  
```  
