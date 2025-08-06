---
description: "Learn more about: MySQL.Database"
title: "MySQL.Database"
ms.subservice: m-source
---
# MySQL.Database

## Syntax

<pre>
MySQL.Database(
    <b>server</b> as text,
    <b>database</b> as text,
    optional <b>options</b> as nullable record
) as table
</pre>

## About

Returns a table of SQL tables, views, and stored scalar functions available in a MySQL database on server `server` in the database instance named `database`. The port may be optionally specified with the server, separated by a colon. An optional record parameter, `options`, may be specified to control the following options:

* `Encoding`: A TextEncoding value that specifies the character set used to encode all queries sent to the server (default is null).
* `CreateNavigationProperties`: A logical (true/false) that sets whether to generate navigation properties on the returned values (default is true).
* `NavigationPropertyNameGenerator`: A function that is used for the creation of names for navigation properties.
* `Query`: A native SQL query used to retrieve data. If the query produces multiple result sets, only the first will be returned.
* `CommandTimeout`: A duration that controls how long the server-side query is allowed to run before it is canceled. The default value is ten minutes.
* `ConnectionTimeout`: A duration that controls how long to wait before abandoning an attempt to make a connection to the server. The default value is driver-dependent.
* `TreatTinyAsBoolean`: A logical (true/false) that determines whether to force tinyint columns on the server as logical values. The default value is true.
* `OldGuids`: A logical (true/false) that sets whether char(36) columns (if false) or binary(16) columns (if true) will be treated as GUIDs. The default value is false.
* `ReturnSingleDatabase`: A logical (true/false) that sets whether to return all tables of all databases (if false) or to return tables and views of the specified database (if true). The default value is false.
* `HierarchicalNavigation`: A logical (true/false) that sets whether to view the tables grouped by their schema names (default is false).

The record parameter is specified as [option1 = value1, option2 = value2...] or [Query = "select ..."] for example.
