---
description: "Learn more about: SharePoint.Tables"
title: "SharePoint.Tables"
---
# SharePoint.Tables

## Syntax

<pre>
SharePoint.Tables(<b>url</b> as text, optional <b>options</b> as nullable record) as table
</pre>

## About

Returns a table containing a row for each List item found at the specified SharePoint list, `url`. Each row contains properties of the List. `options` may be specified to control the following options:

* `ApiVersion`: A number (14 or 15) or the text "Auto" that specifies the SharePoint API version to use for this site. When not specified, API version 14 is used. When Auto is specified, the server version will be automatically discovered if possible, otherwise version defaults to 14. Non-English SharePoint sites require at least version 15.
* `Implementation`: Optional. Specifies which version of the SharePoint connector to use. Accepted values are "2.0" or null. If the value is "2.0", the 2.0 implementation of the SharePoint connector is used. If the value is null, the original implementation of the SharePoint connector is used.
* `ViewMode`: Optional. This option is only valid for implementation 2.0. Accepted values are "All" and "Default". If no value is specified, the value is set to "All". When "All"; is specified, the view includes all user-created and system-defined columns. When "Default" is specified, the view will match what the user sees when looking at the list online in whichever view that user set as Default in their settings. If the user edits their default view to add or remove either user-created or system-defined columns, or by creating a new view and setting it as default, these changes will propagate through the connector.
* `DisableAppendNoteColumns`: Prevents the connector from using a separate endpoint for note columns.
