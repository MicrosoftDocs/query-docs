---
description: "Learn more about: Tables.GetRelationships"
title: "Tables.GetRelationships"
ms.subservice: m-source
---
# Tables.GetRelationships

## Syntax

<pre>
Tables.GetRelationships(<b>tables</b> as table, optional <b>dataColumn</b> as nullable text) as table
</pre>

## About

Gets the relationships among a set of tables. The set `tables` is assumed to have a structure similar to that of a navigation table. The column defined by `dataColumn` contains the actual data tables.
