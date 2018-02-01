---
title: "Table.FromValue | Microsoft Docs"
ms.custom: ""
ms.date: "01/19/2018"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: d1ba6885-13e6-4ab6-94ef-08d014d262c0
caps.latest.revision: 7
author: "Minewiskan"
ms.author: "owend"
manager: "kfile"
---
# Table.FromValue

  
## About  
Returns a table with a column containing the provided value or list of values.  
  
```  
Table.FromValue (value as any) as table  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|Value|The value to convert.|  
  
## Example  
  
```  
Table.FromValue({1, "Bob", "123-4567"}) equals  
```  
  
|Value|  
|---------|  
|1|  
|Bob|  
|132-4567|  
  
