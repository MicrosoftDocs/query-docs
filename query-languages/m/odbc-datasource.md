---
description: "Learn more about: Odbc.DataSource"
title: "Odbc.DataSource"
ms.subservice: m-source
---
# Odbc.DataSource

## Syntax

<pre>
Odbc.DataSource(<b>connectionString</b> as any, optional <b>options</b> as nullable record) as table
</pre>

## About

Returns a table of SQL tables and views from the ODBC data source specified by the connection string `connectionString`. `connectionString` can be text or a record of property value pairs. Property values can either be text or number. An optional record parameter, `options`, may be provided to specify additional properties. The record can contain the following fields:

* `CreateNavigationProperties`: A logical (true/false) that sets whether to generate navigation properties on the returned values (default is true).
* `HierarchicalNavigation`: A logical (true/false) that sets whether to view the tables grouped by their schema names (default is false).
* `ConnectionTimeout`: A duration that controls how long to wait before abandoning an attempt to make a connection to the server. The default value is 15 seconds.
* `CommandTimeout`: A duration that controls how long the server-side query is allowed to run before it is canceled. The default value is ten minutes.
* `SqlCompatibleWindowsAuth`: A logical (true/false) that determines whether to produce SQL Server-compatible connection string options for Windows authentication. The default value is true.

## Example 1

Return the SQL tables and views from the provided connection string.

**Usage**

```powerquery-m
Odbc.DataSource("dsn=your_dsn")
```

**Output**

```powerquery-m
table
```
