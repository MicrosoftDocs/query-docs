---
title: "Text.Start | Microsoft Docs"
ms.date: 4/16/2018
ms.prod: power-query
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# Text.Start

  
## About  
Returns the count of characters from the start of a text value.  
  
```  
Text.Start(string as nullable text, count as number) as nullable text  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|string|The string value to parse.|  
|count|The number of characters to return.|  
  
## Example  
  
```  
Text.Start("abcd", 2) equals "ab"  
```  
