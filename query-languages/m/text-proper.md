---
title: "Text.Proper | Microsoft Docs"
ms.date: 4/16/2018
ms.service: powerbi
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# Text.Proper

  
## About  
Returns a text value with first letters of all words converted to uppercase.  
  
```  
Text.Proper(string as nullable text) as nullable text  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|string|The string to transform.|  
  
## Example  
  
```  
Text.Proper("this is an apple") equals "This Is An Apple"  
```  
