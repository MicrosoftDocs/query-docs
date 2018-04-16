---
title: "Value.Metadata | Microsoft Docs"
ms.date: 4/16/2018
ms.service: powerbi
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# Value.Metadata

  
## About  
Returns a record containing the input’s metadata.  
  
```  
Value.Metadata(value as any) as record  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|value|The value to retrieve metadata for.|  
  
## Example  
  
```  
Value.Metadata(1 meta [meta = 1]) equals [ meta = 1]  
```  
