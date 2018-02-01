---
title: "Comparer.Equals | Microsoft Docs"
ms.custom: ""
ms.date: "01/19/2018"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: df753936-e08c-4d79-9042-3fd474b36f6f
caps.latest.revision: 5
author: "Minewiskan"
ms.author: "owend"
manager: "kfile"
---
# Comparer.Equals

  
## About  
Returns a logical value based on the equality check over the two given values.  
  
```  
Comparer.Equals(comparer as function, x as any, y as any) as logical  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|comparer|The comparer function is used to perform the operation.|  
|x|The left value to compare.|  
|y|The right value to compare.|  
  
## Example  
  
```  
let  
comparer1 = Comparer.FromCulture("en-us", false),  
comparer2 = Comparer.FromCulture("en-us", true)      
in       
[         
Test1 =  Comparer.Equals(comparer1,"a","A"), equals false   
Test2 = Comparer.Equals(comparer2,"a","A") equals true       
]  
```  
