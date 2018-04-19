---
title: "Text.Trim | Microsoft Docs"
ms.date: 4/16/2018
ms.prod: power-query
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# Text.Trim

  
## About  
Removes any occurrence of character pattern in trimChars from text.  
  
```  
Text.Trim(text as nullable text, optional trimChars as any) as nullable text  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|text|The text to trim from.|  
|optional trimChars|A character value or a list of character values.|  
  
## <a name="__toc360788912"></a>Remarks  
  
-   Characters are removed from the beginning and end of the text value.  
  
-   If trimChars is not specified, then whitespace characters are trimmed. Whitespace characters are defined by the Power Query formula language specification document. trimChar is either a character value or a list of character values.  
  
## <a name="__toc360788913"></a>Examples  
  
```  
Text.Trim("xyAyz", "x") equals "yAyz"  
```  
**Where**: x is removed.  
  
```  
Text.Trim("xyAyz", {"x","y"}) equals "Ayz"  
```  
**Where**: x and y are removed.  
  
```  
Text.Trim("xyAyz", {"x","y","z"}) equals "A"  
```  
**Where**:  
  
1.  The first x, y and z pattern is removed.  
  
2.  **AND** the second x, y and z pattern is removed  
  
```  
Text.Trim("xyAyz", "xy") equals error  
```  
