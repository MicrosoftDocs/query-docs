---
title: "Splitter.SplitTextByDelimiter | Microsoft Docs"
ms.custom: ""
ms.date: "12/28/2017"
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
manager: "erikre"
---
# Splitter.SplitTextByDelimiter
This topic applies to the Power Query Formula Language which can be used with [Power Query](https://support.office.com/article/Introduction-to-Microsoft-Power-Query-for-Excel-6E92E2F4-2079-4E1F-BAD5-89F6269CD605) and [Power BI Desktop](http://go.microsoft.com/fwlink/p/?LinkId=618607) to build queries that mashup data. See the list of [function categories](https://msdn.microsoft.com/en-us/library/mt211003.aspx).  
  
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
  
