---
description: "Learn more about: SapHana.Database"
title: "SapHana.Database"
ms.date: 11/14/2022
---
# SapHana.Database

## Syntax

<pre>
SapHana.Database(**server** as text, optional **options** as nullable record) as table
</pre>

## About

Returns a table of multidimensional packages from the SAP HANA database `server`. An optional record parameter, `options`, may be specified to control the following options:

* `Query`: A native SQL query used to retrieve data. If the query produces multiple result sets, only the first will be returned.
* `Distribution`: A [SapHanaDistribution](saphanadistribution-type.md) that sets the value of the "Distribution" property in the connection string. Statement routing is the method of evaluating the correct server node of a distributed system before statement execution. The default value is [SapHanaDistribution.All](/powerquery-m/saphanadistribution-type).
* `Implementation`: Specifies the implementation of the SAP HANA connector to use.
* `EnableColumnBinding`: Binds variables to the columns of a SAP HANA result set when fetching data. May potentially improve performance at the cost of slightly higher memory utilization. The default value is false.
* `ConnectionTimeout`: A duration that controls how long to wait before abandoning an attempt to make a connection to the server. The default value is 15 seconds.
* `CommandTimeout`: A duration that controls how long the server-side query is allowed to run before it is canceled. The default value is ten minutes.
