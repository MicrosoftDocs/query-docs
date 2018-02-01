---
title: "Table.FirstN | Microsoft Docs"
ms.custom: ""
ms.date: "01/19/2018"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: c53dda77-7807-4da6-a8ef-07d9b86001c9
caps.latest.revision: 7
author: "Minewiskan"
ms.author: "owend"
manager: "kfile"
---
# Table.FirstN

  
## About  
Returns the first  row(s) of a table, depending on the countOrCondition parameter.  
  
```  
Table.FirstN( table as table, optional countOrCondition as any) as table  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|Table|The Table to check.|  
|optional countOrCondition|Depending on the type, more than one row will be returned.|  
  
## <a name="__toc360789476"></a>Remarks  
  
-   If countOrCondition is a number, many rows (starting at the top) will be returned.  
  
-   If countOrCondition is a condition, the rows that meet the condition will be returned until a row does not meet the condition.  
  
## Example  
  
```  
Table.FirstN(Table.FromRecords({  
  
    [CustomerID = 1, Name = "Bob", Phone = "123-4567"],  
  
    [CustomerID = 2, Name = "Jim", Phone = "987-6543"] ,  
  
    [CustomerID = 3, Name = "Paul", Phone = "543-7890"]  
  
}), 2)  
```  
  
|CustomerID|Name|Phone|  
|--------------|--------|---------|  
|1|Bob|123-4567|  
|2|Jim|987-6543|  
  
