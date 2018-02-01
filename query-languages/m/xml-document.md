---
title: "Xml.Document | Microsoft Docs"
ms.custom: ""
ms.date: "01/19/2018"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: 19f6b8e8-d7ff-4018-89ca-7ba2b49457ba
caps.latest.revision: 7
author: "Minewiskan"
ms.author: "owend"
manager: "kfile"
---
# Xml.Document

  
## About  
Returns the contents of an XML document as a hierarchical table (list of records).  
  
```  
Xml.Document(contents as any, optional options as nullable record, optional encoding as nullable number) as table  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|contents|The contents may be directly passed to the function as text, or it may be the binary value returned by a function like File.Contents or Web.Contents.|  
|options|Xml document options.|  
|encoding|Encoding value.|  
  
## <a name="__toc360789833"></a>Remarks  
  
-   The output of the function has a tabular shape.  Each row in the table corresponds to a node at the current level of depth.  Descending into the XML tree is done through accessing the “Value” property of a given row.  
  
The precise shape of the output table is as follows:  
  
```  
Value.Type(Xml.Document("<a></a>")) =  
  
type {[  
  
    Name = text,  
  
    Namespace = text,  
  
    Value = any,  
  
    Attributes = {[  
  
        Name = text,  
  
        Namespace = text,  
  
        Value = text  
  
    ]}  
  
]}  
```  
  
## Example  
  
```  
Xml.Document("<a></a>")  
  
    equals  { [  
  
    Name = "a",  
  
    Namespace = "",  
  
    Value = {},  
  
    Attributes = {}  
  
] }  
```  
