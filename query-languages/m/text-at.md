---
title: "Text.At | Microsoft Docs"
ms.date: 4/16/2018
ms.service: powerbi
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# Text.At

  
## About  
Returns a character starting at a zero-based offset.  
  
```  
Text.At(value as nullable text, index as number) as nullable text  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|value|The value to parse.|  
|index|The index of the character to return.|  
  
## <a name="__toc360788840"></a>Remarks  
  
-   If the offset is greater than index, an Expression.Error is thrown.  
  
## Examples  
  
```  
Text.At("abcd", 0) equals "a"  
```  
  
```  
Text.At("abcd", 5) equals error  
```  
