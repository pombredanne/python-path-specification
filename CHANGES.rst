
Change History
==============


0.5.6 (TBD)
-----------

- Improved unit tests.
- Improved type checking.



0.5.5 (2017-09-09)
------------------

- Add documentation link to README.


0.5.4 (2017-09-09)
------------------

- `Issue #17`_: Add link to Ruby implementation of *pathspec*.
- Add sphinx documentation.

.. _`Issue #17`: https://github.com/cpburnz/python-path-specification/pull/17


0.5.3 (2017-07-01)
------------------

- `Issue #14`_: Fix byte strings for Python 3.
- `Issue #15`_: Include "LICENSE" in source package.
- `Issue #16`_: Support Python 2.6.

.. _`Issue #14`: https://github.com/cpburnz/python-path-specification/issues/14
.. _`Issue #15`: https://github.com/cpburnz/python-path-specification/pull/15
.. _`Issue #16`: https://github.com/cpburnz/python-path-specification/issues/16


0.5.2 (2017-04-04)
------------------

- Fixed change log.


0.5.1 (2017-04-04)
------------------

- `Issue #13`_: Add equality methods to `PathSpec` and `RegexPattern`.

.. _`Issue #13`: https://github.com/cpburnz/python-path-specification/pull/13


0.5.0 (2016-08-22)
------------------

- `Issue #12`_: Add `PathSpec.match_file()`.
- Renamed `gitignore.GitIgnorePattern` to `patterns.gitwildmatch.GitWildMatchPattern`.
- Deprecated `gitignore.GitIgnorePattern`.

.. _`Issue #12`: https://github.com/cpburnz/python-path-specification/issues/12


0.4.0 (2016-07-15)
------------------

- `Issue #11`_: Support converting patterns into regular expressions without compiling them.
- API change: Subclasses of `RegexPattern` should implement `pattern_to_regex()`.

.. _`Issue #11`: https://github.com/cpburnz/python-path-specification/issues/11


0.3.4 (2015-08-24)
------------------

- `Issue #7`_: Fixed non-recursive links.
- `Issue #8`_: Fixed edge cases in gitignore patterns.
- `Issue #9`_: Fixed minor usage documentation.
- Fixed recursion detection.
- Fixed trivial incompatibility with Python 3.2.

.. _`Issue #7`: https://github.com/cpburnz/python-path-specification/pull/7
.. _`Issue #8`: https://github.com/cpburnz/python-path-specification/pull/8
.. _`Issue #9`: https://github.com/cpburnz/python-path-specification/pull/9


0.3.3 (2014-11-21)
------------------

- Improved documentation.


0.3.2 (2014-11-08)
------------------

- `Issue #5`_: Use tox for testing.
- `Issue #6`_: Fixed matching Windows paths.
- Improved documentation.
- API change: `spec.match_tree()` and `spec.match_files()` now return iterators instead of sets.

.. _`Issue #5`: https://github.com/cpburnz/python-path-specification/pull/5
.. _`Issue #6`: https://github.com/cpburnz/python-path-specification/issues/6


0.3.1 (2014-09-17)
------------------

- Updated README.


0.3.0 (2014-09-17)
------------------

- `Issue #3`_: Fixed trailing slash in gitignore patterns.
- `Issue #4`_: Fixed test for trailing slash in gitignore patterns.
- Added registered patterns.

.. _`Issue #3`: https://github.com/cpburnz/python-path-specification/pull/3
.. _`Issue #4`: https://github.com/cpburnz/python-path-specification/pull/4


0.2.2 (2013-12-17)
------------------

- Fixed setup.py.


0.2.1 (2013-12-17)
------------------

- Added tests.
- Fixed comment gitignore patterns.
- Fixed relative path gitignore patterns.


0.2.0 (2013-12-07)
------------------

- Initial release.
