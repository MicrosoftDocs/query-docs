---
title: "Text.Repeat | Microsoft Docs"
ms.custom: ""
ms.date: "12/28/2017"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: 333b3a8a-1c6d-4e51-9ea7-9c6de7e38504
caps.latest.revision: 5
author: "Minewiskan"
ms.author: "owend"
manager: "erikre"
---
# Text.Repeat
This topic applies to the Power Query Formula Language which can be used with [Power Query](https://support.office.com/article/Introduction-to-Microsoft-Power-Query-for-Excel-6E92E2F4-2079-4E1F-BAD5-89F6269CD605) and [Power BI Desktop](http://go.microsoft.com/fwlink/p/?LinkId=618607) to build queries that mashup data. See the list of [function categories](https://msdn.microsoft.com/en-us/library/mt211003.aspx).  
  
## About  
Returns a text value composed of the input text value repeated a number of times.  
  
```  
Text.Repeat(string as text, repeatCount as number) as text  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|string|The text to repeat.|  
|repeatCount|The number of times to repeat the text.|  
  
## Example  
  
```  
Text.Repeat("a",5) equals "aaaaa"  
```  
