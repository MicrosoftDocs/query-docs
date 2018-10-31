---
title: "Combiner.CombineTextByDelimiter | Microsoft Docs"
ms.date: 4/16/2018
ms.prod: power-query
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# Combiner.CombineTextByDelimiter

  
## About  
Returns a function that combines a list of text into a single text using the specified delimiter.  
  
## Syntax

<pre> 
Combiner.CombineTextByDelimiter(delimiters as text, optional quoteStyle as nullable number) as function  
</pre> 
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|delimiters|Separates the values.|  
|optional quoteStyle|Determines whether there is quoting within the value that should be used to preserve line breaks and for which delimiters are not significant.|  
  
## <a name="__toc360789935"></a>quoteStyle Settings  
  
|Setting|Description|  
|-----------|---------------|  
|QuoteStyle.None|The text in the list is concatenated.|  
|QuoteStyle.Csv (default)|Values containing quotes, line feeds, or the specified delimiter are escaped to conform to the escaped production of CSV.|  
  
