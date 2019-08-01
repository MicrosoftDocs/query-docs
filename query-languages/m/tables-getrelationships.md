---
title: "Tables.GetRelationships | Microsoft Docs"
ms.date: 8/1/2019
ms.service: powerquery

ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# Tables.GetRelationships

## Syntax

<pre>
Tables.GetRelationships(<b>tables</b> as table, optional <b>dataColumn</b> as nullable text) as table
</pre>  
  
## About  
Gets the relationships among a set of tables. The set `tables` is assumed to have a structure similar to that of a navigation table. The column defined by `dataColumn` contains the actual data tables.
