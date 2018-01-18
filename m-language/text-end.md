---
title: "Text.End | Microsoft Docs"
ms.custom: ""
ms.date: "12/28/2017"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: 31a55b0a-2255-4871-8374-69cba62b4934
caps.latest.revision: 5
author: "Minewiskan"
ms.author: "owend"
manager: "erikre"
---
# Text.End
This topic applies to the Power Query Formula Language which can be used with [Power Query](https://support.office.com/article/Introduction-to-Microsoft-Power-Query-for-Excel-6E92E2F4-2079-4E1F-BAD5-89F6269CD605) and [Power BI Desktop](http://go.microsoft.com/fwlink/p/?LinkId=618607) to build queries that mashup data. See the list of [function categories](https://msdn.microsoft.com/en-us/library/mt211003.aspx).  
  
## About  
Returns the number of characters from the end of a text value.  
  
```  
Text.End(string as nullable text, numChars as number) as nullable text  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|string|The string value to parse.|  
|numChars|The number of characters to return.|  
  
## Example  
  
```  
Text.End("abcd", 2) equals "cd"  
```  
