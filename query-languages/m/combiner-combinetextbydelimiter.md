---
title: "Combiner.CombineTextByDelimiter | Microsoft Docs"
ms.custom: ""
ms.date: "01/19/2018"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: b5f31a9a-03ec-4c4a-a21a-e1c87742cbf0
caps.latest.revision: 6
author: "Minewiskan"
ms.author: "owend"
manager: "kfile"
---
# Combiner.CombineTextByDelimiter

  
## About  
Returns a function that combines a list of text into a single text using the specified delimiter.  
  
```  
Combiner.CombineTextByDelimiter(delimiters as text, optional quoteStyle as nullable number) as function  
```  
  
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
  
