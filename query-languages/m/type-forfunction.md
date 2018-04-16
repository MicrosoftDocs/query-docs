---
title: "Type.ForFunction | Microsoft Docs"
ms.date: 4/16/2018
ms.service: powerbi
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# Type.ForFunction

  
## About  
Creates a function type from the given Arguments.  
  
```  
Type.ForFunction(signature as record,  min as number) as type  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|signature|A Record value that contains fields for ReturnType and Parameters. Parameters is itself a record with all the parameter values assigned to their expected types.|  
|min|The minimum number of Arguments required to invoke the function.|  
  
## Example  
  
```  
Type.ForFunction([ReturnType = number, Parameters = [X = number]], 1)  
```  
