import os

if os.environ['PLATFORM'] == 'basalt':
    def FlagsForFile(filename, **kwargs):
        return {{
            'flags': [
                '-std=c11',
                '-x',
                'c',
                '-Wall',
                '-Wextra',
                '-Werror',
                '-Wno-unused-parameter',
                '-Wno-error=unused-function',
                '-Wno-error=unused-variable',
                '-I{sdk}/Pebble/aplite/include',
                '-I{here}/build',
                '-I{here}',
                '-I{here}/build/src',
                '-I{here}/src',
                '-isystem',
                '{stdlib}',
                '-DRELEASE',
                '-DPBL_PLATFORM_BASALT',
                '-DPBL_COLOR',
                '-D_TIME_H_',
            ],
            'do_cache': True,
        }}
elif os.environ['PLATFORM'] == 'aplite':
    def FlagsForFile(filename, **kwargs):
        return {{
            'flags': [
                '-std=c11',
                '-x',
                'c',
                '-Wall',
                '-Wextra',
                '-Werror',
                '-Wno-unused-parameter',
                '-Wno-error=unused-function',
                '-Wno-error=unused-variable',
                '-I{sdk}/Pebble/aplite/include',
                '-I{here}/build',
                '-I{here}',
                '-I{here}/build/src',
                '-I{here}/src',
                '-isystem',
                '{stdlib}',
                '-DRELEASE',
                '-DPBL_PLATFORM_APLITE',
                '-DPBL_BW',
            ],
            'do_cache': True,
        }}
else:
    raise Exception("Need a platform.")