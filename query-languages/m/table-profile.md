---
title: "Table.Profile | Microsoft Docs"
ms.date: 3/28/2019
ms.service: powerquery

ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# Table.Profile

## Syntax

<pre>
Table.Profile(<b>table</b> as table, optional <b>additionalAggregates</b> as nullable list) as table
</pre>
  
## About  
Returns a profile for the columns in table.  
  
The following information is returned for each column (when applicable):  
  
|Value|  
|---------|  
|minimum|  
|maximum|  
|average|  
|standard deviation|  
|count|  
|null count|  
|distinct count|  
  
