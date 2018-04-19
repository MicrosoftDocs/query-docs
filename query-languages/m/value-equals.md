---
title: "Value.Equals | Microsoft Docs"
ms.date: 4/16/2018
ms.prod: power-query
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
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
