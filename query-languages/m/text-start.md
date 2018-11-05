---
title: "Text.Start | Microsoft Docs"
ms.date: 4/16/2018
ms.service: powerquery

ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# Text.Start

  
## About  
Returns the count of characters from the start of a text value.  
  
## Syntax

<pre>
Text.Start(string as nullable text, count as number) as nullable text  
</pre>
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|string|The string value to parse.|  
|count|The number of characters to return.|  
  
## Example  
  
```powerquery-m
Text.Start("abcd", 2) equals "ab"  
```  
