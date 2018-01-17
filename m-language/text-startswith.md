---
title: "Text.StartsWith | Microsoft Docs"
ms.custom: ""
ms.date: "12/28/2017"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: 474a1a8b-1abf-41c3-8a79-be96134f097e
caps.latest.revision: 5
author: "Minewiskan"
ms.author: "owend"
manager: "erikre"
---
# Text.StartsWith
This topic applies to the Power Query Formula Language which can be used with [Power Query](https://support.office.com/article/Introduction-to-Microsoft-Power-Query-for-Excel-6E92E2F4-2079-4E1F-BAD5-89F6269CD605) and [Power BI Desktop](http://go.microsoft.com/fwlink/p/?LinkId=618607) to build queries that mashup data. See the list of [function categories](https://msdn.microsoft.com/en-us/library/mt211003.aspx).  
  
## About  
Returns a logical value indicating whether a text value substring was found at the beginning of a string.  
  
**Note**: Only comparer functions created through the library (Comparer.FromCulture) are supported.  
  
```  
Text.StartsWith(string as nullable text, substring as text, optional comparer as nullable function) as nullable logical  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|string|The text value to parse.|  
|substring|The string to search for.|  
|optional comparer|An optional comparer can be provided to influence the result.|  
  
