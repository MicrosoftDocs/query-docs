---
title: "Table.Skip | Microsoft Docs"
ms.custom: ""
ms.date: "01/19/2018"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: bb68a30f-5cba-413a-947a-ab35b83775e6
caps.latest.revision: 7
author: "Minewiskan"
ms.author: "owend"
manager: "kfile"
---
# Table.Skip

  
## About  
Returns a table that does not contain the first row or rows of the table.  
  
```  
Table.Skip(table as table, optional countOrCondition as any) as table  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|table|The Table to modify.|  
|optional countOrCondition|The number of rows to skip.|  
  
## <a name="__toc360789542"></a>Remarks  
  
-   **Table.Skip** is similar to **List.Skip** but requires a table as input.  
  
-   If countOrCondition is a number, that many rows (starting at the top) will be skipped.  
  
-   If countOrCondition is a condition, the rows that meet the condition will be skipped until a row does not meet the condition.  
  
## Examples  
  
```  
Table.Skip(Table.FromRecords(  
  
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
  
