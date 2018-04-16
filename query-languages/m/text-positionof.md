---
title: "Text.PositionOf | Microsoft Docs"
ms.date: 4/16/2018
ms.service: powerbi
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# Text.PositionOf

  
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
