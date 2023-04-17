



# Norg Tutorial

*This page is generated from [`./norg_tutorial.norg`](./norg_tutorial.norg)


## Useful Videos

- [From No Org to Neorg - Playlist](https://www.youtube.com/watch%3fv=NnmRVY22Lq8&list=PLx2ksyallYzVI8CN1JMXhEf62j2AijeDa)
    - [From No Org to Neorg - The Basics | #1](https://youtu.be/NnmRVY22Lq8)
    - [From No Org to Neorg - Workflow, Links | #2](https://youtu.be/Bi9JiW5nSig)

I highly recommend you watch these videos by `Vhyrro`, the author of [Neorg](https://github.com/nvim-neorg/neorg/) plugin.


# How to Get Started

The current implementations of `norg` format is mostly done with the [Neorg](https://github.com/nvim-neorg/neorg/) plugin.


## Installation Guide

TL;DR. Read this section. [Installation / Quickstart](https://github.com/nvim-neorg/neorg/%23-installationquickstart)

- I'd recommend following the `Treesitter` section as well to install `tree-sitter-norg` spec.
    - `run = ":Neorg sync-parsers",`
- **Mac Users**: ensure that the CC environment variable points to a compiler that has C++14 support.
    - Details written in github README.
    - [Issue and How to solve](https://github.com/nvim-neorg/tree-sitter-norg/issues/7%23issuecomment-1291508121)


## Kickstart Config

Here is my basic config. I'll explain about `plugins` in [Plugins](#plugins).

```lua
-- lazy.nvim spec
local M = {
    "nvim-neorg/neorg",
    ft = "norg",
    dependencies = {
        "nvim-treesitter/nvim-treesitter",
        "nvim-treesitter/nvim-treesitter-textobjects",
        "nvim-cmp",
        "nvim-lua/plenary.nvim",
    },
    build = ":Neorg sync-parsers",
    cmd = "Neorg",
}
local plugins = {
    ["core.defaults"] = {},
    ["core.norg.completion"] = { config = { engine = "nvim-cmp", name = "[Norg]" } },
    ["core.integrations.nvim-cmp"] = {},
    ["core.export"] = {},
}
M.opts = {
    load = plugins,
}
return M
```


# How to Write Your Notes



## Basics of Plugins

There is a config option `config.load = {}` to define plugins you want to use.

<sub>I decomposed that into a local var `plugins` in above code for simplicity tho.</sub>

More information about plugins in [Plugins](#plugins) section.
I'd recommend just simply adding the ones already stated in [Kickstart Config](#kickstart-config).


## How to Write Notes

Below text is a sample note which explains about the norg syntax.

Run `:Neorg toggle-concealer` to see the raw text.


# Heading 1: [Structural Detached Modifiers](specifications.md#structural-detached-modifiers)

Normal text here.
Single new line will be ignored.

Double new line means a new paragraph.


## Heading 2

Indentation of normal text is advised to align with the start of the heading.
See? The indentation of this text is different from the ones in [Heading 1](#heading-1).

Oh, BTW that's how you create in-document links. Literal heading name wrapped in `{}`.
Press `<Enter>` on the link to jump to the definition.
(case, space **in**-sensitive, punctuation **sensitive**).
More about links in [links](#links)

With `---`, you can decrease the heading level. This text is inside [Heading 1](#heading-1) again.

- Bullet List: [Unordered Lists](specifications.md#unordered-lists)
    - Second level bullet is with `--` and not an indented `-`.
        - Third level
    - Second level

1. Numbered List: [Ordered Lists](specifications.md#ordered-lists)
    1. It's `~`, not `1.`
    - Can be mixed with bullets as well.
2. Second

[Quotes](specifications.md#quotes)
> Quotes
>> Quote level 2

- You can use [TODO lists](specifications.md#todo-status-extension) in combination with these lists.
    - I highly suggest read this section as well.


# Links: [Link Location](specifications.md#link-location)

There are so so many types of useful links in `norg`.
You can also press `<Enter>` on all links to open the appropriate application.
(e.g. urls are opened on the browser.)

Again, `Vhyrro` does a great job explaining about links in his video,
[From No Org to Neorg #2: 17:44~](https://youtu.be/Bi9JiW5nSig%3ft=17m44s) so go ahead and watch that video.


## Links TL;DR

- URL: `{https://xxx.example.com}`
    - URL with name: [Neorg GitHub](https://github.com/nvim-neorg/neorg/)
- Norg files
    - Relative to current file: `{:foo/bar:}` -> `foo/bar.norg`
    - Absolute path: `{:/tmp/foo/bar:}` -> `/tmp/foo/bar.norg`. (Also works with `~` = `$HOME`)
    - Relative to current workspace: `{:$/foo/bar:}` -> `~/Norg/Notes/foo/bar.norg`
    - Relative to different workspace: `{:$work/foo/bar:}` -> `~/Norg/work/foo/bar.norg`
- Usual files: `{/ /path/to/file}`
- Headings: [Heading 1](#heading-1)
    - Any level heading: [Heading 2](#heading-2)

**AND YOU CAN COMBINE THEM**
- `Heading 1` of `foo/bar.norg`: [Heading 1](foo/bar.md#heading-1)
- Line numbers: [4](foo/bar.md#4)


# Attached Modifiers

- \*bold\*: **bold**
- \/italic\/: _italic_
- \_underline\_: <u>underline</u>
- \-strike-through\-: ~~strike-through~~
- \!spoiler\!: |spoiler|
- \^superscript\^: <sup>superscript</sup> (cannot be nested into `subscript`)
- \,subscript\,: <sub>subscript</sub> (cannot be nested into `superscript`)
- \`inline code\`: `inline code` (disables any nested markup - verbatim)
- \%[null modifier](#null-modifier)\%: <!-- null modifier -->
- \$inline math\$: f(x) = y (verbatim)
- \&variable\&: variable (verbatim)


## Export

You can convert your `norg` notes to different formats.

`:Neorg export to-file foo.md` -> Exports to `foo.md` in markdown format.

This is a function to export to `suffix` with the same dir and name of current file
```lua
local export_file = function(suffix, open_preview)
    local dst = vim.fn.fnamemodify(vim.fn.expand("%"), ":~:.:r") .. suffix -- same name but with suffix
    vim.cmd(string.format([[Neorg export to-file %s]], string.gsub(dst, " ", [[\ ]])))
    vim.schedule(function()
        vim.cmd.edit(dst)
        if suffix == ".md" and open_preview then
            vim.cmd([[MarkdownPreview]])
        end
    end)
end
-- export_file(".md", true)
```


# Plugins

Keys passed to `config.load` are name of plugins. Their documents can be found in
[Neorg - Wiki](https://github.com/nvim-neorg/neorg/wiki) -> Pages.

I already mentioned the necessary ones in [Kickstart Config](#kickstart-config), but here are ones I personally use as well.
```lua
["core.norg.concealer"] = { config = { icon_preset = "diamond" } },
["core.norg.esupports.metagen"] = { config = { type = "auto", update_date = true } },
["core.norg.qol.toc"] = {},
["core.norg.qol.todo_items"] = {},
["core.looking-glass"] = {},
["core.presenter"] = { config = { zen_mode = "zen-mode" } },
["core.norg.journal"] = {
    config = {
        strategy = "flat",
        workspace = "Notes",
    },
},
["core.norg.dirman"] = {
    config = {
        workspaces = {
            Notes = "~/Nextcloud/Notes",
            Work = "~/Nextcloud/Work",
        }
    }
},
["core.keybinds"] = {
    -- https://github.com/nvim-neorg/neorg/blob/main/lua/neorg/modules/core/keybinds/keybinds.lua
    config = {
        default_keybinds = true,
        neorg_leader = "<Leader><Leader>",
    },
},
```

## Notes



### `core.norg.dirman`

This plugin is very recommended. It manages what are called _workspaces_.

You can define multiple workspaces at `config["core.norg.dirman"].config.workspaces`, and open with
command `:Neorg workspace <name-of-workspace>`.
This command opens `/path/to/workspace/index.norg` which is like the entry point file.

Norg files inside a workspace can be linked with `{:$<name-of-workspace/path/to/file:}`.

So for example, `~/Nextcloud/Notes/journal/2023-04-16.norg` would be `{:$Notes/journal/2023-04-16:}`.
Or, the same workspace can be abbreviated to `$/`


### `core.norg.journal`

This adds commands `:Neorg journal {today,tomorrow,yesterday}`,
which opens norg file with the appropriate date as name.


### `core.keybinds`

To register `norg` file specific keybinds, read this page: [Neorg - Wiki - User-Keybinds](https://github.com/nvim-neorg/neorg/wiki/User-Keybinds).


## Your Own Module

If you want to create your own plugin for neorg, this video is very useful.
[YouTube - Neorg Custom Modules](https://www.youtube.com/watch%3fv=j4lTvIGRhmw&list=PLxpY86LRR3B0rtOBjXAsq1XnsOt4m4owu)


# Tips



## Sync with Git, Nextcloud, etc

**BACKUP YOUR NOTES**


### Nextcloud, Edit on Your Phone

If you use selfhosted Nextcloud, you can edit your `norg` notes from your phone.


#### After Logging In

1. Install [Notes app](https://apps.nextcloud.com/apps/notes)
2. Go to [https://nextcloud.your.domain/apps/notes](https://nextcloud.your.domain/apps/notes)
3. Go down to `Notes settings`
4. Change `File extension for new notes`
    - `User defined` -> `.norg`


#### On Your Phone

1. Access page with safari. <sub>I'm sorry but I use iPhone...</sub>
    - Shoud work on other phones as well tho.
2. Go to [https://nextcloud.your.domain/apps/notes](https://nextcloud.your.domain/apps/notes)
3. Press `share` to `Add page to home`.
4. You have a new app that jumps directly to notes


#### Notes

- Might not work if you have [Text](https://github.com/nextcloud/text) app installed
