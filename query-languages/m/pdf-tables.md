---
title: "Pdf.Tables | Microsoft Docs"
ms.date: 11/13/2018
ms.service: powerquery
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# Pdf.Tables

  
## About  
Returns any tables found in `pdf`. An optional record parameter, `options`, may be provided to specify additional properties. The record can contain the following fields: 

- `StartPage`

- `EndPage`
  
## Syntax

<pre>
Pdf.Tables(**pdf** as binary, optional **options** as nullable record) as table
</pre>
  
## Example 1

Returns the tables contained in sample.pdf.

```powerquery-m
Pdf.Tables(File.Contents("c:\sample.pdf"))
```

`#table({"Name", "Kind", "Data"}, ...)`
