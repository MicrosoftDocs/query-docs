---
title: "Table.SelectRowsWithErrors | Microsoft Docs"
ms.date: 4/16/2018
ms.prod: power-query
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# Table.SelectRowsWithErrors

  
## About  
Returns a table with only the rows from table that contain an error in at least one of the cells in a row.  
  
```  
Table.SelectRowsWithErrors(table as table, optional columns as nullable list) as table  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|table|The Table to check.|  
|optional columns|Only cells in the column list are inspected for errors.|  
  
## <a name="__toc360789534"></a>Remarks  
  
-   Only errors detected by directly accessing the cell are considered. Errors nested more deeply, such as a structured value in a cell, are ignored.  
  
## Example  
  
```  
Table.SelectRowsWithErrors(Table.FromRecords(  
  
{  
  
      [CustomerID =..., Name = "Bob", Phone = "123-4567"],  
  
      [CustomerID = 2, Name = "Jim", Phone = "987-6543"] ,  
  
      [CustomerID = 3, Name = "Paul", Phone = "543-7890"] ,  
  
      [CustomerID = 4, Name = "Ringo", Phone = "232-1550"]  
  
}  
  
))  
```  
  
|CustomerID|Name|Phone|  
|--------------|--------|---------|  
|Error|Bob|123-4567|  
  
