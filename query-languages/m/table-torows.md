---
title: "Table.ToRows | Microsoft Docs"
ms.custom: ""
ms.date: "01/19/2018"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: f2ab5209-6a7f-4878-9c27-27c7406a77b8
caps.latest.revision: 7
author: "Minewiskan"
ms.author: "owend"
manager: "kfile"
---
# Table.ToRows

  
## About  
Returns a nested list of row values from an input table.  
  
```  
Table.ToRows(table as table) as list  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|table|The Table to check.|  
  
## Example  
  
```  
let  
  
    Source = Table.ToRows(Table.FromRecords({  
  
    [CustomerID =1, Name ="Bob", Phone = "123-4567"],  
  
    [CustomerID =2, Name ="Jim", Phone = "987-6543"],  
  
    [CustomerID =3, Name ="Paul", Phone = "543-7890"]  
  
}))  
  
in  
  
    Source  
  
equals  
  
{  
  
    {1, "Bob", "123-4567"},  
  
    {2, "Jim", "987-6543"},  
  
    {3,  "Paul", "543-7890"}  
  
}  
```  
