---
title: "Text.PadStart | Microsoft Docs"
ms.date: 4/16/2018
ms.service: powerbi
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# Text.PadStart

  
## About  
Returns a text value padded at the beginning with pad to make it at least length characters.  If pad is not specified, whitespace is used as pad.  
  
```  
Text.PadStart(text as nullable text, length as number, optional pad as nullable text) as nullable text  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|text|The text to parse.|  
|length|The length to pad to.|  
|optional pad|The text to pad with.  If pad is not specified, whitespace is used as pad.|  
  
## Examples  
  
```  
Text.PadStart("xyz", 5, "a") equals "aaxyz"  
```  
  
```  
Text.PadStart("xyz", 9, "pad") equals error  
```  
