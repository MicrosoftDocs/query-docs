---
title: "Text.PositionOfAny | Microsoft Docs"
ms.custom: ""
ms.date: "01/19/2018"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: 1cb5ff59-88c1-4b12-9a02-276e51849d6c
caps.latest.revision: 6
author: "Minewiskan"
ms.author: "owend"
manager: "kfile"
---
# Text.PositionOfAny

  
## About  
Returns the first occurrence of a text value in list and returns its position starting at startOffset.  
  
```  
Text.PositionOfAny(string as text, list as list, optional occurrence as nullable number) as number  
```  
  
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
  
```  
List.PositionOfAny("ABCD", {"B","C"}) equals 1  
```  
  
```  
List.PositionOfAny("ABCBA", {"A","B"}, Occurrence.First) equals 0  
```  
  
```  
List.PositionOfAny("ABCBA", {"A","B"}, Occurrence.Last) equals 4  
```  
  
```  
List.PositionOfAny("ABCBA", {"A","B"}, Occurrence.All) equals {0,1,3,4}  
```  
