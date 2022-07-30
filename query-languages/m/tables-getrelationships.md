---
description: "Learn more about: Tables.GetRelationships"
title: "Tables.GetRelationships"
ms.date: 8/1/2019
ms.service: powerquery

ms.topic: reference
author: dougklopfenstein
ms.author: dougklo

---
# Tables.GetRelationships

## Syntax

<pre>
Tables.GetRelationships(<b>tables</b> as table, optional <b>dataColumn</b> as nullable text) as table
</pre>  
  
## About  
Gets the relationships among a set of tables. The set `tables` is assumed to have a structure similar to that of a navigation table. The column defined by `dataColumn` contains the actual data tables.
