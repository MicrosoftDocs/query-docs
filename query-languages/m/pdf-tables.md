---
title: "Pdf.Tables | Microsoft Docs"
ms.date: 02/12/2019
ms.service: powerquery
ms.reviewer: gepopell
ms.topic: reference
author: dougklopfenstein
ms.author: v-douklo

---
# Pdf.Tables

## Syntax

<pre>
Pdf.Tables(<b>pdf</b> as binary, optional <b>options</b> as nullable record) as table
</pre>
  
## About  

Returns any tables found in <code>pdf</code>. An optional record parameter, <code>options</code>, may be provided to specify additional properties. The record can contain the following fields: <ul> <li><code>StartPage</code> : Specifies the first page in the range of pages to examine. Default: 1.</li> <li><code>EndPage</code> : Specifies the last page in the range of pages to examine. Default: the last page of the document.</li> <li><code>MultiPageTables</code> : Controls whether similar tables on consecutive pages will be automatically combined into a single table. Default: true.</li> <li><code>EnforceBorderLines</code> : Controls whether border lines are always enforced as cell boundaries (when true), or simply used as one hint among many for determining cell boundaries (when false). Default: false.</li> </ul> 

## Example 1

Returns the tables contained in sample.pdf.

```powerquery-m
Pdf.Tables(File.Contents("c:\sample.pdf"))
```

`#table({"Name", "Kind", "Data"}, ...)`
