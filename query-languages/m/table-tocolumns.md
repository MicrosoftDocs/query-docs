---
title: "Table.ToColumns | Microsoft Docs"
ms.custom: ""
ms.date: "01/19/2018"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: 24a0580b-f4f6-4012-8896-82d6ee529875
caps.latest.revision: 8
author: "Minewiskan"
ms.author: "owend"
manager: "kfile"
---
# Table.ToColumns

  
## About  
Returns a list of nested lists each representing a column of values in the input table.  
  
```  
Table.ToColumns(table as table) as list  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|table|The Table to convert.|  
  
## Example  
  
```  
let  
  
    Source = Table.ToColumns(Table.FromRecords(  
  
{  
  
    [CustomerID = 1, Name = "Bob", Phone = "123-4567"],  
  
      [CustomerID = 2, Name = "Jim", Phone = "987-6543"]  
  
}))  
  
in  
  
    Source  
  
equals  
  
{  
  
    {1, 2},  
  
    {"Bob",  "Jim"},  
  
    { "123-4567", "987-6543"}  
  
}  
```  
