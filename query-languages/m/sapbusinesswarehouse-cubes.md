---
title: "SapBusinessWarehouse.Cubes | Microsoft Docs"
ms.date: 4/16/2018
ms.prod: power-query
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# SapBusinessWarehouse.Cubes
`SapBusinessWarehouse.Cubes(**server** as text, **systemNumberOrSystemId** as text, **sclientId**s as text, optional **soptionsOrLogonGroup**s as any, optional **soptions**s as nullable record) as table`

## About
Returns a table of InfoCubes and queries grouped by InfoArea from an SAP Business Warehouse instance at server `server` with system number `systemNumberOrSystemId` and Client ID `clientId`. An optional record parameter, `optionsOrLogonGroup`, may be specified to control options. 