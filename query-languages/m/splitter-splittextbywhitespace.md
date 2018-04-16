---
title: "Splitter.SplitTextByWhitespace | Microsoft Docs"
ms.date: 4/16/2018
ms.service: powerbi
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# Splitter.SplitTextByWhitespace

  
## About  
Returns a function that splits text according to whitespace.  
  
```  
Splitter.SplitTextByWhitespace(optional quoteStyle as nullable number) as function  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|optional quoteStyle|The quoteStyle acts as described in Lines.FromText.  By default, it is QuoteStyle.Csv.|  
  
## <a name="__toc360789922"></a>Remarks  
  
-   Splitter.SplitTextByWhitespace is similar to SplitTextByAnyDelimiter where the delimiters provided are all characters for which char.IsWhitespace returns true.  
  
SplitTextByWhitespace will consider any non-zero sequence of whitespace characters a delimiter.  
  
