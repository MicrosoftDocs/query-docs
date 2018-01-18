---
title: "PostgreSQL.Database | Microsoft Docs"
ms.custom: ""
ms.date: "12/28/2017"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: 380bf792-99ea-40d8-940e-9c7100906698
caps.latest.revision: 7
author: "Minewiskan"
ms.author: "owend"
manager: "erikre"
---
# PostgreSQL.Database
<code>PostgreSQL.Database(**server** as text, **database** as text, optional **options** as nullable record) as table</code>

## About

Returns a table of SQL tables and views available in a PostgreSQL database on server <code>server</code> in the database instance named <code>database</code>. The port may be optionally specified with the server, separated by a colon. An optional record parameter, <code>options</code>, may be specified to control the following options: 

* <code>CreateNavigationProperties</code> : A logical (true/false) that sets whether to generate navigation properties on the returned values (default is true).
* <code>NavigationPropertyNameGenerator</code> : A function that is used for the creation of names for navigation properties.
* <code>Query</code> : A native SQL query used to retrieve data. If the query produces multiple result sets, only the first will be returned.
* <code>CommandTimeout</code> : A duration which controls how long the server-side query is allowed to run before it is canceled. The default value is ten minutes.
* <code>ConnectionTimeout</code> : A duration which controls how long to wait before abandoning an attempt to make a connection to the server. The default value is driver-dependent.
* <code>HierarchicalNavigation</code> : A logical (true/false) that sets whether to view the tables grouped by their schema names (default is false).

 The record parameter is specified as [option1 = value1, option2 = value2...] or [Query = "select ..."] for example.
  
