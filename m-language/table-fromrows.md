---
title: "Table.FromRows | Microsoft Docs"
ms.custom: ""
ms.date: "12/28/2017"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: df1c29db-7e3c-4a25-a071-e344c07fb725
caps.latest.revision: 9
author: "Minewiskan"
ms.author: "owend"
manager: "erikre"
---
# Table.FromRows
## About  
Creates a table from the list <code>rows</code> where each element of the list is an inner list that contains the column values for a single row. An optional list of column names, a table type, or a number of columns could be provided for <code>columns</code>.
  
  
```  
Table.FromRows(rows as list, optional columns as any) as table  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|rows|The List to convert.|  
|optional columns|An optional list of column names, or a table type.|  
  
## <a name="__goback"></a>Example  
  
```  
Table.FromRows({{1, "Bob", "123-4567"} , {2, "Jim", "987-6543"}}, {"CustomerID ", "Name", "Phone"})  
```  
  
|CustomerID|Name|Phone|  
|--------------|--------|---------|  
|1|Bob|123-4567|  
|2|Jim|987-6543|  
  
