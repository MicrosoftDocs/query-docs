---
title: "Number.Sign | Microsoft Docs"
ms.custom: ""
ms.date: "01/19/2018"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: 767dde17-d163-4ed8-a2cf-a6bee831cc33
caps.latest.revision: 6
author: "Minewiskan"
ms.author: "owend"
manager: "kfile"
---
# Number.Sign

  
## About  
Returns 1 for positive numbers, -1 for negative numbers or 0 for zero.  
  
```  
Number.Sign(number as nullable number) as nullable number  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|number|Number to evaluate.|  
  
## Examples  
  
```  
Number.Sign(-1) equals -1  
```  
  
```  
Number.Sign(1) equals 1  
```  
