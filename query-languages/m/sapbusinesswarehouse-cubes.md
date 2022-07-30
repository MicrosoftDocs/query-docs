---
description: "Learn more about: SapBusinessWarehouse.Cubes"
title: "SapBusinessWarehouse.Cubes"
ms.date: 7/29/2019
ms.service: powerquery
ms.topic: reference
author: dougklopfenstein
ms.author: dougklo

---
# SapBusinessWarehouse.Cubes

## Syntax

<pre>
SapBusinessWarehouse.Cubes(<b>server</b> as text, <b>systemNumberOrSystemId</b> as text, <b>clientId</b> as text, optional <b>optionsOrLogonGroup</b> as any, optional <b>options</b> as nullable record) as table
</pre>

## About
Returns a table of InfoCubes and queries grouped by InfoArea from an SAP Business Warehouse instance at server `server` with system number `systemNumberOrSystemId` and Client ID `clientId`. An optional record parameter, `optionsOrLogonGroup`, may be specified to control options. 
