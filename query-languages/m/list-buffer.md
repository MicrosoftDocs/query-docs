---
title: "List.Buffer | Microsoft Docs"
ms.custom: ""
ms.date: "01/19/2018"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: b4ad2505-6297-4e9d-a3f7-2c237e76908a
caps.latest.revision: 5
author: "Minewiskan"
ms.author: "owend"
manager: "kfile"
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
