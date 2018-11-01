---
title: "Combiner.CombineTextByLengths | Microsoft Docs"
ms.date: 4/16/2018
ms.service: powerquery

ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# Combiner.CombineTextByLengths

  
## About  
Returns a function that merges a list of text into a single text.  
  
## Syntax

<pre> 
Combiner.CombineTextByLengths(lengths as list, optional template as nullable text) as function  
</pre> 
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|lengths|The lengths to combine on.|  
|optional template|The Combiner template.|  
  
## <a name="__toc360789947"></a>Remarks  
  
-   Combiner.CombineTextByLengths  is similar to CombineTextByRanges, except that the lengths are used to determine the locations of the text.  
  
-   As in Splitter.SplitTextByLengths, each length must be non-negative.  
  
-   As in SplitTextByLengths, CombineTextByLengths works by delegating to CombineTextByRanges.  
  
