---
title: "Combiner.CombineTextByLengths | Microsoft Docs"
ms.custom: ""
ms.date: "01/19/2018"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: 1fecaf7b-a933-4b0d-91a8-12327f166943
caps.latest.revision: 6
author: "Minewiskan"
ms.author: "owend"
manager: "kfile"
---
# Combiner.CombineTextByLengths

  
## About  
Returns a function that merges a list of text into a single text.  
  
```  
Combiner.CombineTextByLengths(lengths as list, optional template as nullable text) as function  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|lengths|The lengths to combine on.|  
|optional template|The Combiner template.|  
  
## <a name="__toc360789947"></a>Remarks  
  
-   Combiner.CombineTextByLengths  is similar to CombineTextByRanges, except that the lengths are used to determine the locations of the text.  
  
-   As in Splitter.SplitTextByLengths, each length must be non-negative.  
  
-   As in SplitTextByLengths, CombineTextByLengths works by delegating to CombineTextByRanges.  
  
