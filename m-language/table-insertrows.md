---
title: "Table.InsertRows | Microsoft Docs"
ms.custom: ""
ms.date: "01/19/2018"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: eb5d977c-9a6f-46a5-9e64-9b4563f28ec6
caps.latest.revision: 8
author: "Minewiskan"
ms.author: "owend"
manager: "kfile"
---
# Table.InsertRows

  
## About  
Returns a table with the list of rows inserted into the table at an index. Each row to insert must match the row type of the table..  
  
```  
Table.InsertRows(table as table, offset as number, rows as list) as table  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|table|The Table to insert rows into.|  
|offset|The row number to insert at.|  
|rows|The List of rows to insert.|  
  
## Remark  
  
-   Table.InsertRows is similar to List.InsertRange but requires a table as input.  
  
## Example  
  
```  
Table.InsertRows(Table.FromRecords({  
  
    [CustomerID = 1, Name = "Bob", Phone = "123-4567"],  
  
    [CustomerID = 2, Name = "Jim", Phone = "987-6543"] }),  
  
    2,  
  
    { [CustomerID = 3, Name = "Paul", Phone = "543-7890"] })  
  
Table.InsertRows(Table.FromRecords({  
  
    [CustomerID = 1, Name = "Bob", Phone = "123-4567"],  
  
    [CustomerID = 2, Name = "Jim", Phone = "987-6543"] }),  
  
    2,  
  
    { [CustomerID = 3, Name = "Paul", Phone = "543-7890"] })  
```  
  
|CustomerID|Name|Phone|  
|--------------|--------|---------|  
|1|Bob|123-4567|  
|2|Jim|987-6543|  
|3|Paul|543-7890|  
  
