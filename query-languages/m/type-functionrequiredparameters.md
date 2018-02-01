---
title: "Type.FunctionRequiredParameters | Microsoft Docs"
ms.custom: ""
ms.date: "01/19/2018"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: c3269116-7b36-4b66-bad3-b827422a406c
caps.latest.revision: 5
author: "Minewiskan"
ms.author: "owend"
manager: "kfile"
---
# Type.FunctionRequiredParameters

  
## About  
Returns a number indicating the minimum number of parameters required to invoke the a type of function.  
  
```  
Type.FunctionRequiredParameters(#"type" as type) as number  
```  
  
## Examples  
  
```  
Type.FunctionRequiredParameters( type function () as any) equals 0  
```  
  
```  
Type.FunctionRequiredParameters( type function (x as number) as any) equals 1  
```  
