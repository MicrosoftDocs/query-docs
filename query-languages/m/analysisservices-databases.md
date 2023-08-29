---
description: "Learn more about: AnalysisServices.Databases"
title: "AnalysisServices.Databases"
---
# AnalysisServices.Databases

## Syntax

<pre>
AnalysisServices.Databases(<b>server</b> as text, optional <b>options</b> as nullable record) as table
</pre>

## About

Returns databases on an Analysis Services instance, `server`. An optional record parameter, `options`, may be provided to specify additional properties. The record can contain the following fields:

* `TypedMeasureColumns`: A logical value indicating if the types specified in the multidimensional or tabular model will be used for the types of the added measure columns. When set to false, the type "number" will be used for all measure columns. The default value for this option is false.
* `Culture`: A culture name specifying the culture for the data. This corresponds to the 'Locale Identifier' connection string property.
* `CommandTimeout`: A duration that controls how long the server-side query is allowed to run before it is canceled. The default value is driver-dependent.
* `ConnectionTimeout`: A duration that controls how long to wait before abandoning an attempt to make a connection to the server. The default value is driver-dependent.
* `SubQueries`: A number (0, 1 or 2) that sets the value of the "SubQueries" property in the connection string. This controls the behavior of calculated members on subselects or subcubes. (The default value is 2).
* `Implementation`
