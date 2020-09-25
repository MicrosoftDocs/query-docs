---
title: "Table.CombineColumnsToRecord | Microsoft Docs"
ms.date: 09/14/2020
ms.service: powerquery

ms.reviewer: gepopell
ms.topic: reference
author: dougklopfenstein
ms.author: v-douklo

---
# Table.CombineColumnsToRecord

## Syntax

<pre>
Table.CombineColumnsToRecord(<b>table</b> as table, <b>newColumnName</b> as text, <b>sourceColumns</b> as list, optional <b>options</b> as nullable record) as table
</pre>
  
## About  
Combines the specified columns of `table` into a new record-valued column named `newColumnName` where each record has field names and values corresponding to the column names and values of the columns that were combined. If a record is specified for `options`, the following options may be provided:

* `DisplayNameColumn`: When specified as text, indicates that the given column name should be treated as the display name of the record. This need not be one of the columns in the record itself.
* `TypeName`: When specified as text, supplies a logical type name for the resulting record which can be used during data load to drive behavior by the loading environment.
