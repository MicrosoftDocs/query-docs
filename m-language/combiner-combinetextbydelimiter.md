---
title: "Combiner.CombineTextByDelimiter | Microsoft Docs"
ms.custom: ""
ms.date: "12/28/2017"
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
manager: "erikre"
---
# Combiner.CombineTextByDelimiter
This topic applies to the Power Query Formula Language which can be used with [Power Query](https://support.office.com/article/Introduction-to-Microsoft-Power-Query-for-Excel-6E92E2F4-2079-4E1F-BAD5-89F6269CD605) and [Power BI Desktop](http://go.microsoft.com/fwlink/p/?LinkId=618607) to build queries that mashup data. See the list of [function categories](https://msdn.microsoft.com/en-us/library/mt211003.aspx).  
  
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
  
