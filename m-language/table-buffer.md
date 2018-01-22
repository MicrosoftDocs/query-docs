---
title: "Table.Buffer | Microsoft Docs"
ms.custom: ""
ms.date: "01/19/2018"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: 6ce1d7a9-e3fb-4cce-9af2-e219ae2ed53c
caps.latest.revision: 5
author: "Minewiskan"
ms.author: "owend"
manager: "kfile"
---
# Table.Buffer

  
## About  
Buffers a table into memory, isolating it from external changes during evaluation.  
  
```  
Table.Buffer(table as table) as table  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|table|The Table to buffer.|  
  
## <a name="__toc360789722"></a>Remarks  
  
-   Table.Buffer is similar to List.Buffer but requires a table as input.  
  
## Example  
  
```  
Table.Buffer(Sql.Database("localhost", "Northwind")[Customers]) equals Buffered copy of the Customers table  
```  
