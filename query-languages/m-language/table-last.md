---
title: "Table.Last | Microsoft Docs"
ms.custom: ""
ms.date: "01/19/2018"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: 6c380b9d-0ec6-4d0d-8576-3c01889f3eb5
caps.latest.revision: 7
author: "Minewiskan"
ms.author: "owend"
manager: "kfile"
---
# Table.Last

  
## About  
Returns the last row of a table.  
  
```  
Table.Last(table as table, optional default as) as any  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|table|The Table to check.|  
|optional default|Optional default value.|  
  
## <a name="__toc360789492"></a>Remark  
  
-   If the table is empty, Table.Last returns null.  
  
## Example  
  
```  
Table.Last(Table.FromRecords({  
  
    [CustomerID = 1, Name = "Bob", Phone = "123-4567"],  
  
      [CustomerID = 2, Name = "Jim", Phone = "987-6543"] ,  
  
      [CustomerID = 3, Name = "Paul", Phone = "543-7890"]  
  
}))  
```  
  
|Name|Value|  
|--------|---------|  
|CustomerID|3|  
|Name|Paul|  
|Phone|543-7890|  
  
