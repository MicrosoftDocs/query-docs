---
title: "Duration.ToRecord | Microsoft Docs"
ms.custom: ""
ms.date: "01/19/2018"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: 036c1a94-99c3-49c9-812c-c2c83dbca4be
caps.latest.revision: 5
author: "Minewiskan"
ms.author: "owend"
manager: "kfile"
---
# Duration.ToRecord

  
## About  
Returns a record with parts of a Duration value.  
  
```  
Duration.ToRecords(duration as duration) as record  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|duration|The Duration to parse.|  
  
## Example  
  
```  
Duration.ToRecord(#duration(2, 5, 55, 20)) equals [Days=2, Hours=5, Minutes=55, Seconds=20]  
```  
