---
title: "Date.ToRecord | Microsoft Docs"
ms.custom: ""
ms.date: "01/19/2018"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: a22cb485-4582-451a-b1a1-1f258a2c51c9
caps.latest.revision: 5
author: "Minewiskan"
ms.author: "owend"
manager: "kfile"
---
# Date.ToRecord

  
## About  
Returns a record containing parts of a Date value.  
  
```  
Date.ToRecord(date as date) as record  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|date|The Date to parse.|  
  
## Example  
  
```  
Date.ToRecord(#date(2013, 1, 1) equals [Year=2013,Month=1,Day=1]  
```  
