---
title: "Value.RemoveMetadata | Microsoft Docs"
ms.date: 4/16/2018
ms.service: powerbi
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# Value.RemoveMetadata

  
## About  
Removes the metadata on the value and returns the original value.  
  
```  
Value.RemoveMetadata(value as any) as any  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|value|The value to remove metadata from.|  
  
## Example  
  
```  
Value.RemoveMetadata(1 meta [meta = 1]) equals 1  
```  
