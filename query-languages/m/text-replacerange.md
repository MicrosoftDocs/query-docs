---
title: "Text.ReplaceRange | Microsoft Docs"
ms.custom: ""
ms.date: "01/19/2018"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: 5d3440ea-cdf0-440f-9d53-5e763d474100
caps.latest.revision: 6
author: "Minewiskan"
ms.author: "owend"
manager: "kfile"
---
# Text.ReplaceRange

  
## About  
Replaces length characters in a text value starting at a zero-based offset with the new text value.  
  
```  
Text.ReplaceRange(text as nullable text, offset as number, length as number, newText as text) as nullable text  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|text|The text to parse.|  
|offset|The beginning of the range.|  
|length|The length of the range.|  
|newText|The replacement text.|  
  
## Example  
  
```  
Text.ReplaceRange("abcdef", 2, 3, "xyz") equals "abxyzf"  
```  
