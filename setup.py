from setuptools import setup

setup(
    name="electrum-gmc-server",
    version="1.0",
    scripts=['run_electrum_gmc_server.py','electrum-gmc-server'],
    install_requires=['plyvel','jsonrpclib', 'irc>=11'],
    package_dir={
        'electrumgmcserver':'src'
        },
    py_modules=[
        'electrumgmcserver.__init__',
        'electrumgmcserver.utils',
        'electrumgmcserver.storage',
        'electrumgmcserver.deserialize',
        'electrumgmcserver.networks',
        'electrumgmcserver.blockchain_processor',
        'electrumgmcserver.server_processor',
        'electrumgmcserver.processor',
        'electrumgmcserver.version',
        'electrumgmcserver.ircthread',
        'electrumgmcserver.stratum_tcp',
        'electrumgmcserver.stratum_http'
    ],
    description="Gamecredits Electrum Server",
    author="Thomas Voegtlin",
    author_email="thomasv1@gmx.de",
    license="GNU Affero GPLv3",
    url="https://github.com/Gamecredits-Universe/electrum-gmc-server/",
    long_description="""Server for the Electrum Lightweight Gamecredits Wallet"""
)


