"""
django-lessons
"""
__version_info__ = {
    'major': 1,
    'minor': 5,
    'micro': 3,
    'releaselevel': 'final',
    'serial': 1,
}


def get_version():
    """
    Return the formatted version information
    """
    vers = ["%(major)i.%(minor)i" % __version_info__, ]

    if __version_info__['micro']:
        vers.append(".%(micro)i" % __version_info__)
    if __version_info__['releaselevel'] != 'final':
        vers.append('%(releaselevel)s%(serial)i' % __version_info__)
    return ''.join(vers)

__version__ = get_version()
