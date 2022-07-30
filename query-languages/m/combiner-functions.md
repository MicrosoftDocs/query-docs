---
description: "Learn more about: Combiner functions"
title: "Combiner functions | Microsoft Docs"
ms.date: 5/16/2020
ms.service: powerquery

ms.topic: reference
author: dougklopfenstein
ms.author: dougklo

---
# Combiner functions

These functions are used by other library functions that merge values. For example, `Table.ToList` and `Table.CombineColumns` apply a combiner function to each row in a table to produce a single value for each row.

|Name|Description|
|------------|---------------|
|[Combiner.CombineTextByDelimiter](combiner-combinetextbydelimiter.md)|Returns a function that combines a list of text into a single text using the specified delimiter.|
|[Combiner.CombineTextByEachDelimiter](combiner-combinetextbyeachdelimiter.md)|Returns a function that combines a list of text into a single text using each specified delimiter in sequence.|
|[Combiner.CombineTextByLengths](combiner-combinetextbylengths.md)|Returns a function that combines a list of text into a single text using the specified lengths.|
|[Combiner.CombineTextByPositions](combiner-combinetextbypositions.md)|Returns a function that combines a list of text into a single text using the specified positions.|
|[Combiner.CombineTextByRanges](combiner-combinetextbyranges.md)|Returns a function that combines a list of text into a single text using the specified positions and lengths.|
