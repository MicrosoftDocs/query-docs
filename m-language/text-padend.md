---
title: "Text.PadEnd | Microsoft Docs"
ms.custom: ""
ms.date: "12/28/2017"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: 7e6048a7-6fd2-4eac-b62f-5a89914eb13f
caps.latest.revision: 5
author: "Minewiskan"
ms.author: "owend"
manager: "erikre"
---
# Text.PadEnd
This topic applies to the Power Query Formula Language which can be used with [Power Query](https://support.office.com/article/Introduction-to-Microsoft-Power-Query-for-Excel-6E92E2F4-2079-4E1F-BAD5-89F6269CD605) and [Power BI Desktop](http://go.microsoft.com/fwlink/p/?LinkId=618607) to build queries that mashup data. See the list of [function categories](https://msdn.microsoft.com/en-us/library/mt211003.aspx).  
  
## About  
Returns a text value padded at the end with pad to make it at least length characters.  
  
```  
Text.PadEnd(text as nullable text, length as number, pad as nullable text) as nullable text  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|text|The text to parse.|  
|length|The length to pad to.|  
|pad|The text to pad with.|  
  
## <a name="__toc360788905"></a>Remarks  
  
-   If pad is not specified, whitespace is used as pad.  
  
## Example  
  
```  
Text.PadEnd("abc", 5, "a") equals "abcaa"  
```  
