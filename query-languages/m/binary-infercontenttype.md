---
description: "Learn more about: Binary.InferContentType"
title: "Binary.InferContentType"
ms.subservice: m-source
---
# Binary.InferContentType

## Syntax

<pre>
Binary.InferContentType(<b>source</b> as binary) as record
</pre>

## About

Returns a record with field Content.Type that contains the inferred MIME-type. If the inferred content type is text/*, and an encoding code page is detected, then additionally returns field Content.Encoding that contains the encoding of the stream. If the inferred content type is text/csv, and the format is delimited, additionally returns field Csv.PotentialDelimiter containing a table for analysis of potential delimiters. If the inferred content type is text/csv, and the format is fixed-width, additionally returns field Csv.PotentialPositions containing a list for analysis of potential fixed width column positions.
