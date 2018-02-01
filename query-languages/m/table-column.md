---
title: "Table.Column | Microsoft Docs"
ms.custom: ""
ms.date: "01/19/2018"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: f31d7bcd-a3b0-4336-8c85-513eb24bee8d
caps.latest.revision: 7
author: "Minewiskan"
ms.author: "owend"
manager: "kfile"
---
# Table.Column

  
## About  
Returns the values from a column in a table.  
  
```  
Table.Column(table as table, column as text) as list  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|table|The Table to check.|  
|column|The column to check.|  
  
## <a name="__toc360789550"></a>Remarks  
  
-   **Table.Column** is similar to **Record.Field** but requires a table as input.  
  
## <a name="__goback"></a>Example  
  
```  
Table.Column(Table.FromRecords(  
  
{  
  
      [CustomerID = 1, Name = "Bob", Phone = "123-4567"],  
  
      [CustomerID = 2, Name = "Jim", Phone = "987-6543"] ,  
  
      [CustomerID = 3, Name = "Paul", Phone = "543-7890"] ,  
  
      [CustomerID = 4, Name = "Ringo", Phone = "232-1550"]  
  
}  
  
), "Name")  
  
equals {"Bob", "Jim", "Paul", "Ringo"}  
```  
