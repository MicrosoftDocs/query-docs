---
title: "Table.Repeat | Microsoft Docs"
ms.custom: ""
ms.date: "01/19/2018"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: 68e86620-ea81-4800-bed1-acaa1dddc4e9
caps.latest.revision: 8
author: "Minewiskan"
ms.author: "owend"
manager: "kfile"
---
# Table.Repeat

  
## About  
Returns a table containing the rows of the table repeated the **count** number of times.  
  
```  
Table.Repeat(table as table, count as number) as table  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|table|The Table to check.|  
|count|The number of times to repeat the table.|  
  
## Example  
  
```  
Table.Repeat(Table.FromRecords({[Column1=1], [Column1=2]}), 2)  
```  
  
|Column1|  
|-----------|  
|1|  
|2|  
|1|  
|2|  
  
