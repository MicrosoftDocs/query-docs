---
title: "Table.PartitionValues | Microsoft Docs"
ms.custom: ""
ms.date: "01/19/2018"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: 59e50083-9e54-4d13-afc7-5699220ab262
caps.latest.revision: 6
author: "Minewiskan"
ms.author: "owend"
manager: "kfile"
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
  
