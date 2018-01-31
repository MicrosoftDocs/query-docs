---
title: "Lines.FromText | Microsoft Docs"
ms.custom: ""
ms.date: "01/19/2018"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: 11dd6cac-1644-408c-8a45-3f5ecf76b646
caps.latest.revision: 5
author: "Minewiskan"
ms.author: "owend"
manager: "kfile"
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
  
