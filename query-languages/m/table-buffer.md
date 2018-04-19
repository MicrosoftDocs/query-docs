---
title: "Table.Buffer | Microsoft Docs"
ms.date: 4/16/2018
ms.prod: power-query
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
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
