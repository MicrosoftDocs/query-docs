---
title: "Value.RemoveMetadata | Microsoft Docs"
ms.custom: ""
ms.date: "01/19/2018"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: 519e98bf-6ad2-41ca-b2c9-b4a496de4e44
caps.latest.revision: 5
author: "Minewiskan"
ms.author: "owend"
manager: "kfile"
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
