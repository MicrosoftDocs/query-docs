---
title: "Salesforce.Data | Microsoft Docs"
ms.date: 4/16/2018
ms.service: powerbi
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# Salesforce.Data
<code>Salesforce.Data(optional **loginUrl** as any, optional **options** as nullable record) as table</code>

## About

Returns the objects on the Salesforce account provided in the credentials. The account will be connected through the provided environment <code>loginUrl</code>. If no environment is provided then the account will connect to production (https://login.salesforce.com). An optional record parameter, <code>options</code>, may be provided to specify additional properties. The record can contain the following fields: 
* <code>CreateNavigationProperties</code> : A logical (true/false) that sets whether to generate navigation properties on the returned values (default is false).
* <code>ApiVersion</code> : The Salesforce API version to use for this query. When not specified, API version 29.0 is used. 
