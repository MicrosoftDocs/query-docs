---
title: "Xml.Document | Microsoft Docs"
ms.date: 4/16/2018
ms.prod: power-query
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
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
