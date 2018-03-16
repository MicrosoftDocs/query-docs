---
title: "Table.ExpandListColumn | Microsoft Docs"
ms.custom: ""
ms.date: "01/19/2018"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: b7807a22-b0f9-4bd9-af2c-ef4c44d10682
caps.latest.revision: 8
author: "Minewiskan"
ms.author: "owend"
manager: "kfile"
---
# Table.ExpandListColumn

  
## About  
Given a column of lists in a table, create a copy of a row for each value in its list.  
  
```  
Table.ExpandListColumn(table as table, column as text) as table  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|table|The Table to modify.|  
|column|The column to expand.|  
  
## Example  
  
```  
Table.ExpandListColumn(  
  
    Table.FromRecords(  
  
    {  
  
    [Name= {"Bob", "Jim", "Paul"}, Discount = .15]  
  
}), "Name")  
```  
  
|Name|Discount|  
|--------|------------|  
|Bob|0.15|  
|Jim|0.15|  
|Paul|0.15|  
  
