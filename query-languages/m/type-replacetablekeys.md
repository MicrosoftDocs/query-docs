---
title: "Type.ReplaceTableKeys | Microsoft Docs"
ms.date: 4/16/2018
ms.service: powerbi
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
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
