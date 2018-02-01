---
title: "Type.IsOpenRecord | Microsoft Docs"
ms.custom: ""
ms.date: "01/19/2018"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: 4fa1b072-5b30-41ef-addb-4799200b88f4
caps.latest.revision: 5
author: "Minewiskan"
ms.author: "owend"
manager: "kfile"
---
# Type.IsOpenRecord

  
## About  
Returns whether a record type is open.  
  
```  
Type.IsOpenRecord(#"type" as type) as logical  
```  
  
## Examples  
  
```  
Type.IsOpenRecord(type [ A = number,…]) equals true  
```  
  
```  
Type.IsOpenRecord(type [ A = number]) equals false  
```  
