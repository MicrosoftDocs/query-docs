---
title: "Text.PositionOf | Microsoft Docs"
ms.custom: ""
ms.date: "12/28/2017"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: 3b20aed7-bae2-46fe-a1bd-4f43ed2df0da
caps.latest.revision: 6
author: "Minewiskan"
ms.author: "owend"
manager: "erikre"
---
# Text.PositionOf
This topic applies to the Power Query Formula Language which can be used with [Power Query](https://support.office.com/article/Introduction-to-Microsoft-Power-Query-for-Excel-6E92E2F4-2079-4E1F-BAD5-89F6269CD605) and [Power BI Desktop](http://go.microsoft.com/fwlink/p/?LinkId=618607) to build queries that mashup data. See the list of [function categories](https://msdn.microsoft.com/en-us/library/mt211003.aspx).  
  
## About  
Returns the first occurrence of substring in a string and returns its position starting at startOffset.  
  
```  
Text.PositionOf(string as nullable text, substring as text, optional occurrence as nullable number, optional comparer as nullable function) as nullable number  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|string|The text to parse.|  
|substring|The text to string to search for.|  
|optional occurrence|An enum that controls the scope of operation.|  
|optional comparer|The optional culture aware comparer function can be provided.|  
  
## Occurrence Settings  
  
|Setting|Description|  
|-----------|---------------|  
|Occurrence.First or Occurrence.Last|A single position is returned.|  
|Occurrence.All|A list of positions is returned for all occurrences.|  
  
## <a name="__toc360788876"></a>Remarks  
  
-   If a text value is not found, -1 is returned.  
  
## Examples  
  
```  
Text.PositionOf("ABCD", "C") equals 2  
```  
  
```  
Text.PositionOf("ABCBA", "A", Occurrence.First) equals 0  
```  
  
```  
Text.PositionOf("ABCBA", "A", Occurrence.Last) equals 4  
```  
  
```  
Text.PositionOf("ABCBA", "A", Occurrence.All) equals {0,4}  
```  
