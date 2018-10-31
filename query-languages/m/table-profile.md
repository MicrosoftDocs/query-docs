---
title: "Table.Profile | Microsoft Docs"
ms.date: 4/16/2018
ms.prod: power-query
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# Table.Profile

## Syntax

<pre>
Table.Profile(table as table) as table  
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
  
