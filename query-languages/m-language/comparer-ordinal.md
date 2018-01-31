---
title: "Comparer.Ordinal | Microsoft Docs"
ms.custom: ""
ms.date: "01/19/2018"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: 89a9b474-5f98-4f82-bfe5-0ce55df055a2
caps.latest.revision: 5
author: "Minewiskan"
ms.author: "owend"
manager: "kfile"
---
# Comparer.Ordinal

  
## About  
Returns a comparer function which uses Ordinal rules to compare values.  
  
```  
Comparer.Ordinal(x as any, y as any) as number  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|x|The left value to compare.|  
|y|The right value to compare.|  
  
## Examples  
  
```  
Comparer.Equals(Comparer.Ordinal, "a","A")equals false  
```  
