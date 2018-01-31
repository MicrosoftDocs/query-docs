---
title: "Table.AlternateRows | Microsoft Docs"
ms.custom: ""
ms.date: "01/19/2018"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: 23005789-e676-4af8-b028-ac23aad65de8
caps.latest.revision: 7
author: "Minewiskan"
ms.author: "owend"
manager: "kfile"
---
# Table.AlternateRows

  
## About  
Returns a table containing an alternating pattern of the rows from a table.  
  
```  
Table.AlternateRows( table as table, offset as number, skip as number, take as number) as table  
```  
  
## <a name="__toc360789469"></a>Remarks  
  
-   Table.AlternateRows is similar to List.Alternate but requires a table as input.  
  
## Example  
  
```  
Table.AlternateRows(Table.FromRecords({  
  
    [CustomerID = 1, Name = "Bob", Phone = "123-4567"],  
  
    [CustomerID = 2, Name = "Jim", Phone = "987-6543"] ,  
  
    [CustomerID = 3, Name = "Paul", Phone = "543-7890"]}), 1, 1, 1)  
```  
  
|CustomerID|Name|Phone|  
|--------------|--------|---------|  
|1|Bob|123-4567|  
|3|Paul|543-7890|  
  
