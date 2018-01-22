---
title: "Number.IsNaN | Microsoft Docs"
ms.custom: ""
ms.date: "01/19/2018"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: 212b9df8-7efe-48da-9132-4786ddec4dbb
caps.latest.revision: 5
author: "Minewiskan"
ms.author: "owend"
manager: "kfile"
---
# Number.IsNaN

  
## About  
Returns true if a value is Number.NaN.  
  
```  
Number.IsNaN(value as number) as logical  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|value|Value to evaluate.|  
  
## Examples  
  
```  
Number.IsNaN(1) equals false  
```  
  
```  
Number.IsNaN(0/0) equals true  
```  
