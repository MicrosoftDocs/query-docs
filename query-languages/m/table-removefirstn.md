---
title: "Table.RemoveFirstN | Microsoft Docs"
ms.custom: ""
ms.date: "01/19/2018"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: e3402391-cf13-44d8-82f4-bc68dfc26bbd
caps.latest.revision: 5
author: "Minewiskan"
ms.author: "owend"
manager: "kfile"
---
# Table.RemoveFirstN

  
## About  
Returns a table with the specified number of rows removed from the table starting at the first row. The number of rows removed depends on the optional countOrCondition parameter.  
  
```  
Table.RemoveFirstN( table as table, optional countOrCondition as any) as table  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|table|The Table to remove rows from.|  
|optional countOrCondition|Optional number of rows or condition to remove rows, default is 1|  
  
## <a name="__toc360789538"></a>Remarks  
  
-   If countOrCondidtion is omitted only the first row is removed  
  
-   If countOrCondidtion is a number, that many rows (starting from the top) will be removed)  
  
-   If countOrCondidtion is a condition, the rows that meet the condition will be removed until a rows does not meet the condition  
  
## Example  
  
```  
Table.RemoveFirstN(  
  
    Table.FromRecords(  
  
{  
  
    [CustomerID = 1, Name = "Bob", Phone = "123-4567"],  
  
      [CustomerID = 2, Name = "Jim", Phone = "987-6543"] ,  
  
      [CustomerID = 3, Name = "Paul", Phone = "543-7890"] ,  
  
      [CustomerID = 4, Name = "Ringo", Phone = "232-1550"]  
  
}  
  
), 2)  
```  
  
|CustomerID|Name|Phone|  
|--------------|--------|---------|  
|3|Paul|543-7890|  
|4|Ringo|232-1550|  
  
```  
Table.RemoveFirstN(  
  
    Table.FromRecords(  
  
{  
  
    [CustomerID = 1, Name = "Bob", Phone = "123-4567"],  
  
      [CustomerID = 2, Name = "Jim", Phone = "987-6543"] ,  
  
      [CustomerID = 3, Name = "Paul", Phone = "543-7890"] ,  
  
      [CustomerID = 4, Name = "Ringo", Phone = "232-1550"]  
  
}  
  
), each _ [CustomerID] <= 2)  
```  
  
|CustomerID|Name|Phone|  
|--------------|--------|---------|  
|3|Paul|543-7890|  
|4|Ringo|232-1550|  
  
