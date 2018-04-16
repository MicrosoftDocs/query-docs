---
title: "Text.Replace | Microsoft Docs"
ms.date: 4/16/2018
ms.service: powerbi
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# Text.Replace

  
## About  
Replaces all occurrences of a substring with a new text value.  
  
```  
Text.Replace (text as nullable text, old as text, new as text) as nullable text  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|text|The text to parse.|  
|old|The text to replace.|  
|new|The replacement text.|  
  
## Example  
  
```  
Text.Replace("Thisisanorange", "orange", "apple") equals "Thisisanapple"  
```  
