---
title: "Table.CombineColumnsToRecord | Microsoft Docs"
ms.date: 06/16/2020
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
Combines the specified columns into a new record-valued column where each record has field names and values corresponding to the column names and values of the columns that were combined.
