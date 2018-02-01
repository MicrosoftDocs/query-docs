---
title: "Value.Metadata | Microsoft Docs"
ms.custom: ""
ms.date: "01/19/2018"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: d4278eee-b70a-4ae6-9d2a-abd3c7e22bf3
caps.latest.revision: 5
author: "Minewiskan"
ms.author: "owend"
manager: "kfile"
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
