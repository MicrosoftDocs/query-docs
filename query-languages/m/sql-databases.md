---
description: "Learn more about: Sql.Databases"
title: "Sql.Databases"
ms.date: 11/23/2020
ms.service: powerquery
ms.topic: reference
author: dougklopfenstein
ms.author: dougklo
---
# Sql.Databases

## Syntax

<pre>
Sql.Databases(<b>server</b> as text, optional <b>options</b> as nullable record) as table
</pre>

## About

Returns a table of databases on the specified SQL server, `server`. An optional record parameter, `options`, may be specified to control the following options:

* `CreateNavigationProperties`: A logical (true/false) that sets whether to generate navigation properties on the returned values (default is true).
* `NavigationPropertyNameGenerator`: A function that is used for the creation of names for navigation properties.
* `MaxDegreeOfParallelism`: A number that sets the value of the "maxdop" query clause in the generated SQL query.
* `CommandTimeout`: A duration that controls how long the server-side query is allowed to run before it is canceled. The default value is ten minutes.
* `ConnectionTimeout`: A duration that controls how long to wait before abandoning an attempt to make a connection to the server. The default value is driver-dependent.
* `HierarchicalNavigation`: A logical (true/false) that sets whether to view the tables grouped by their schema names (default is false).
* `MultiSubnetFailover`: A logical (true/false) that sets the value of the "MultiSubnetFailover" property in the connection string (default is false).
* `UnsafeTypeConversions`: A logical (true/false) that, if true, attempts to fold type conversions which could fail and cause the entire query to fail. Not recommended for general use.
* `ContextInfo`: A binary value that is used to set the CONTEXT_INFO before running each command.
* `OmitSRID`: A logical (true/false) that, if true, omits the SRID when producing Well-Known Text from geometry and geography types.

The record parameter is specified as [option1 = value1, option2 = value2...] for example.

Does not support setting a SQL query to run on the server. [`Sql.Database`](sql-database.md) should be used instead to run a SQL query. 
