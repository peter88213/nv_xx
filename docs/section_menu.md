[${Home page}](https://github.com/peter88213/novelibre) > [${Online help}](index.md) > ${Section} menu

---

# ${Section} menu

**Section operation**

## ${Add}

**Add a new section**

With **${Section} > ${Add}**, you can add a section to the tree.

-   The new section is placed at the next free position after the
    selection, if possible.
-   Otherwise, no new section is generated.
-   The new section has an auto-generated title. You can change it in
    the right pane.

### Properties of a new section:

-   *Normal* type
-   *Outline* completion status
-   No viewpoint character assigned
-   No plot line or tag assigned
-   No date/time set

## ${Add multiple sections...}

**Add new sections in bulk**

With **${Section} > ${Add multiple sections...}**, you can add up to 20
sections to the tree.

-   You will be prompted to enter the number of new sections.
-   The number of sections to be added at once is limited to 20.
-   The new sections are placed at the next free position after the
    selection, if possible.
-   Otherwise, no new section is generated.

## ${Set Type}

**Set the type of the selected section**

With **${Section} > ${Set Type}**, you can set the type of the selected
section to *${Normal}* or *${Unused}* .

> **Hint**
> 
> Type change for multiple sections:
> 
> -   Either select multiple sections, or
> -   select a chapter.

## ${Set Status}

**Set the section completion status**

With **${Section} > ${Set Status}**, you can set the completion status 
of the selected section to 
*${Outline}*, *${Draft}*, *${1st Edit}*, *${2nd Edit}*, or *${Done}*.

> **Hint**
> 
> Status change for multiple sections:
> 
> -   Either select multiple sections, or
> -   select a parent node (chapter or Book)

## ${Set Viewpoint...}

**Assign a viewpoint character to the section**

With **${Section} > ${Set Viewpoint...}**, you open a pop-up window with a
dropdown list containing all characters in the tree view's sort order.
Click on the character you want to assign as viewpoint character. If you
click on the topmost entry (the blank one) of the list, this will clear
the viewpoint association.

> **Hint**
> 
> Select a parent node to set the viewpoint for all subordinate sections.

## ${Export section descriptions for editing}

**Export an ODT document that can be imported again after editing**

With **${Section} > ${Export section descriptions for editing}**, you can
create a text document with a **full synopsis** containing part/chapter
headings and section descriptions that can be edited and reimported.
File name suffix is `_sections_tmp`.

## ${Section table (export only)}

**Export an ODS document**

With **${Section} > ${Section table (export only)}**, you can create a
spreadsheet with a row per section, containing the following data:

-   Section ID (hidden)
-   Section number (link to manuscript)
-   Title
-   Description
-   Viewpoint
-   Date
-   Time
-   Day
-   Duration
-   Tags
-   Section notes
-   Scene
-   Goal
-   Conflict
-   Outcome
-   Status
-   Words total
-   Word count
-   Characters
-   Locations
-   Items

> **Note**
> 
> Only "${Normal}" sections appear in the section table. Sections of the
> "Unused" type are omitted.

File name suffix is `_sectionlist`.

Clicking on a section number with `${Ctrl}` pressed, you can jump to the
corresponding section in the manuscript. However, if you edit this
spreadsheet, you cannot apply the changes with *novelibre* (in contrast
to the [plot grid](plot_menu.html#export-plot-grid-for-editing)). The
section table is more intended for extracting the metadata of the
writing project, for example, in the case of abandoning *novelibre*.

## ${Show Time table}

**Show an HTML report with a time table**

With **${Section} > ${Show Time table}**, you can create a HTML file that
contains a time table, and launch your system's web browser for
displaying it.

In the time table, the dated "${Normal}" sections are listed in
chronological order. In addition to date/time and duration, the columns
include the section title, description, locations and characters as well
as plot lines with plot notes.

> **Note**
> 
> The report is a temporary file, auto-deleted on program exit. If needed,
> you can have your web browser save or print it.

---

[English manual](https://peter88213.github.io/nvhelp-en/)

