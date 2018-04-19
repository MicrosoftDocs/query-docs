---
title: "Value.NullableEquals | Microsoft Docs"
ms.date: 4/16/2018
ms.prod: power-query
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# Value.NullableEquals

  
## About  
Returns a logical value or null based on two values .  
  
```  
Value.NullableEquals(value1 as any, value2 as any) as any  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|value1|The right value to compare.|  
|value2|The left value to compare.|  
  
## <a name="__toc360789738"></a>Remarks  
  
-   If either of the argument is null, it applies a nullable equality rules; otherwise, the same result as Value.Equals.  
  
## Example  
  
```  
Value.NullableEquals(1, null) equals null  
```  
