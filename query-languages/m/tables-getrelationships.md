---
title: "Tables.GetRelationships | Microsoft Docs"
ms.date: 4/16/2018
ms.prod: power-query
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# Tables.GetRelationships

## Syntax

<pre>
Tables.GetRelationships(tables as table, optional dataColumn as nullable text) as table
</pre>  
  
## About  
Gets the relationships among a set of tables. The tables are assumed to have a structure similar to that of a navigation table. The column defined by dataColumn contains the actual data tables.  
  
