---
description: "Learn more about: Excel.Workbook"
title: "Excel.Workbook | Microsoft Docs"
ms.date: 11/23/2020
ms.service: powerquery

ms.reviewer: gepopell
ms.topic: reference
author: dougklopfenstein
ms.author: bezhan

---
# Excel.Workbook
  
## Syntax

<pre>
Excel.Workbook(<b>workbook</b> as binary, optional <b>useHeaders</b> as any, optional <b>delayTypes</b> as nullable logical) as table
</pre>

## About  
Returns the contents of the Excel workbook.  

* `useHeaders` can be null, a logical (true/false) value indicating whether the first row of each returned table should be treated as a header, or an options record. (See below for more details on the options record.) Default: false.
* `delayTypes` can be null or a logical (true/false) value indicating whether the columns of each returned table should be left untyped. Default: false.

If a record is specified for `useHeaders` (and `delayTypes` is null), the following record fields may be provided: 

* `UseHeaders`: Can be null or a logical (true/false) value indicating whether the first row of each returned table should be treated as a header. Default: false.
* `DelayTypes`: Can be null or a logical (true/false) value indicating whether the columns of each returned table should be left untyped. Default: false.
* `InferSheetDimensions`: Can be null or a logical (true/false) value indicating whether the area of a worksheet that contains data should be inferred by reading the worksheet itself, rather than by reading the dimensions metadata from the file. This can be useful in cases where the dimensions metadata is incorrect. Note that this option is only supported for Open XML Excel files, not for legacy Excel files. Default: false.
