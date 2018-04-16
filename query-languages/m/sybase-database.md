---
title: "Sybase.Database | Microsoft Docs"
ms.date: 4/16/2018
ms.service: powerbi
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# Sybase.Database
<code>Sybase.Database(**server** as text, **database** as text, optional **options** as nullable record) as table</code>

## About

Returns a table of SQL tables and views available in a Sybase database on server <code>server</code> in the database instance named <code>database</code>. The port may be optionally specified with the server, separated by a colon. An optional record parameter, <code>options</code>, may be specified to control the following options: 

* <code>CreateNavigationProperties</code> : A logical (true/false) that sets whether to generate navigation properties on the returned values (default is true).
* <code>NavigationPropertyNameGenerator</code> : A function that is used for the creation of names for navigation properties.
* <code>Query</code> : A native SQL query used to retrieve data. If the query produces multiple result sets, only the first will be returned.
* <code>CommandTimeout</code> : A duration which controls how long the server-side query is allowed to run before it is canceled. The default value is ten minutes.
* <code>ConnectionTimeout</code> : A duration which controls how long to wait before abandoning an attempt to make a connection to the server. The default value is driver-dependent.
* <code>HierarchicalNavigation</code> : A logical (true/false) that sets whether to view the tables grouped by their schema names (default is false).

 The record parameter is specified as [option1 = value1, option2 = value2...] or [Query = "select ..."] for example.
  
