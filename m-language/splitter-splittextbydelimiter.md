---
title: "Splitter.SplitTextByDelimiter | Microsoft Docs"
ms.custom: ""
ms.date: "01/19/2018"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: 8efbc894-65db-475a-a4c5-e1a0fb42065b
caps.latest.revision: 6
author: "Minewiskan"
ms.author: "owend"
manager: "kfile"
---
# Splitter.SplitTextByDelimiter

  
## About  
Returns a function that will split text according to a delimiter.  
  
```  
Splitter.SplitTextByDelimiter(delimiter as text, optional quoteStyle as nullable number) as function  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|delimiter|The delimiter character is used to identify at what points to split the string.  The delimiter character is not included in the split values.  A trailing delimiter character will yield an additional empty text value.  The split values contain all characters between the delimiters.  This function will always produce at least one value.|  
|optional quoteStyle|The quoteStyle acts as described in Lines.FromText.  By default, it is QuoteStyle.Csv.|  
  
**Quote styles**  
  
-   QuoteStyle.None = 0;  
  
-   QuoteStyle.Csv  = 1;  
  
