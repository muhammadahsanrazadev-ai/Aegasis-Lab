"""Load-time repairs so Flask-RESTPlus 0.13 can import.

RESTPlus 0.13 imports collections.MutableMapping, which Python 3.10 removed,
and werkzeug.cached_property, which Werkzeug 1.0 no longer exports from the
package root. The brief asks for Flask-RESTPlus, so these aliases stay and
Flask-RESTX is not used.
"""

import collections
import collections.abc

import werkzeug
import werkzeug.utils

collections.MutableMapping = collections.abc.MutableMapping
collections.Mapping = collections.abc.Mapping
if not hasattr(werkzeug, "cached_property"):
    werkzeug.cached_property = werkzeug.utils.cached_property
