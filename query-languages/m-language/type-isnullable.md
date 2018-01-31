---
title: "Type.IsNullable | Microsoft Docs"
ms.custom: ""
ms.date: "01/19/2018"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: f8880043-d671-40d1-843c-92feafcef715
caps.latest.revision: 5
author: "Minewiskan"
ms.author: "owend"
manager: "kfile"
---
# Type.IsNullable

  
## About  
Returns true if a type is a nullable type; otherwise, false.  
  
```  
Type.IsNullable(#"type" as type) as logical  
```  
  
## Examples  
  
```  
Type.IsNullable(type nullable number) equals true  
```  
  
```  
Type.IsNullable(number) equals false  
```  
