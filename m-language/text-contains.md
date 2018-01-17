---
title: "Text.Contains | Microsoft Docs"
ms.custom: ""
ms.date: "12/28/2017"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: 88e751e2-b418-45c8-bee3-c84f944ef22a
caps.latest.revision: 5
author: "Minewiskan"
ms.author: "owend"
manager: "erikre"
---
# Text.Contains
This topic applies to the Power Query Formula Language which can be used with [Power Query](https://support.office.com/article/Introduction-to-Microsoft-Power-Query-for-Excel-6E92E2F4-2079-4E1F-BAD5-89F6269CD605) and [Power BI Desktop](http://go.microsoft.com/fwlink/p/?LinkId=618607) to build queries that mashup data. See the list of [function categories](https://msdn.microsoft.com/en-us/library/mt211003.aspx).  
  
## About  
Returns true if a text value **substring** was found within a text value **string**; otherwise, false.  
  
```  
Text.Contains(string as nullable text, substring as text, optional comparer as nullable function) as nullable logical  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|string|The text to parse.|  
|substring|The text to search for.|  
|optional comparer|The optional culture aware comparer function can be provided.|  
  
## Examples  
  
```  
Text.Contains("abc", "a") equals true  
```  
  
```  
Text.Contains("abc", "d") equals false  
```  
