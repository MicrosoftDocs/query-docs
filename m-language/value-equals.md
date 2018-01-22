---
title: "Value.Equals | Microsoft Docs"
ms.custom: ""
ms.date: "01/19/2018"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: deeffc0d-9ba9-4d78-832c-6b9b01a51fbb
caps.latest.revision: 5
author: "Minewiskan"
ms.author: "owend"
manager: "kfile"
---
# Value.Equals

  
## About  
Returns whether two values are equal.  
  
```  
Value.Equals(left as any, right as any, equater as record) as logical  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|left|The left value to compare.|  
|right|The right value to compare.|  
|equater|Optional equater record.|  
  
## Examples  
  
```  
Value.Equals(2,4)   
equals false  
```  
  
```  
Value.Equals(2,4,  
[     
Equals= (x,y) => Number.Mod(x,2)=Number.Mod(y,2),     
Hash = (x) => Value.Hash(x)  
])equals true  
```  
