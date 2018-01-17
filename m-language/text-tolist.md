---
title: "Text.ToList | Microsoft Docs"
ms.custom: ""
ms.date: "12/28/2017"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: be2ad426-18a6-4b86-ac20-a18cc04796f8
caps.latest.revision: 5
author: "Minewiskan"
ms.author: "owend"
manager: "erikre"
---
# Text.ToList
This topic applies to the Power Query Formula Language which can be used with [Power Query](https://support.office.com/article/Introduction-to-Microsoft-Power-Query-for-Excel-6E92E2F4-2079-4E1F-BAD5-89F6269CD605) and [Power BI Desktop](http://go.microsoft.com/fwlink/p/?LinkId=618607) to build queries that mashup data. See the list of [function categories](https://msdn.microsoft.com/en-us/library/mt211003.aspx).  
  
## About  
Returns a list of characters from a text value.  
  
```  
Text.ToList(text as text) as list  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|Text|The text to parse through.|  
  
## Example  
  
```  
Text.ToList("abc") equals {"a","b","c"}  
```  
