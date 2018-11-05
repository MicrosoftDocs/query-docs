---
title: "Combiner.CombineTextByEachDelimiter | Microsoft Docs"
ms.date: 4/16/2018
ms.service: powerquery

ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# Combiner.CombineTextByEachDelimiter

  
## About  
Returns a function that combines a list of text into a single text using each specified delimiter in sequence.  
  
## Syntax

<pre>  
Combiner.CombineTextByEachDelimiter(delimiters as list, optional quoteStyle as number) as function  
</pre>  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|delimiters|The delimiter characters are used to identify at what points to split the string.  The delimiter character is not included in the split values.  A trailing delimiter character will yield an additional empty text value.  The split values contain all characters between the delimiters.  This function will always produce at least one value.|  
|optional quoteStyle|Determines whether there is quoting within the value that should be used to preserve line breaks and for which delimiters are not significant.|  
  
## <a name="__toc360789938"></a>Remarks  
  
-   Combiner.CombineTextByEachDelimiter is similar to CombineTextByDelimiter except that each delimiter is used in turn.  
  
-   An error is thrown by the resulting function if the cardinality of the line passed to it exceeds the cardinality of the delimiters.  
  
