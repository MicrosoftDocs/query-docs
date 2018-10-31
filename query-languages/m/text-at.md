---
title: "Text.At | Microsoft Docs"
ms.date: 4/16/2018
ms.prod: power-query
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# Text.At

  
## About  
Returns a character starting at a zero-based offset.  
  
## Syntax

<pre>
Text.At(value as nullable text, index as number) as nullable text  
</pre>
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|value|The value to parse.|  
|index|The index of the character to return.|  
  
## <a name="__toc360788840"></a>Remarks  
  
-   If the offset is greater than index, an Expression.Error is thrown.  
  
## Examples  
  
```powerquery-m
Text.At("abcd", 0) equals "a"  
```  
  
```powerquery-m
Text.At("abcd", 5) equals error  
```  
