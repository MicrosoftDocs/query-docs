---
title: "Value.ReplaceMetadata | Microsoft Docs"
ms.custom: ""
ms.date: "01/19/2018"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: 94b027bd-d2c0-4e1b-9edc-e9523d630784
caps.latest.revision: 5
author: "Minewiskan"
ms.author: "owend"
manager: "kfile"
---
# Value.ReplaceMetadata

  
## About  
Replaces the metadata on a value with the new metadata record provided and returns the original value with the new metadata attached.  
  
```  
Value.ReplaceMetadata(value as any, newMeta as record) as any  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|value|The value to modify.|  
|newMeta|The new metadata to replace the old metadata with..|  
  
## Example  
  
```  
Value.ReplaceMetadata(1 meta [meta = 1], [meta=2]) equals  1 meta [meta = 2]  
```  
