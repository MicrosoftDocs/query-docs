---
description: "Learn more about: Pdf.Tables"
title: "Pdf.Tables"
ms.subservice: m-source
ms.topic: reference
---
# Pdf.Tables

## Syntax

<pre>
Pdf.Tables(<b>pdf</b> as binary, optional <b>options</b> as nullable record) as table
</pre>
  
## About

Returns any tables found in `pdf`. An optional record parameter, `options`, may be provided to specify additional properties. The record can contain the following fields:

* `Implementation`: The version of the algorithm to use when identifying tables. Old versions are available only for backwards compatibility, to prevent old queries from being broken by algorithm updates. The newest version should always give the best results. Valid values are "1.3", "1.2", "1.1", or null.
* `StartPage`: Specifies the first page in the range of pages to examine. Default: 1.
* `EndPage`: Specifies the last page in the range of pages to examine. Default: the last page of the document.
* `MultiPageTables`: Controls whether similar tables on consecutive pages will be automatically combined into a single table. Default: true.
* `EnforceBorderLines`: Controls whether border lines are always enforced as cell boundaries (when true), or simply used as one hint among many for determining cell boundaries (when false). Default: false.

## Example 1

Returns the tables contained in sample.pdf.

**Usage**

```powerquery-m
Pdf.Tables(File.Contents("c:\sample.pdf"))
```

**Output**

```powerquery-m
#table({"Name", "Kind", "Data"}, ...)
```
