---
title: "Text.RemoveRange | Microsoft Docs"
ms.date: 4/16/2018
ms.prod: power-query
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# Text.RemoveRange

  
## About  
Removes count characters at a zero-based offset from a text value.  
  
## Syntax

<pre>
Text.RemoveRange(text as nullable text, offset as number, count as number) as nullable text  
</pre>
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|text|The text to parse.|  
|offset|The index to start at.|  
|count|The number of characters to remove.|  
  
## <a name="__toc360788862"></a>Remarks  
  
-   If count is not specified, the default value of 1 is used.  
  
-   If offset is less than zero or more than the length of a text value, or if count if less than zero then an Expression.Error is thrown.  
  
## Examples  
  
```powerquery-m
Text.RemoveRange("abcdef", 2) equals "abdef"  
```  
  
```powerquery-m
Text.RemoveRange("abcdef", 2, 2) equals "abef"  
```  
