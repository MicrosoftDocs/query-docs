---
title: "List.Buffer | Microsoft Docs"
ms.date: 4/16/2018
ms.service: powerbi
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# List.Buffer

  
## About  
Buffers the list in memory.  The result of this call is a stable list, which means it will have a determinimic count, and order of items.  
  
```  
List.Buffer(list as list) as list  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|list|The List to buffer.|  
  
## Example  
  
```  
List.Buffer(Sql:Database("localhost","northwind")[Customers]) equals stable copy of table Customers  
```  
