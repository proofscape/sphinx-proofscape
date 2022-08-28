Page B
======

This is Page B.

There are no widgets on this page.
So there should be no ``<script>`` tag defining a ``pfsc_widget_data``.

.. code-block:: proofscape

    from gh.foo.bar import spam as eggs

    # This is a comment.
    deduc Thm {
        supp P {
            sy="$P$"
        }
        asrt C {
            en='$C$'
        }
        meson = "
        Suppose P. Then C.
        "
    }

    deduc Pf of Thm.C {
        asrt A {
            fr="""$A$"""
        }
        asrt B {
            de='''$B$'''
        }
        meson = '
        From Thm.P get A. Then B, hence Thm.C.
        '
    }
