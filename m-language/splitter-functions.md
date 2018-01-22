---
title: "Splitter functions | Microsoft Docs"
ms.custom: ""
ms.date: "01/19/2018"
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
manager: "kfile"
---
# Splitter functions
[!INCLUDE[mIntroText](../includes/mintrotext-md.md)]  
  
## <a name="__toc360789908"></a>Splitter  
  
|Function|Description|  
|------------|---------------|  
|[Splitter.SplitByNothing](splitter-splitbynothing.md)|Returns a function that does no splitting, returning its argument as a single element list.| 
|[Splitter.SplitTextByAnyDelimiter](splitter-splittextbyanydelimiter.md)|Returns a function that splits text by any supported delimiter.|
|[Splitter.SplitTextByDelimiter](splitter-splittextbydelimiter.md)|Returns a function that will split text according to a delimiter.|  
|[Splitter.SplitTextByEachDelimiter](splitter-splittextbyeachdelimiter.md)|Returns a function that splits text by each delimiter in turn.|  
|[Splitter.SplitTextByLengths](splitter-splittextbylengths.md)|Returns a function that splits text according to the specified lengths.|  
|[Splitter.SplitTextByPositions](splitter-splittextbypositions.md)|Returns a function that splits text according to the specified positions.|  
|[Splitter.SplitTextByRanges](splitter-splittextbyranges.md)|Returns a function that splits text according to the specified ranges.|  
|[Splitter.SplitTextByRepeatedLengths](splitter-splittextbyrepeatedlengths.md)|Returns a function that splits text into a list of text after the specified length repeatedly.|
|[Splitter.SplitTextByWhitespace](splitter-splittextbywhitespace.md)|Returns a function that splits text according to whitespace.|  
  
Parameter values | Description
---------------- | -----------
[QuoteStyle.Csv](quotestyle-csv.md) | Quote characters indicate the start of a quoted string. Nested quotes are indicated by two quote characters.
[QuoteStyle.None](quotestyle-none.md) | Quote characters have no significance.
