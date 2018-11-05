---
title: "Xml.Tables | Microsoft Docs"
ms.date: 4/16/2018
ms.service: powerquery

ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# Xml.Tables

  
## About  
Returns the contents of an XML document as a nested collection of flattened tables.  
  
## Syntax

<pre>
Xml.Tables(contents as any, optional options as nullable record, optional encoding as nullable number) as table  
</pre>
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|Contents|The contents may be directly passed to the function as text, or it may be the binary value returned by a function like File.Contents or Web.Contents.|  
|optional options|Control the behavior of this function.|  
|encoding|Encoding value.|  
  
## <a name="__toc360789837"></a>options Settings  
  
|Setting|Description|  
|-----------|---------------|  
|NavigationTable|If true, output tables are navigation tables. Default value is true.|  
  
## <a name="__goback"></a>Example  
  
```powerquery-m
Xml.Tables("<books>  
  
    <book>  
  
        <name>Book1</name>  
  
    </book>  
  
    <book>  
  
        <name>Book2</name>  
  
    </book>  
  
</books>")  
  
equals  
  
(Table.FromRecords({ [  
  
    Name = "book",  
  
    Table = (Table.FromRecords({ [  
  
        name = "Book1"  
  
    ], [  
  
        name = "Book2"  
  
    ]  
  
)  
```  
