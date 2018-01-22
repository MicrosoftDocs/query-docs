---
title: "Number.RoundDown | Microsoft Docs"
ms.custom: ""
ms.date: "01/19/2018"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: cf4bd4c6-6f8d-4ee7-ac59-b945ccbe175f
caps.latest.revision: 6
author: "Minewiskan"
ms.author: "owend"
manager: "kfile"
---
# Number.RoundDown

  
## About  
Returns the largest integer less than or equal to a number value.  
  
```  
Number.RoundDown(value as nullable number) as nullable number  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|value|Value to round down.|  
  
## Examples  
  
```  
Number.RoundDown(-1.2) equals -2  
```  
  
```  
Number.RoundDown(1.2) equals 1  
```  
