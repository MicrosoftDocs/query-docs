---
title: "Splitter.SplitTextByWhitespace | Microsoft Docs"
ms.custom: ""
ms.date: "01/19/2018"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: 266f341c-9d74-4137-a0fa-61918ccdc14a
caps.latest.revision: 6
author: "Minewiskan"
ms.author: "owend"
manager: "kfile"
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
  
