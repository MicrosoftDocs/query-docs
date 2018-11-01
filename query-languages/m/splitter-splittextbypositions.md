---
title: "Splitter.SplitTextByPositions | Microsoft Docs"
ms.date: 4/16/2018
ms.service: powerquery

ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# Splitter.SplitTextByPositions

  
## About  
Returns a function that splits text according to the specified positions.  
  
## Syntax

<pre> 
Splitter.SplitTextByPositions(positions as list) as function  
</pre>
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|positions|The positions to split on.|  
  
## <a name="__toc360789928"></a>Remarks  
  
-   Each item in positions should be a non-negative number indicating the position at which to break the text, and each item must be greater than or equal to the previous.  SplitTextByPositions works by computing a set of ranges by using the difference between subsequent positions as lengths (with the last position of effectively infinite length) and delegating to SplitTextByRanges.  The list returned will have the same cardinality as that of the positions.  
  
