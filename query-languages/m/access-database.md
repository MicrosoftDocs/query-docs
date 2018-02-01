---
title: "Access.Database | Microsoft Docs"
ms.custom: ""
ms.date: "01/19/2018"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: 88702295-2e3c-47f3-993e-a37fee82d9bb
caps.latest.revision: 7
author: "Minewiskan"
ms.author: "owend"
manager: "kfile"
---
# Access.Database

  
```  
Access.Database(database as binary, optional options as nullable record) as table  
```  
  
## About  
Returns a structural representation of an Access database, <code>database</code>. An optional record parameter, <code>options</code>, may be specified to control the following options: <ul> <li> <code>CreateNavigationProperties</code> : A logical (true/false) that sets whether to generate navigation properties on the returned values (default is false).</li> <li> <code>NavigationPropertyNameGenerator</code> : A function that is used for the creation of names for navigation properties.</li> </ul> The record parameter is specified as [option1 = value1, option2 = value2...] for example.  
  
## Example  
  
```  
Access.Database(File.Contents("c:\users\myuser\Desktop\mydb.accdb"))  
```  
  
