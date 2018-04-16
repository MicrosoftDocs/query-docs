---
title: "Lines.FromText | Microsoft Docs"
ms.date: 4/16/2018
ms.service: powerbi
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# Lines.FromText

  
## About  
Converts a text value to a list of text values split at lines breaks.  
  
```  
Lines.FromText(text as text,  optional quoteStyle as nullable number,  optional includeLineSeparators as nullable logical) as list  
```  
  
## <a name="__toc360789868"></a>Arguments  
  
|Argument|Description|  
|------------|---------------|  
|text|The text to parse.|  
|optional quoteStyle|Style of quote.|  
|optional includeLineSeparators|If includeLineSeparators is true, then the line break characters are included in the text. If a delimiter is specified, then line breaks may appear within quotes|  
  
