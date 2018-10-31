---
title: "Access.Database | Microsoft Docs"
ms.date: 4/16/2018
ms.prod: power-query
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# Access.Database

## Syntax

<pre>  
Access.Database(database as binary, optional options as nullable record) as table  
</pre> 
  
## About  
Returns a structural representation of an Access database, `database`. An optional record parameter, `options`, may be specified to control the following options: <ul> <li> `CreateNavigationProperties` : A logical (true/false) that sets whether to generate navigation properties on the returned values (default is false).</li> <li> `NavigationPropertyNameGenerator` : A function that is used for the creation of names for navigation properties.</li> </ul> The record parameter is specified as [option1 = value1, option2 = value2...] for example.  
  
## Example  
  
```powerquery-m  
Access.Database(File.Contents("c:\users\myuser\Desktop\mydb.accdb"))  
```  
  
