---
title: "Record.Field | Microsoft Docs"
ms.custom: ""
ms.date: "01/19/2018"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: c9cddf5e-42b8-4096-ad29-46c43c405e98
caps.latest.revision: 7
author: "Minewiskan"
ms.author: "owend"
manager: "kfile"
---
# Record.Field

  
## About  
Returns the value of the given field.  This function can be used to dynamically create field lookup syntax for a given record. In that way it is a dynamic verison of the record[field] syntax.  
  
```  
Record.Field(record as record, field as text) as any  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|record|The record to check.|  
|field|The field to obain the value for.|  
  
## <a name="__goback"></a>Example  
  
```  
Record.Field([CustomerID = 1, Name = "Bob", Phone = "123-4567"], "CustomerID") equals 1  
```  
