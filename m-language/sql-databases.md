---
title: "Sql.Databases | Microsoft Docs"
ms.custom: ""
ms.date: "12/28/2017"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: e8207142-e59e-451f-ae58-ae3f968d9999
caps.latest.revision: 9
author: "Minewiskan"
ms.author: "owend"
manager: "erikre"
---
# Sql.Databases
<code>Sql.Databases(**server** as text, optional **options** as nullable record) as table</code>

## About

Returns a table of databases on the specified SQL server, <code>server</code>. An optional record parameter, <code>options</code>, may be specified to control the following options: 

* <code>CreateNavigationProperties</code> : A logical (true/false) that sets whether to generate navigation properties on the returned values (default is true).
  
* <code>NavigationPropertyNameGenerator</code> : A function that is used for the creation of names for navigation properties.

* <code>MaxDegreeOfParallelism</code> : A number that sets the value of the &quot;maxdop&quot; query clause in the generated SQL query.
  
* <code>CommandTimeout</code> : A duration which controls how long the server-side query is allowed to run before it is canceled. The default value is ten minutes.
  
* <code>ConnectionTimeout</code> : A duration which controls how long to wait before abandoning an attempt to make a connection to the server. The default value is driver-dependent.
  
* <code>HierarchicalNavigation</code> : A logical (true/false) that sets whether to view the tables grouped by their schema names (default is false). 
  
* <code>MultiSubnetFailover</code> : A logical (true/false) that sets the value of the &quot;MultiSubnetFailover&quot; property in the connection string (default is false).
  
* <code>UnsafeTypeConversions</code>
  

The record parameter is specified as [option1 = value1, option2 = value2...] for example.
  
Does not support setting a SQL query to run on the server. <code>Sql.Database</code> should be used instead to run a SQL query. 