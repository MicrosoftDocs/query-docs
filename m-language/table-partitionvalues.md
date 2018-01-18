---
title: "Table.PartitionValues | Microsoft Docs"
ms.custom: ""
ms.date: "12/28/2017"
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
manager: "erikre"
---
# Table.PartitionValues
This topic applies to the Power Query Formula Language which can be used with [Power Query](https://support.office.com/article/Introduction-to-Microsoft-Power-Query-for-Excel-6E92E2F4-2079-4E1F-BAD5-89F6269CD605) and [Power BI Desktop](http://go.microsoft.com/fwlink/p/?LinkId=618607) to build queries that mashup data. See the list of [function categories](https://msdn.microsoft.com/en-us/library/mt211003.aspx).  
  
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
  
