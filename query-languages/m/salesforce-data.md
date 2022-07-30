---
description: "Learn more about: Salesforce.Data"
title: "Salesforce.Data"
ms.date: 02/03/2021
ms.service: powerquery
ms.topic: reference
author: dougklopfenstein
ms.author: dougklo

---
# Salesforce.Data

## Syntax

<pre>
Salesforce.Data(optional <b>loginUrl</b> as any, optional <b>options</b> as nullable record) as table
</pre>

## About

Returns the objects on the Salesforce account provided in the credentials. The account will be connected through the provided environment `loginUrl`. If no environment is provided then the account will connect to production (https://login.salesforce.com). An optional record parameter, `options`, may be provided to specify additional properties. The record can contain the following fields: 
* `CreateNavigationProperties` : A logical (true/false) that sets whether to generate navigation properties on the returned values (default is false).
* `ApiVersion` : The Salesforce API version to use for this query. When not specified, API version 29.0 is used.
* `Timeout` : A duration that controls how long to wait before abandoning the request to the server. The default value is source-specific.
