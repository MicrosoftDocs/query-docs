---
title: "Table.ToRecords | Microsoft Docs"
ms.custom: ""
ms.date: "01/19/2018"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: af5e62d2-28ac-438a-a080-273c6dd4d064
caps.latest.revision: 5
author: "Minewiskan"
ms.author: "owend"
manager: "kfile"
---
# Table.ToRecords

  
## About  
Returns a list of records from an input table.  
  
```  
Table.ToRecords(table as table) as list  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|table|The Table to convert.|  
  
## Example  
  
```  
Table.ToRecords(Table.FromRows({{"1", "2"}},{"a", "b"})) equals {[a = "1", b = "2"]}  
```  
