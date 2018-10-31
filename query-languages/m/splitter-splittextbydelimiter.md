---
title: "Splitter.SplitTextByDelimiter | Microsoft Docs"
ms.date: 4/16/2018
ms.prod: power-query
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# Splitter.SplitTextByDelimiter

  
## About  
Returns a function that will split text according to a delimiter.  
  
## Syntax

<pre>
Splitter.SplitTextByDelimiter(delimiter as text, optional quoteStyle as nullable number) as function  
</pre>
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|delimiter|The delimiter character is used to identify at what points to split the string.  The delimiter character is not included in the split values.  A trailing delimiter character will yield an additional empty text value.  The split values contain all characters between the delimiters.  This function will always produce at least one value.|  
|optional quoteStyle|The quoteStyle acts as described in Lines.FromText.  By default, it is QuoteStyle.Csv.|  
  
**Quote styles**  
  
-   QuoteStyle.None = 0;  
  
-   QuoteStyle.Csv  = 1;  
  
