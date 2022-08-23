import json

import pytest
from bs4 import BeautifulSoup


def test(app):
    app.build()


def get_chart_widget_anchors(html):
    """
    Get the list of any and all <a> tags having class `chartWidget`.
    """
    soup = BeautifulSoup(html, 'html.parser')
    return list(soup.find_all('a', class_='chartWidget'))


def get_widget_data_from_script_tag(html):
    """
    If the HTML contains a <script> tag defining pfsc_widget_data, then parse
    the JSON and return the widget data itself.

    Otherwise return None.
    """
    soup = BeautifulSoup(html, 'html.parser')
    intro = '\nconst pfsc_widget_data = '
    for s in soup.find_all('script'):
        if s.text.startswith(intro):
            rem = s.text[len(intro):]
            data = json.loads(rem)
            return data
    return None


@pytest.mark.sphinx(buildername='html')
def test_sphinx_build(app, status, warning):
    app.build()
    assert not status.read()
    assert not warning.read()

    # Page A
    # ======
    html = (app.outdir / 'pageA.html').read_text()

    # Have exactly one chart widget anchor tag, and it has a class encoding its UID.
    A = get_chart_widget_anchors(html)
    assert len(A) == 1
    assert 'test-foo-doc-_sphinx-pageA-w0_WIP' in A[0].get('class')

    # Defines the expected pfsc_widget_data
    wd = get_widget_data_from_script_tag(html)
    assert len(wd) == 1
    #print('\n', json.dumps(wd[0], indent=4))
    assert wd[0] == {
        "view": [
            "gh.foo.bar.H.ilbert.ZB.Thm168.Pf"
        ],
        "versions": {
            "gh.foo.bar": "v1.2.3"
        },
        "pane_group": "test.foo.doc@WIP._sphinx.pageA:CHART:",
        "src_line": 12,
        "type": "CHART",
        "uid": "test-foo-doc-_sphinx-pageA-w0_WIP",
        "version": "WIP",
        "widget_libpath": "test.foo.doc._sphinx.pageA.w0"
    }

    # Page B
    # ======
    html = (app.outdir / 'pageB.html').read_text()

    # Does not define pfsc_widget_data
    assert get_widget_data_from_script_tag(html) is None

    # Page C
    # ======
    html = (app.outdir / 'foo/pageC.html').read_text()

    # Get the expected anchor tags:
    A = get_chart_widget_anchors(html)
    for i, (a, expected_label) in enumerate(zip(A, PAGE_C_WIDGETS_LABELS)):
        assert f'test-foo-doc-_sphinx-foo-pageC-w{i}_WIP' in a.get('class')
        assert a.text == expected_label

    # Get the expected pfsc_widget_data:
    wd = get_widget_data_from_script_tag(html)
    #print('\n', json.dumps(wd, indent=4))
    assert wd == PAGE_C_WIDGET_DATA


PAGE_C_WIDGETS_LABELS = [
    'chart widget',
    'chart widgets',
    'substitutions',
    'one-line color definition',
    'color defn with repeated LHS, plus use of update',
]


PAGE_C_WIDGET_DATA = [
    {
        "view": [
            "gh.foo.bar.H.ilbert.ZB.Thm168.Pf"
        ],
        "versions": {
            "gh.foo.bar": "v1.2.3"
        },
        "pane_group": "test.foo.doc@WIP._sphinx.foo.pageC:CHART:",
        "src_line": 16,
        "type": "CHART",
        "uid": "test-foo-doc-_sphinx-foo-pageC-w0_WIP",
        "version": "WIP",
        "widget_libpath": "test.foo.doc._sphinx.foo.pageC.w0"
    },
    {
        "view": [
            "gh.foo.bar.H.ilbert.ZB.Thm168.Thm"
        ],
        "versions": {
            "gh.foo.bar": "v1.2.3"
        },
        "pane_group": "test.foo.doc@WIP._sphinx.foo.pageC:CHART:",
        "src_line": 18,
        "type": "CHART",
        "uid": "test-foo-doc-_sphinx-foo-pageC-w1_WIP",
        "version": "WIP",
        "widget_libpath": "test.foo.doc._sphinx.foo.pageC.w1"
    },
    {
        "on_board": [
            "gh.foo.spam.H.ilbert.ZB.Thm168.X1"
        ],
        "off_board": [
            "gh.foo.spam.H.ilbert.ZB.Thm168.X2"
        ],
        "view": [
            "gh.foo.bar.H.ilbert.ZB.Thm168.Thm.A10",
            "gh.foo.bar.H.ilbert.ZB.Thm168.Pf.A10",
            "gh.foo.bar.H.ilbert.ZB.Thm168.Pf.A20"
        ],
        "color": {
            ":olB": [
                "gh.foo.bar.H.ilbert.ZB.Thm168.Pf.A10",
                "gh.foo.bar.H.ilbert.ZB.Thm168.Pf.A20"
            ],
            ":bgG": [
                "gh.foo.bar.H.ilbert.ZB.Thm168.Thm.A10"
            ]
        },
        "versions": {
            "gh.foo.spam": "WIP",
            "gh.foo.bar": "v1.2.3"
        },
        "pane_group": "test.foo.doc@WIP._sphinx.foo.pageC:CHART:",
        "src_line": 32,
        "type": "CHART",
        "uid": "test-foo-doc-_sphinx-foo-pageC-w2_WIP",
        "version": "WIP",
        "widget_libpath": "test.foo.doc._sphinx.foo.pageC.w2"
    },
    {
        "view": [
            "gh.foo.bar.H.ilbert.ZB.Thm168.Pf"
        ],
        "color": {
            ":olB": [
                "gh.foo.bar.H.ilbert.ZB.Thm168.Pf.A10",
                "gh.foo.bar.H.ilbert.ZB.Thm168.Pf.A20"
            ]
        },
        "versions": {
            "gh.foo.bar": "v1.2.3"
        },
        "pane_group": "test.foo.doc@WIP._sphinx.foo.pageC:CHART:",
        "src_line": 40,
        "type": "CHART",
        "uid": "test-foo-doc-_sphinx-foo-pageC-w3_WIP",
        "version": "WIP",
        "widget_libpath": "test.foo.doc._sphinx.foo.pageC.w3"
    },
    {
        "color": {
            ":bgG": [
                "gh.foo.bar.H.ilbert.ZB.Thm168.Pf.A10",
                "gh.foo.bar.H.ilbert.ZB.Thm168.Pf.A20",
                "gh.foo.bar.H.ilbert.ZB.Thm168.Thm.A10"
            ],
            ":update": True
        },
        "versions": {
            "gh.foo.bar": "v1.2.3"
        },
        "pane_group": "test.foo.doc@WIP._sphinx.foo.pageC:CHART:",
        "src_line": 44,
        "type": "CHART",
        "uid": "test-foo-doc-_sphinx-foo-pageC-w4_WIP",
        "version": "WIP",
        "widget_libpath": "test.foo.doc._sphinx.foo.pageC.w4"
    }
]
