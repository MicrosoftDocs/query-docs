---
description: "Learn more about: SapHana.Database"
title: "SapHana.Database"
ms.date: 9/1/2022
---
# SapHana.Database

## Syntax

<pre>
SapHana.Database(**server** as text, optional **options** as nullable record) as table
</pre>

## About

Returns a table of multidimensional packages from the SAP HANA database `server`. An optional record parameter, `options`, may be specified to control the following options:

* `Query`: A native SQL query used to retrieve data. If the query produces multiple result sets, only the first will be returned.
* `Distribution`: A [SapHanaDistribution](saphanadistribution-type.md) that sets the value of the &quot;Distribution&quot; property in the connection string. Statement routing is the method of evaluating the correct server node of a distributed system before statement execution. The default value is `SapHanaDistribution.All`.
* `Implementation`: Specifies the implementation of the SAP HANA connector to use.
* `EnableColumnBinding`: Binds variables to the columns of a SAP HANA result set when fetching data. May potentially improve performance at the cost of slightly higher memory utilization. The default value is false.
