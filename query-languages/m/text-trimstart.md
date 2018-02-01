---
title: "Text.TrimStart | Microsoft Docs"
ms.custom: ""
ms.date: "01/19/2018"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: 1658d6d5-2f24-434a-b1d8-0fe37b3e9c5f
caps.latest.revision: 5
author: "Minewiskan"
ms.author: "owend"
manager: "kfile"
---
# Text.TrimStart

  
## About  
Removes any occurrences of the characters in trimChars from the start of the original text value.  
  
```  
Text.TrimStart(text as nullable text, optional trimChars as nullable list) as nullable text  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|text|The text to trim from.|  
|optional trimChars|A character value or a list of character values.|  
  
## <a name="__toc360788916"></a>Remarks  
  
-   If trimChars is not specified, then whitespace characters are trimmed.  
  
