---
title: "Text.PositionOfAny | Microsoft Docs"
ms.date: 4/16/2018
ms.service: powerquery

ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# Text.PositionOfAny

  
## About  
Returns the first occurrence of a text value in list and returns its position starting at startOffset.  
  
## Syntax

<pre>
Text.PositionOfAny(string as text, list as list, optional occurrence as nullable number) as number  
</pre>
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|string|The string to search for.|  
|list|The list to search through.|  
|optional occurrence|An enum that controls the scope of operation.|  
  
## Settings  
  
|Setting|Description|  
|-----------|---------------|  
|Occurrence.First or Occurrence.Last|A single position is returned.|  
|Occurrence.All|A list of positions is returned for all occurrences.|  
  
## <a name="__toc360788880"></a>Remarks  
  
-   If the text values are not found in the list, -1 is returned.  
  
## Examples  
  
```powerquery-m
List.PositionOfAny("ABCD", {"B","C"}) equals 1  
```  
  
```powerquery-m
List.PositionOfAny("ABCBA", {"A","B"}, Occurrence.First) equals 0  
```  
  
```powerquery-m
List.PositionOfAny("ABCBA", {"A","B"}, Occurrence.Last) equals 4  
```  
  
```powerquery-m
List.PositionOfAny("ABCBA", {"A","B"}, Occurrence.All) equals {0,1,3,4}  
```  
