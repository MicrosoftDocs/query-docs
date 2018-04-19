---
title: "Text.Contains | Microsoft Docs"
ms.date: 4/16/2018
ms.prod: power-query
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# Text.Contains

  
## About  
Returns true if a text value **substring** was found within a text value **string**; otherwise, false.  
  
```  
Text.Contains(string as nullable text, substring as text, optional comparer as nullable function) as nullable logical  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|string|The text to parse.|  
|substring|The text to search for.|  
|optional comparer|The optional culture aware comparer function can be provided.|  
  
## Examples  
  
```  
Text.Contains("abc", "a") equals true  
```  
  
```  
Text.Contains("abc", "d") equals false  
```  
