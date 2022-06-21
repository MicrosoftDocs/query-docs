---
description: "Learn more about: Oracle.Database"
title: "Oracle.Database | Microsoft Docs"
ms.date: 02/03/2021
ms.service: powerquery
ms.reviewer: ehvonleh
ms.topic: reference
author: dougklopfenstein
ms.author: dougklo

---
# Oracle.Database

## Syntax

<pre>
Oracle.Database(<b>server</b> as text, optional <b>options</b> as nullable record) as table
</pre>

## About

Returns a table of SQL tables and views from the Oracle database on server `server`. The port may be optionally specified with the server, separated by a colon. An optional record parameter, `options`, may be specified to control the following options:  

* `CreateNavigationProperties` : A logical (true/false) that sets whether to generate navigation properties on the returned values (default is true).
* `NavigationPropertyNameGenerator` : A function that is used for the creation of names for navigation properties.
* `Query` : A native SQL query used to retrieve data. If the query produces multiple result sets, only the first will be returned.
* `CommandTimeout` : A duration that controls how long the server-side query is allowed to run before it is canceled. The default value is ten minutes.
* `ConnectionTimeout` : A duration that controls how long to wait before abandoning an attempt to make a connection to the server. The default value is driver-dependent.
* `HierarchicalNavigation` : A logical (true/false) that sets whether to view the tables grouped by their schema names (default is false).

 The record parameter is specified as [option1 = value1, option2 = value2...] or [Query = "select ..."] for example. 
