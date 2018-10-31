---
title: "Sql.Databases | Microsoft Docs"
ms.date: 4/16/2018
ms.prod: power-query
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# Sql.Databases
`Sql.Databases(**server** as text, optional **options** as nullable record) as table`

## About

Returns a table of databases on the specified SQL server, `server`. An optional record parameter, `options`, may be specified to control the following options: 

* `CreateNavigationProperties` : A logical (true/false) that sets whether to generate navigation properties on the returned values (default is true).
  
* `NavigationPropertyNameGenerator` : A function that is used for the creation of names for navigation properties.

* `MaxDegreeOfParallelism` : A number that sets the value of the &quot;maxdop&quot; query clause in the generated SQL query.
  
* `CommandTimeout` : A duration which controls how long the server-side query is allowed to run before it is canceled. The default value is ten minutes.
  
* `ConnectionTimeout` : A duration which controls how long to wait before abandoning an attempt to make a connection to the server. The default value is driver-dependent.
  
* `HierarchicalNavigation` : A logical (true/false) that sets whether to view the tables grouped by their schema names (default is false). 
  
* `MultiSubnetFailover` : A logical (true/false) that sets the value of the &quot;MultiSubnetFailover&quot; property in the connection string (default is false).
  
* `UnsafeTypeConversions`
  

The record parameter is specified as [option1 = value1, option2 = value2...] for example.
  
Does not support setting a SQL query to run on the server. `Sql.Database` should be used instead to run a SQL query. 