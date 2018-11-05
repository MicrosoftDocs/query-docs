---
title: "SapBusinessObjects.Universes | Microsoft Docs"
ms.date: 4/16/2018
ms.service: powerquery

ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# SapBusinessObjects.Universes

  
## About  
Connects to the SAP BusinessObjects BI Universe at the specified URL and returns the set of available universes.  
  
## Syntax

<pre> 
SapBusinessObjects.Universes(url as text) as table  
</pre>
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|url|The URL of the SAP BusinessObjects BI Universe to connect to.|  
  
## Remarks  
The function returns a top-level table of two rows. The row with Id = “Universes” contains a nested table of all of the universes available at the URL. The row with Id = “DisplayFolders” contains a nested tree of tables representing the display folder hierarchy of the available universes.  
  
The table of universes provides a stable path to access a particular universe by its ID.  
The nested tree of display folder tables provides a user-friendly way to organize and navigate to universes and is not guaranteed to remain stable.  
  
## Examples  
  
```powerquery-m 
SapBusinessObjects.Universes("http://sap.example.com:6405/biprws")  
```  
