---
title: "Splitter.SplitTextByWhitespace | Microsoft Docs"
ms.custom: ""
ms.date: "12/28/2017"
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
manager: "erikre"
---
# Splitter.SplitTextByWhitespace
This topic applies to the Power Query Formula Language which can be used with [Power Query](https://support.office.com/article/Introduction-to-Microsoft-Power-Query-for-Excel-6E92E2F4-2079-4E1F-BAD5-89F6269CD605) and [Power BI Desktop](http://go.microsoft.com/fwlink/p/?LinkId=618607) to build queries that mashup data. See the list of [function categories](https://msdn.microsoft.com/en-us/library/mt211003.aspx).  
  
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
  
