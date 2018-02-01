---
title: "Type.NonNullable | Microsoft Docs"
ms.custom: ""
ms.date: "01/19/2018"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: cf2938fe-417c-4ab6-9d85-6b2b600f8f01
caps.latest.revision: 5
author: "Minewiskan"
ms.author: "owend"
manager: "kfile"
---
# Type.NonNullable

  
## About  
Returns the non nullable type from a type.  
  
```  
Type.NonNullable(#"type" as type) as type  
```  
  
## Example  
  
```  
Type.NonNullable(type nullable number) equals type number  
```  
