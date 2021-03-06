import os
import sys

if 'COV_CORE_SOURCE' in os.environ:
    try:
        from pytest_cov.embed import init
        init()
    except Exception as exc:
        sys.stderr.write(
            "pytest-cov: Failed to setup subprocess coverage. "
            "Environ: {0!r} "
            "Exception: {1!r}\n".format(
                dict((k, v) for k, v in os.environ.items() if k.startswith('COV_CORE')),
                exc
            )
        )
