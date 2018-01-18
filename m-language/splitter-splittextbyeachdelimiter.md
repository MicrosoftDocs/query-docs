---
title: "Splitter.SplitTextByEachDelimiter | Microsoft Docs"
ms.custom: ""
ms.date: "12/28/2017"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: 103866a1-6a7a-4fe7-9a04-e97b301cffad
caps.latest.revision: 5
author: "Minewiskan"
ms.author: "owend"
manager: "erikre"
---
# Splitter.SplitTextByEachDelimiter
This topic applies to the Power Query Formula Language which can be used with [Power Query](https://support.office.com/article/Introduction-to-Microsoft-Power-Query-for-Excel-6E92E2F4-2079-4E1F-BAD5-89F6269CD605) and [Power BI Desktop](http://go.microsoft.com/fwlink/p/?LinkId=618607) to build queries that mashup data. See the list of [function categories](https://msdn.microsoft.com/en-us/library/mt211003.aspx).  
  
## About  
Returns a function that splits text by each delimiter in turn.  
  
```  
Splitter.SplitTextByEachDelimiter(delimiters as list, optional quoteStyle as nullable number) as function  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|Delimiters|The delimiter characters are used to identify at what points to split the string.  The delimiter character is not included in the split values.  A trailing delimiter character will yield an additional empty text value.  The split values contain all characters between the delimiters.  This function will always produce at least one value.|  
|optional quoteStyle|The quoteStyle acts as described in Lines.FromText.  By default, it is QuoteStyle.Csv.|  
  
## <a name="__toc360789916"></a>Remarks  
  
-   Splitter.SplitTextByEachDelimiter is similar to Splitter.SplitTextByDelimiter except that each delimiter is used once in order to determine the points at which to break the text.  
  
