name = 'usdmanager'

version = '0.13.0.sse.1.0.0'

authors = [
	'Dreamworks'
]

description = '''USD Manager'''

with scope('config') as c:
	# Determine location to release: internal (int) vs external (ext)
	# NOTE: Modify this variable to reflect the current package situation
	release_as = 'ext'

	# The 'c' variable here is actually rezconfig.py
	# 'release_packages_path' is a variable defined inside rezconfig.py

	import os
	if release_as == 'int':
		c.release_packages_path = os.environ['SSE_REZ_REPO_RELEASE_INT']
	elif release_as == 'ext':
		c.release_packages_path = os.environ['SSE_REZ_REPO_RELEASE_EXT']

requires = [
	"python-3",
	"pyside2_setup",
	"qtpy",
]

private_build_requires = [
]

variants = [
	['platform-linux', 'arch-x86_64', 'os-centos-7'],
]

def commands():
	env.REZ_USDMANAGER_ROOT = '{root}'

	env.PYTHONPATH.append('{root}')
	env.PATH.append('{root}/scripts')

build_command = 'rez python {root}/rez_build.py'

uuid = 'repository.usdmanager'

