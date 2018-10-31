---
title: "Text.End | Microsoft Docs"
ms.date: 4/16/2018
ms.prod: power-query
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# Text.End

  
## About  
Returns the number of characters from the end of a text value.  
  
## Syntax

<pre>
Text.End(string as nullable text, numChars as number) as nullable text  
</pre> 
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|string|The string value to parse.|  
|numChars|The number of characters to return.|  
  
## Example  
  
```powerquery-m 
Text.End("abcd", 2) equals "cd"  
```  
