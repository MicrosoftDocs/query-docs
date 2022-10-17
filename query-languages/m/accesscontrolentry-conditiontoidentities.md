---
description: "Learn more about: AccessControlEntry.ConditionToIdentities"
title: "AccessControlEntry.ConditionToIdentities"
ms.date: 10/7/2022
---
# AccessControlEntry.ConditionToIdentities

## Syntax

<pre>
AccessControlEntry.ConditionToIdentities(<b>identityProvider</b> as function, <b>condition</b> as function) as list
</pre>

## About

Using the specified `identityProvider`, converts the `condition` into the list of identities for which `condition` would return `true` in all authorization contexts with `identityProvider` as the identity provider. An error is raised if it is not possible to convert `condition` into a list of identities, for example if `condition` consults attributes other than user or group identities to make a decision.

Note that the list of identities represents the identities as they appear in `condition` and no normalization (such as group expansion) is performed on them.
