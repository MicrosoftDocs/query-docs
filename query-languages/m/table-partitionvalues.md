---
title: "Table.PartitionValues | Microsoft Docs"
ms.date: 4/16/2018
ms.prod: power-query
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# Table.PartitionValues

  
## About  
Returns information about how a table is partitioned.  
  
```  
Table.PartitionValues(table as table) as table;  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|table|The input table.|  
  
## Remarks  
A table is returned where each column is a partition column in the original table, and each row corresponds to a partition in the original table.  
  
