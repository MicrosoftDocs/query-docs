---
title: "Type.FunctionParameters | Microsoft Docs"
ms.custom: ""
ms.date: "01/19/2018"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: e22e5ace-c04c-45d0-b3d7-11d516154291
caps.latest.revision: 5
author: "Minewiskan"
ms.author: "owend"
manager: "kfile"
---
# Type.FunctionParameters

  
## About  
Returns a record with field values set to the name of the parameters of a function type, and their values set to their corresponding types.  
  
```  
Type.FunctionParameters(functionType as type) as record  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|functionType|The function type to check.|  
  
## Examples  
  
```  
Type.FunctionParameters(type function () as any) equals []  
```  
  
```  
Type.FunctionParameters(type function (x as number, y as text) as any) equals [ x = number, y = text ]  
```  
