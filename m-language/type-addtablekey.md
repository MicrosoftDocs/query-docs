---
title: "Type.AddTableKey | Microsoft Docs"
ms.custom: ""
ms.date: "01/19/2018"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: 55146283-291d-4ae3-9900-26efa31fc1c3
caps.latest.revision: 5
author: "Minewiskan"
ms.author: "owend"
manager: "kfile"
---
# Type.AddTableKey

  
## About  
Add a key to a table type.  
  
```  
Type.AddTableKey (table as type, columns as list,  isPrimary as logical) as type  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|table|The table type to modify.|  
|columns|Columns that define the key.|  
|isPrimary|Logical stating whether or not it is the primary key.|  
  
## Example  
  
```  
Type.AddTableKey(tableType, {"A", "B"}, false) equals  add a non-primary key that combines values from columns A and B  
```  
