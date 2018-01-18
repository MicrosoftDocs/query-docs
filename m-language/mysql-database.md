---
title: "MySQL.Database | Microsoft Docs"
ms.custom: ""
ms.date: "12/28/2017"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: 38d25323-b119-4c39-aab9-53d994217161
caps.latest.revision: 10
author: "Minewiskan"
ms.author: "owend"
manager: "erikre"
---
# MySQL.Database
<code>MySQL.Database(**server** as text, **database** as text, optional **options** as nullable record) as table</code>

## About

Returns a table of SQL tables, views, and stored scalar functions available in a MySQL database on server <code>server</code> in the database instance named <code>database</code>. The port may be optionally specified with the server, separated by a colon. An optional record parameter, <code>options</code>, may be specified to control the following options: 

* <code>CreateNavigationProperties</code> : A logical (true/false) that sets whether to generate navigation properties on the returned values (default is true).
* <code>NavigationPropertyNameGenerator</code> : A function that is used for the creation of names for navigation properties.
* <code>Query</code> : A native SQL query used to retrieve data. If the query produces multiple result sets, only the first will be returned.
* <code>CommandTimeout</code> : A duration which controls how long the server-side query is allowed to run before it is canceled. The default value is ten minutes.
* <code>ConnectionTimeout</code> : A duration which controls how long to wait before abandoning an attempt to make a connection to the server. The default value is driver-dependent.
* <code>TreatTinyAsBoolean</code> : A logical (true/false) that determines whether to force tinyint columns on the server as logical values. The default value is true.
* <code>OldGuids</code> : A logical (true/false) that sets whether char(36) columns (if false) or binary(16) columns (if true) will be treated as GUIDs. The default value is false. 
* <code>ReturnSingleDatabase</code> : A logical (true/false) that sets whether to return all tables of all databases (if false) or to return tables and views of the specified database (if true). The default value is false.
* <code>HierarchicalNavigation</code> : A logical (true/false) that sets whether to view the tables grouped by their schema names (default is false).

 The record parameter is specified as [option1 = value1, option2 = value2...] or [Query = "select ..."] for example. 
  
