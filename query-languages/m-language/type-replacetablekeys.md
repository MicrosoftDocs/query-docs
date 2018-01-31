---
title: "Type.ReplaceTableKeys | Microsoft Docs"
ms.custom: ""
ms.date: "01/19/2018"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: 3a35056f-d0bf-4e0d-a686-6808e9e3e73b
caps.latest.revision: 5
author: "Minewiskan"
ms.author: "owend"
manager: "kfile"
---
# Type.ReplaceTableKeys

  
## About  
Replaces the keys in a table type.  
  
```  
Type.ReplaceTableKeys(tableType as type,  keys as list) as type  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|tableType|The table type to modify.|  
|keys|The list of keys to replace.|  
  
## Example  
  
```  
Type.ReplaceTableKeys(tableType, {}) equals  returns type value with all keys removed  
```  
