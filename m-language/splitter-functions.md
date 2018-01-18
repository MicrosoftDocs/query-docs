---
title: "Splitter functions | Microsoft Docs"
ms.custom: ""
ms.date: "12/28/2017"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "index-page "
ms.assetid: 513fde5d-b826-4def-99d1-c4dfda9ecdb6
caps.latest.revision: 9
author: "Minewiskan"
ms.author: "owend"
manager: "erikre"
---
# Splitter functions
The Power Query Formula Language is a mashup language for transforming data. It's a functional, case sensitive language similar to F\#. Power Query Formula Language is used in a number of Microsoft products such as Power BI Desktop, Excel, and Analysis Services. To learn more about the language, see [PowerQueryName reference](https://msdn.microsoft.com/en-us/library/mt211003.aspx).  
  
## <a name="__toc360789908"></a>Splitter  
  
|Function|Description|  
|------------|---------------|  
|[Splitter.SplitByNothing](../PowerQuery/splitter-splitbynothing.md)|Returns a function that does no splitting, returning its argument as a single element list.| 
|[Splitter.SplitTextByAnyDelimiter](../PowerQuery/splitter-splittextbyanydelimiter.md)|Returns a function that splits text by any supported delimiter.|
|[Splitter.SplitTextByDelimiter](../PowerQuery/splitter-splittextbydelimiter.md)|Returns a function that will split text according to a delimiter.|  
|[Splitter.SplitTextByEachDelimiter](../PowerQuery/splitter-splittextbyeachdelimiter.md)|Returns a function that splits text by each delimiter in turn.|  
|[Splitter.SplitTextByLengths](../PowerQuery/splitter-splittextbylengths.md)|Returns a function that splits text according to the specified lengths.|  
|[Splitter.SplitTextByPositions](../PowerQuery/splitter-splittextbypositions.md)|Returns a function that splits text according to the specified positions.|  
|[Splitter.SplitTextByRanges](../PowerQuery/splitter-splittextbyranges.md)|Returns a function that splits text according to the specified ranges.|  
|[Splitter.SplitTextByRepeatedLengths](../PowerQuery/splitter-splittextbyrepeatedlengths.md)|Returns a function that splits text into a list of text after the specified length repeatedly.|
|[Splitter.SplitTextByWhitespace](../PowerQuery/splitter-splittextbywhitespace.md)|Returns a function that splits text according to whitespace.|  
  
Parameter values | Description
---------------- | -----------
[QuoteStyle.Csv](../PowerQuery/quotestyle-csv.md) | Quote characters indicate the start of a quoted string. Nested quotes are indicated by two quote characters.
[QuoteStyle.None](../PowerQuery/quotestyle-none.md) | Quote characters have no significance.
