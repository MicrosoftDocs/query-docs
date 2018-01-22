---
title: "Text.Replace | Microsoft Docs"
ms.custom: ""
ms.date: "01/19/2018"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: 4684c2d5-975a-4f11-a201-b5c8871d2d34
caps.latest.revision: 5
author: "Minewiskan"
ms.author: "owend"
manager: "kfile"
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
