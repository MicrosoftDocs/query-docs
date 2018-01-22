---
title: "Record.FieldCount | Microsoft Docs"
ms.custom: ""
ms.date: "01/19/2018"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: 2e97792b-7900-49ab-ba4c-e58314e5e8d3
caps.latest.revision: 5
author: "Minewiskan"
ms.author: "owend"
manager: "kfile"
---
# Record.FieldCount

  
## About  
Returns the number of fields in a record.  
  
```  
Record.FieldCount(record as record) as number  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|record|The Record to check against.|  
  
## Example  
  
```  
Record.FieldCount([A=1, B=2]) equals 2  
```  
