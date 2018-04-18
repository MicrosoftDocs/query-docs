---
title: "Binary.InferContentType | Microsoft Docs"
ms.date: 4/17/2018
ms.service: powerbi
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# Binary.InferContentType
<code>Binary.InferContentType(<b>source</b> as binary) as record</code>
  
## About  
Returns a record with field Content.Type that contains the inferred MIME-type. If the inferred content type is text/*, and an encoding code page is detected, then additionally returns field Content.Encoding that contains the encoding of the stream. If the inferred content type is text/csv, and the format is delimited, additionally returns field Csv.PotentialDelimiter containing a table for analysis of potential delimiters. If the inferred content type is text/csv, and the format is fixed-width, additionally returns field Csv.PotentialPositions containing a list for analysis of potential fixed width column positions.
