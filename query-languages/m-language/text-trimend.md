---
title: "Text.TrimEnd | Microsoft Docs"
ms.custom: ""
ms.date: "01/19/2018"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: 18ba02f0-2454-4145-ab97-586bbdea117e
caps.latest.revision: 5
author: "Minewiskan"
ms.author: "owend"
manager: "kfile"
---
# Text.TrimEnd

  
## About  
Removes any occurrences of the characters specified in trimChars from the end of the original text value.  
  
```  
Text.TrimEnd(text as nullable text,  optional trimChars as nullable list) as nullable text  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|text|The text to trim from.|  
|optional trimChars|A character value or a list of character values. If trimChars is not specified, then whitespace characters are trimmed.|  
  
