---
title: "Table.PrefixColumns | Microsoft Docs"
ms.custom: ""
ms.date: "01/19/2018"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: 11c519ee-a710-45c9-9367-8b5ef7a7d613
caps.latest.revision: 7
author: "Minewiskan"
ms.author: "owend"
manager: "kfile"
---
# Table.PrefixColumns

  
## About  
Returns a table where the columns have all been prefixed with a text value.  
  
```  
Table.PrefixColumns(table as table, prefix as text) as table  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|table|The Table to modify.|  
|prefix|The prefix to add to every text value.|  
  
## Example  
  
```  
Table.PrefixColumns(Table.FromRecords(  
  
{  
  
    [CustomerID = 1, Name = "Bob", Phone = "123-4567"]  
  
}  
  
), "MyTable")  
```  
  
|MyTable.CustomerID|MyTable.Name|MyTable.Phone|  
|----------------------|----------------|-----------------|  
|1|Bob|123-4567|  
  
