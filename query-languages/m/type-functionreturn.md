---
title: "Type.FunctionReturn | Microsoft Docs"
ms.custom: ""
ms.date: "01/19/2018"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: 5d069d1e-0e8c-4b99-a348-78f4825bf550
caps.latest.revision: 5
author: "Minewiskan"
ms.author: "owend"
manager: "kfile"
---
# Type.FunctionReturn

  
## About  
Returns a type returned by a function type.  
  
```  
Type.FunctionReturn(type as type) as type  
```  
  
## Examples  
  
```  
Type.FunctionReturn(type function () as any) equals type any  
```  
  
```  
Type.FunctionReturn(type function () as [A = number]) equals type [A = number]  
```  
