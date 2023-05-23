## 0.4.0 (230523)

Breaking changes:

* This package now provides only syntax highlighting. All roles and directives
  related to proofscape widgets are now deactivated here. Their development
  continues in the `pise/server` project.

## 0.3.2 (230523)

Maintenance:

* Switch from `setup.py` to `setup.cfg`.

## 0.3.1 (220921)

Bug Fixes:

* Syntax highlighting: do not require spaces around `=` in `meson` definition.
* Syntax highlighting: recognize `subdeduc` as node type.

## 0.3.0 (220918)

Enhancements:

* Add syntax highlighting for `proofscape` and `meson` languages.

## 0.2.0 (220823)

Breaking changes:

* `pfsc-defns` directive no longer accepts `:versions:` option.

Enhancements:

* New `pfsc_import_repos` config var accepts dictionary defining
  versions for imported repos globally.
