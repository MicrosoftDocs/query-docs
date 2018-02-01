---
title: "Table.RowCount | Microsoft Docs"
ms.custom: ""
ms.date: "01/19/2018"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: 437ae9f2-7529-4ad9-8122-8170ea176e7c
caps.latest.revision: 7
author: "Minewiskan"
ms.author: "owend"
manager: "kfile"
---
# Table.RowCount

  
## About  
Returns the number of rows in a table.  
  
```  
Table.RowCount(table as table) as number  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|table|The Table to check.|  
  
## Example  
  
```  
let  
  
    emptyTable = Table.FromRows({}),  
  
     tableValue = Table.FromRows({{1,"Bob", "123-4567"}, {2,"Jim", "987-6543"}}, {"ProductID", "ProductName", "UnitPrice"})  
  
in  
  
[  
  
     IsEmptyTest1    = Table.IsEmpty(emptyTable),  
  
    IsEmptyTest2 = Table.IsEmpty(tableValue),  
  
    RowCount = Table.RowCount(tableValue),  
  
    ColumnCount = Table.ColumnCount(tableValue)  
  
]  
  
equals  
```  
  
|||  
|-|-|  
|IsEmptyTest1|true|  
|IsEmptyTest2|false|  
|**RowCount**|2|  
|ColumnCount|3|  
  
