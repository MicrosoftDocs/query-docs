---
title: "Number.RoundAwayFromZero | Microsoft Docs"
ms.custom: ""
ms.date: "01/19/2018"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: 25a06bf2-acdd-4a5b-acb5-b7e08223f30b
caps.latest.revision: 6
author: "Minewiskan"
ms.author: "owend"
manager: "kfile"
---
# Number.RoundAwayFromZero

  
## About  
Returns Number.RoundUp(value) when value &gt;= 0 and Number.RoundDown(value) when value &lt; 0.  
  
```  
Number.RoundAwayFromZero(value as nullable number) as nullable number  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|value|Value to round away from zero.|  
  
## Examples  
  
```  
Number.RoundAwayFromZero(-1.2) equals -2  
```  
  
```  
Number.RoundAwayFromZero(1.2) equals 2  
```  
