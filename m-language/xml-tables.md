---
title: "Xml.Tables | Microsoft Docs"
ms.custom: ""
ms.date: "12/28/2017"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: 4cb0d34c-ee55-4a29-9a1d-91e8571b550c
caps.latest.revision: 7
author: "Minewiskan"
ms.author: "owend"
manager: "erikre"
---
# Xml.Tables
This topic applies to the Power Query Formula Language which can be used with [Power Query](https://support.office.com/article/Introduction-to-Microsoft-Power-Query-for-Excel-6E92E2F4-2079-4E1F-BAD5-89F6269CD605) and [Power BI Desktop](http://go.microsoft.com/fwlink/p/?LinkId=618607) to build queries that mashup data. See the list of [function categories](https://msdn.microsoft.com/en-us/library/mt211003.aspx).  
  
## About  
Returns the contents of an XML document as a nested collection of flattened tables.  
  
```  
Xml.Tables(contents as any, optional options as nullable record, optional encoding as nullable number) as table  
```  
  
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
  
```  
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
