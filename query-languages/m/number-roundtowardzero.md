---
title: "Number.RoundTowardZero | Microsoft Docs"
ms.custom: ""
ms.date: "01/19/2018"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: e91aec16-024e-4cdf-a962-7a70e1fdfd2a
caps.latest.revision: 6
author: "Minewiskan"
ms.author: "owend"
manager: "kfile"
---
# Number.RoundTowardZero

  
## About  
Returns Number.RoundDown(x) when x &gt;= 0 and Number.RoundUp(x) when x &lt; 0.  
  
```  
Number.RoundTowardZero(value as nullable number) as nullable number  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|value|Value to round toward zero.|  
  
## Examples  
  
```  
Number.RoundTowardZero(-1.2) equals -1  
```  
  
```  
Number.RoundTowardZero(1.2) equals 1  
```  
