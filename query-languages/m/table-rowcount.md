---
title: "Table.RowCount | Microsoft Docs"
ms.date: 4/16/2018
ms.service: powerbi
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
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
  
