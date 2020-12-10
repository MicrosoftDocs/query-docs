---
title: "Pdf.Tables | Microsoft Docs"
ms.date: 06/15/2020
ms.service: powerquery
ms.reviewer: gepopell
ms.topic: reference
author: dougklopfenstein
ms.author: bezhan

---
# Pdf.Tables

## Syntax

<pre>
Pdf.Tables(<b>pdf</b> as binary, optional <b>options</b> as nullable record) as table
</pre>
  
## About  

Returns any tables found in `pdf`. An optional record parameter, `options`, may be provided to specify additional properties. The record can contain the following fields:

* `Implementation`: The version of the algorithm to use when identifying tables. Valid values are "1.1" or null.
* `StartPage`: Specifies the first page in the range of pages to examine. Default: 1.
* `EndPage`: Specifies the last page in the range of pages to examine. Default: the last page of the document.
* `MultiPageTables`: Controls whether similar tables on consecutive pages will be automatically combined into a single table. Default: true.
* `EnforceBorderLines`: Controls whether border lines are always enforced as cell boundaries (when true), or simply used as one hint among many for determining cell boundaries (when false). Default: false. 

## Example 1
Returns the tables contained in sample.pdf.

```
Pdf.Tables(File.Contents("c:\sample.pdf"))
```

```
#table({"Name", "Kind", "Data"}, ...)
```
