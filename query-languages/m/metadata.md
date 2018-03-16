---
title: "Metadata | Microsoft Docs"
ms.custom: ""
ms.date: "03/07/2018"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: 52c2eae3-e274-43d6-b78e-c94ac7e4e5e9
caps.latest.revision: 6
author: "Minewiskan"
ms.author: "owend"
manager: "kfile"
---
# Metadata
**Metadata** is information about a value that is associated with a value. **Metadata** is represented as a record value, called a metadata record. The fields of a **metadata record** can be used to store the metadata for a value. Every value has a metadata record. If the value of the metadata record has not been specified, then the metadata record is empty (has no fields). Associating a metadata record with a value does not change the value’s behavior in evaluations except for those that explicitly inspect metadata records.  
  
A metadata record value is associated with a value x using the syntax value meta [record]. For example, the following associates a metadata record with Rating and Tags fields with the text value "Mozart":  
  
```  
"Mozart" meta [ Rating = 5,   
Tags = {"Classical"} ]  
```  
A metadata record can be accessed for a value using the `Value.Metadata` function. In the following example, the expression in the ComposerRating field accesses the metadata record of the value in the Composer field, and then accesses the Rating field of the metadata record.  
  
```  
[  
    Composer = "Mozart" meta [ Rating = 5, Tags = {"Classical"} ],  
    ComposerRating = Value.Metadata(Composer)[Rating]   // 5  
]  
```  
Metadata records are not preserved when a value is used with an operator or function that constructs a new value. For example, if two text values are concatenated using the &amp; operator, the metadata of the resulting text value is an empty record [].  
  
The standard library functions `Value.RemoveMetadata` and `Value.ReplaceMetadata` can be used to remove all metadata from a value and to replace a value’s metadata.  
  
